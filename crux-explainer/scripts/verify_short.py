"""Fully decode a Shorts master and check the Crux delivery defaults."""
import argparse
import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--story-end', type=float, help='First CTA frame time in seconds')
    parser.add_argument('--ffmpeg', default='ffmpeg')
    parser.add_argument('--ffprobe', default='ffprobe')
    args = parser.parse_args()
    source = str(args.video.resolve(strict=True))
    result = subprocess.run(
        [args.ffprobe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', source],
        capture_output=True, text=True, check=True)
    media = json.loads(result.stdout)
    video = next((s for s in media['streams'] if s['codec_type'] == 'video'), None)
    audio = next((s for s in media['streams'] if s['codec_type'] == 'audio'), None)
    if not video or not audio:
        sys.exit('Expected a video stream and an audio stream.')
    fps = Fraction(video['avg_frame_rate'])
    duration = float(video.get('duration', media['format']['duration']))
    errors = []
    if (video['width'],video['height'],fps,video['codec_name'],audio['codec_name']) != (1080,1920,30,'h264','aac'):
        errors.append('Master must be 1080 x 1920, 30 fps, H.264 with AAC audio for this preset.')
    if args.story_end is not None:
        cta = duration - args.story_end
        if args.story_end <= 0 or not 2 - 1/30 <= cta <= 3 + 1/30:
            errors.append(f'CTA duration {cta:.2f}s is outside the 2-3 second range.')
        print(f'CTA: {cta:.2f}s')
    measured = subprocess.run(
        [args.ffmpeg,'-hide_banner','-nostats','-xerror','-i',source,'-map','0:v:0','-map','0:a:0',
         '-af','ebur128=peak=true','-f','null','-'],
        capture_output=True, text=True, check=True)
    summary = measured.stderr.rsplit('Summary:',1)[-1]
    for pattern,label,unit in [(r'^\s*I:\s+(-?inf|[-\d.]+)','Integrated loudness','LUFS'),
                               (r'^\s*Peak:\s+(-?inf|[-\d.]+)','True peak','dBTP')]:
        match = re.search(pattern, summary, re.MULTILINE)
        if match:
            print(f'{label}: {match[1]} {unit}')
            level = float(match[1])
            if level == float('-inf'):
                errors.append('Audio appears silent.')
            elif unit == 'dBTP' and level > -1:
                errors.append('True peak is above -1 dBTP.')
        else:
            errors.append(f'{label} could not be measured.')
    print(f'{args.video.name}: {video["width"]} x {video["height"]}, {fps} fps, {duration:.2f}s. Full decode passed.')
    if errors:
        sys.exit('\n'.join(errors))
    print('Review captions, voice, scene effects, and visual accuracy manually.')


if __name__ == '__main__':
    main()
