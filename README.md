# Manara Home integration

The `manara_home` Home Assistant custom integration, installed through HACS. It is the site-side half of the Manara platform.

> Proprietary. See [LICENSE](LICENSE). **Status: skeleton.** It loads and its config flow opens with no fields. Nothing else is implemented yet.

## What it will do

| Area | Summary | Decision |
|---|---|---|
| Enrolment | Show QR codes with one-time codes; sign device CSRs through the provisioning Worker | [ADR 0005](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0005-remote-access.md), [ADR 0006](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0006-provisioning-worker.md) |
| Device profiles | Phone, tablet, wall panel and TV profiles served to the Manara Home app | [ADR 0003](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0003-client-app-fork.md) |
| TV control | Switch TV dashboards with `manara://navigate/<path>` over ADB | [ADR 0004](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0004-site-integration.md) |
| Fleet health and revocation | Track enrolled devices; revoke a certificate and remove its HA session | [ADR 0004](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0004-site-integration.md) |
| Consent switches | Health, inventory and per-class analytics opt-in | [ADR 0002](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0002-data-leaving-a-site.md) |
| Publishing | Push allowlisted health and inventory to `ingest.manara.co.in`, buffered when the hub is down | [ADR 0008](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0008-telemetry.md) |
| Maintainer switch | 24-hour support access, logged and notified | [ADR 0009](https://github.com/ManaraEngineering/manara-platform/blob/develop/docs/adr/0009-support-access.md) |

## Contracts

Data shapes come from the platform [contracts](https://github.com/ManaraEngineering/manara-platform/tree/develop/contracts). A pinned copy is vendored in [custom_components/manara_home/contracts/](custom_components/manara_home/contracts/), so it ships through HACS and can enforce the health allowlist on site. [VERSION](custom_components/manara_home/contracts/VERSION) records the platform commit.

Never edit the vendored files. Change them in `manara-platform`, then run:

```sh
python scripts/sync_contracts.py ../manara-platform
```

TODO: a CI check that the vendored copy matches the pinned platform commit. It needs a token that can read the private platform repo.

## Install (HACS)

In HACS, open the menu → **Custom repositories**, add `https://github.com/ManaraEngineering/manara-home-integration` with type **Integration**, then install **Manara Home** and restart Home Assistant.

TODO: if the repo goes private after the MVP, HACS needs a GitHub token with access to it, or another distribution route.

## Develop

Home Assistant does not support Windows, so run tests on Linux, macOS or WSL.

```sh
uv venv -p 3.14 ~/.venvs/manara-home-integration
VIRTUAL_ENV=~/.venvs/manara-home-integration uv pip install -r requirements_test.txt
bash scripts/check.sh                 # from Windows: wsl -e bash scripts/check.sh
```

Install the hooks with `pre-commit install`. In an IDE, open `manara-platform/manara.code-workspace` for all repos together, with tasks for these checks.

## Branching

`develop` is the default branch and all work lands there by PR. `main` is stable.

`main` is protected: it requires a PR, and the `lint`, `test`, `hassfest`, `hacs` and `secrets` checks must pass.
