---
name: development-readiness
description: Assess whether this learning-lab repository is ready to begin a new development task. Use when asked for a development-readiness assessment or blockers to starting new work.
---

# Development readiness

Perform a read-only assessment. Do not modify files or Git state.

1. Read and follow `AGENTS.md`, and read `docs/project-context.md` plus any other durable context needed to understand the repository.
2. Check the current branch and working-tree state with `git status --short --branch`.
3. Run the repository's existing local verification as documented in the project context. Currently, use `python3 -B verify_demo.py` to avoid writing bytecode.
4. Report the checks performed, their results, and anything that would block beginning a new development task. If no blockers were found, say so; distinguish non-blocking observations and verification limitations.
5. Do not perform additional repository-health or Git-integrity checks unless the preceding results give a concrete reason. State that reason before running a targeted read-only check.
