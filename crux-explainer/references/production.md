# Production and delivery

## Script and shots

Start the Short with motion and the core question. Build around a single cause-and-effect chain and give each shot one job. Favor punchy, conversational speech and visible transitions. Use timing from narration to anchor cuts. For each beat record spoken line, claim ID, what moves, camera angle and move, lighting intention, SFX, and caption or necessary label. Aim for a compact runtime that lets the mechanism land. Across a series, vary the pacing, setting, and visual demonstration to suit each story.

## Visual direction

Use the available renderer that best serves the scene, such as Blender for modeled environments or a deterministic Three.js scene for a procedural demo. Inspect the source project or renderer setup first. Use original or commercially cleared assets. Start with a motivated key, soft fill, disciplined palette, and separation of the subject from the background. Use restrained glow only where it supports a light source, contact marker, or reveal. Check highlights and local contrast on a phone-sized preview.

Favor visual effects like a contact highlight, light sweep, shadow crossing a planet, frost spreading, a cutaway, or a movement trail where they explain a change. Avoid persistent decoration. Time effects to the actual movement, diagram state, and narrated beat. Use short phrase captions in a consistent position within safe areas. Keep the top free of repetitive headings and use labels only for quantities, distinctions, or scale notes viewers need. Keep text off faces and key actions.

## Audio and captions

If using ElevenLabs, verify model, voice ID, API access, and commercial rights for the account before a full batch. For Brian, the tested voice ID is nPczCjzI2devNBz1zQrb. Use the officially supported Eleven v4 API and Creative stability where compatible. Automatically insert sparse bracketed delivery tags from the shot plan, such as [curious] for a hook, [clear and precise] for a mechanism, or [awed] for a reveal. Check performance and timing with a short sample. If the provider denies the voice or plan, report the exact blocker and use a substitute only when authorized. Read credentials from environment variables or an approved secret store.

Align edited captions to provider timestamps or verified forced alignment. Remove delivery tags from captions, and re-align after any tempo or trimming changes. Use a soothing ambient music bed with ducking and a restrained sound matched to each important action. Examples include a rail roll, crystal tick, soft sweep, water splash, or CTA click. Listen to narration intelligibility in mono and on small speakers. Around -16 LUFS integrated and -1.5 dBTP is a useful mixing baseline, subject to the material.

## Export and quality gate

Default to a 1080 x 1920 H.264 MP4 at 30 fps with AAC audio and a 9:16 cover. Render stills for the hook, mechanism, payoff, and CTA before long renders. Check each shot during motion for geometry, framing, clipping, seams, exposure, caption sync, and comprehension. End with a roughly 2.5-second visual Crux Uncovered subscribe card, kept clear of Shorts UI. Reuse the approved channel identity and verify the handle from the owner or supplied reference. A subtle click and music tail can accompany the card.

Watch and listen to the final rendered file, then fully decode it. Run python scripts/verify_short.py PATH_TO_MP4 --story-end SECONDS, using the timestamp of the first CTA frame. Use --story-end only when the video has a CTA. Technical checks supplement the viewing pass. Check a sample of caption and SFX events against the waveform and frame, and check that narration ends before the CTA. Provide the MP4, JPG cover, captions or timing, metadata, and evidence and rights records for complete productions. Keep project sources and report any item still awaiting a check.
