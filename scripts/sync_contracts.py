"""Copy contract schemas from a manara-platform checkout into the integration.

Usage: python scripts/sync_contracts.py ../manara-platform

Copies contracts/*.json (schemas only, not examples) and records the
platform commit in custom_components/manara_home/contracts/VERSION.
Never edit the vendored files by hand; change them in manara-platform.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

DEST = (
    Path(__file__).resolve().parent.parent / "custom_components/manara_home/contracts"
)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    platform = Path(sys.argv[1]).resolve()
    src = platform / "contracts"
    if not src.is_dir():
        print(f"not a manara-platform checkout: {platform}")
        return 2

    if subprocess.run(
        ["git", "-C", str(platform), "status", "--porcelain", "contracts"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip():
        print("manara-platform/contracts has uncommitted changes; commit them first")
        return 1
    sha = subprocess.run(
        ["git", "-C", str(platform), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()

    for old in DEST.glob("*.json"):
        old.unlink()
    for schema in sorted(src.glob("*.json")):
        shutil.copy2(schema, DEST / schema.name)
        print(f"copied {schema.name}")
    (DEST / "VERSION").write_text(f"ManaraEngineering/manara-platform@{sha}\n")
    print(f"pinned to {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
