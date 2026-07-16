# Routing proxy judge prompt

You are a skill-routing judge. Below is the complete active list of skills in
this isolated environment. For each prompt, return the single skill you would
invoke, or `none`.

Output exactly one line per prompt:

```text
<number>: <skill-name-or-none>
```

Do not explain your choices and do not inspect any other file.

## Skills

`taste-extractor`: Extracts portable taste from any accessible medium into an
evidence-traced profile and downstream production brief. Use for extracting,
distilling, reverse-engineering, or capturing the style, taste, feel, visual
language, voice, or character of an interface, image, text, video, music,
object, brand, or experience so another agent can create new work with the same
character without copying source content. Also use for cross-medium style
translation and refuse fabrication when the source cannot be inspected. Not
for directly generating the final artifact unless asked for both extraction
and creation.

`skill-creator`: Create or update an Agent Skill with specialized knowledge,
workflows, or tool integrations.

`imagegen`: Generate or edit raster images such as illustrations, photos,
textures, sprites, mockups, or cutouts.

`humanizer`: Rewrite text to remove signs of AI-generated writing and make it
sound more natural.

`naming-as-design`: Repair muddy, overlapping, or conflicting names that
distort a product or workflow's mental model.

`local-mythology`: Articulate a project's identity when naming, tone, scope, or
product character is drifting.

`dojo`: Create, test, harden, pressure-test, or evaluate an Agent Skill and
produce release evidence.

`james`: Cold-review a planning document for future-agent restartability using
only declared project-owned context.

## Prompts

1. Pull the taste out of these three landing pages and give another agent a reusable brief.
2. Reverse-engineer the voice of this essay without copying phrases so we can use its character in onboarding.
3. What makes this ceramic collection feel like itself? Translate that into rules for a status page.
4. I have timestamped notes from a music video. Extract its motion and pacing grammar for another launch-film agent.
5. Distill the feel of this synth track into a production handoff for a game sound designer.
6. Use the service ritual in these restaurant observations as taste input for a new app flow.
7. Use taste-extractor on this link. If you cannot inspect it, tell me what evidence you need instead of guessing.
8. Build an evidence-traced style profile from these product photos without copying their literal compositions.
9. Across these three packaging variants, extract what is invariant and what a new variant may change.
10. Create a new Agent Skill that teaches agents how to reconcile CSV schemas.
11. Use Dojo to test the taste-extractor skill before I publish it.
12. Generate a transparent-background bitmap illustration of a sleepy capybara.
13. Rewrite this paragraph so it sounds natural instead of AI-generated.
14. These three product concepts all use “workspace” differently. Fix the naming model.
15. James-review this implementation plan so a future agent can execute it cold.
