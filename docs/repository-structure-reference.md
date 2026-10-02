# Repository structure reference

This first version is the canonical structural reference for future AI-assisted
projects. It records only the roles established in this repository. Reuse the
separation of responsibilities; adapt project content and tooling to each project.

## Core/template structure

| Component | Purpose and when used | What belongs here | What does not belong here |
| --- | --- | --- | --- |
| `AGENTS.md` | Codex entry point, read when working in the repository. | A minimal directive to read and follow `instructions/core.md`. | Duplicated shared rules, project context, or implementation. |
| `CLAUDE.md` | Claude entry point, importing the same shared instructions. | The native import `@instructions/core.md`. | A second copy of shared rules or project documentation. |
| `instructions/core.md` | Tool-independent source of shared repository rules, followed through either bootstrap. | Applicable constraints and protected-file rules. | Application code, transient task notes, or duplicated descriptive context. |
| `docs/` | Durable reference material, consulted to understand the project and its structure. | The established context and structure documents below. | Application implementation, executable checks, or temporary experiment logs. |
| `docs/project-context.md` | Durable project facts used to recover context across sessions. | Purpose, application overview, constraints, verification, and an accurate CI summary. | Temporary labels or intentional failures presented as requirements; replacement rules that conflict with `instructions/core.md`. |
| `docs/repository-structure-reference.md` | Canonical reference used when interpreting or reusing this repository structure. | Established component roles, boundaries, and relationships. | Tutorials, task history, or unstandardized future layouts. |

The bootstraps route agents to shared instructions; project context describes the
project; this reference describes where those responsibilities live. Summaries in
documentation must remain consistent with the shared rules and executable files.

## Project-specific implementation and automation

These files exist in the lab, but their names, technologies, and behavior are not
universal template requirements.

| Component | Purpose and when used | What belongs here | What does not belong here |
| --- | --- | --- | --- |
| `index.html` | Browser demo, opened directly without a build step. | All current demo markup and JavaScript, including buttons that reveal hidden messages. | Agent instructions, repository documentation, or verification logic. |
| `verify_demo.py` | Local verification, run with `python3 verify_demo.py`, and invoked by CI. | Standard-library `unittest` checks of required HTML content. It is currently protected from modification by shared instructions. | Application behavior or claims of browser interaction coverage: these checks only inspect source text. |
| `.github/workflows/verify.yml` | GitHub Actions configuration for verification on pushes and pull requests. | Checkout and execution of `python3 verify_demo.py` on `ubuntu-latest`, with read-only repository-content permissions. | Shared agent rules, application code, or a duplicate implementation of the tests. |

CI invokes verification, verification reads `index.html`, and project context
summarizes that arrangement. The workflow is the executable source for CI behavior.

The single-file application rule, dependency restriction, protected verifier, and
`LAB RULE APPLIED` response marker are current lab rules, not requirements imposed
on every future project by this template. Greeting labels and temporary lab
experiments likewise do not define the reusable structure. Existing lab rules
remain applicable here.

## Optional expansion structures

No optional expansion layout is standardized in this version. Such structures
will be documented later when established; this reference defines no layout for
skills, MCP, hooks, subagents, procedures, or other future extensions.
