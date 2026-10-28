# Agent instructions: manara-home-integration

Read by AI coding agents (Antigravity, Claude Code and others). Humans: see [README.md](README.md).

## What this repo is

The `manara_home` Home Assistant custom integration (HACS), the site-side half of the Manara platform. Architecture and locked decisions live in [ManaraEngineering/manara-platform](https://github.com/ManaraEngineering/manara-platform), especially ADRs 0002, 0004, 0005, 0006, 0008 and 0009. Follow them; if a task seems to conflict, stop and ask.

## Ground rules

- **Never commit secrets:** tokens, keys, certificates, `secrets.yaml`, `.env`. Gitleaks runs in pre-commit and CI.
- **Contracts are vendored, never hand-edited.** `custom_components/manara_home/contracts/` is a pinned copy from manara-platform. Change schemas there, then run `python scripts/sync_contracts.py ../manara-platform`.
- **Only allowlisted data leaves a site.** Anything published must validate against the vendored `health.v1.json` or `inventory.v1.json`. Cameras, voice and location never leave a site. Analytics is opt-in per site and per data class.
- Target **current Home Assistant (2026.10+) on Python 3.14**. HA now uses `probatio` instead of `voluptuous` for schemas; follow current core integrations, not older examples.
- Keep `manifest.json` keys ordered: `domain`, `name`, then alphabetical (hassfest enforces this).
- Work on `develop` or a branch off it. Never commit to `main` directly.

## Commands

Home Assistant does not install on Windows. On this machine, run checks in WSL:

```sh
wsl -e bash scripts/check.sh          # ruff, ruff format --check, mypy, pytest
```

On Linux or macOS, run `bash scripts/check.sh` with a Python 3.14 venv at `~/.venvs/manara-home-integration` (or set `MANARA_VENV`).

Pre-commit on Windows: set `VIRTUALENV_OVERRIDE_APP_DATA=%USERPROFILE%\.cache\venvdata` first.

## Tests

- Use `pytest-homeassistant-custom-component` fixtures (`hass`, `MockConfigEntry`).
- Every config-flow step and every publish path needs a test. Publishing tests must assert that payloads validate against the vendored schema.
