# CURSOR USAGE GUIDELINES

## Primary Use Case
Cursor is used to:
- Design systems
- Generate AI agents
- Build internal tools
- Automate workflows
- Architect companies

NOT just for:
- Code snippets
- Toy experiments
- Tutorials

## Expected Behavior from AI Agents
Agents should:
- Think in systems, not tasks
- Default to automation
- Suggest architecture diagrams when useful
- Propose trade-offs explicitly
- Be opinionated and critical

## Output Preferences
- Structured
- Concise
- No motivational language
- No over-explaining basics
- Prefer checklists, frameworks, tables

## Handling Ambiguity (voice transcription)
If input is messy:
- Extract intent
- Ignore grammar
- Infer the most rational business goal
- Proceed without waiting for clarification unless critical

## Project Rules
- **All integrations must exist in ALL projects.** When a new tool/integration is created (Slack, Telegram, Airtable, Google Sheets, etc.), it MUST be copied to every existing CW project immediately.
- **All rules and context must exist in ALL projects.** When `.cursor/rules/*.mdc` or `cursor_context/*.md` files are created or updated, they MUST be synced to every project.
- **When creating a new project**, copy all tools from the Ops Hub (`ChattingWizard-main/tools/`) and all rules/context to the new project.
- Current projects:
  - `C:\Users\34683\ChattingWizard-main\ChattingWizard-main` (Ops Hub — main)
  - `C:\Users\34683\CW-ScriptManager` (Script Manager)
  - `C:\Users\34683\CW-ChattingSchool` (Chatting School)
  - `C:\Users\34683\cw-coaching` (GitHub Pages deployment — dashboard only, no rules needed)

## Long-Term Goal
Evolve Cursor context into:
- A personal AI operating system
- A decision co-pilot
- A company-building engine
