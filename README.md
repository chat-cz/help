# Chat.cz — nápověda (mkdocs)

This repository contains the MkDocs-powered documentation site for Chat.cz.

## Quickstart (local)

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Serve locally with live reload:

```bash
python -m mkdocs serve -w ./ --livereload
```

Open http://127.0.0.1:8000 in your browser.

## Build (production)

```bash
python -m mkdocs build
```

The static site will be generated into the `site/` folder.

## VS Code

The repository includes a `.vscode/launch.json` configuration that runs MkDocs using the workspace virtualenv and enables live reload. To use it:

- Open this folder in VS Code.
- Select the Python interpreter `.venv/bin/python` (bottom-right selector).
- Open Run and Debug (Ctrl+Shift+D) and run "MkDocs: serve (venv)".

## CI

A GitHub Actions workflow is provided to validate that `mkdocs build` succeeds on pushes and PRs to `main`.

## Notes

- `requirements.txt` currently contains `mkdocs` and `mkdocs[i18n]`. Consider pinning exact versions for reproducible installs.
- Custom theme overrides live in `custom_theme/`.

---
