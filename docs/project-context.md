# Project context

- **Purpose:** Vibe Coding Lab is a minimal browser demo with buttons that reveal greeting messages.
- **Application:** All page markup and JavaScript live in `index.html`. Open it directly in a browser; no build step is required. Click handlers reveal initially hidden message elements.
- **Constraints:** Keep application implementation in `index.html` and do not add external dependencies. Repository instructions protect `verify_demo.py` from modification.
- **Verification:** Run `python3 verify_demo.py`. It uses Python's standard-library `unittest` to check the HTML for an expected button label and message. These are static content checks; they do not exercise browser click behavior.
- **CI:** `.github/workflows/verify.yml` runs the same verification on GitHub Actions for pull requests, using an Ubuntu runner.

Temporary experiment labels and intentional test failures are not project requirements.
