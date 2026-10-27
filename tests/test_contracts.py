"""The vendored contract schemas ship with the integration and are pinned."""

import json
from pathlib import Path

CONTRACTS = (
    Path(__file__).resolve().parent.parent / "custom_components/manara_home/contracts"
)
EXPECTED = {
    "device-profile.v1.json",
    "enrolment-qr.v1.json",
    "health.v1.json",
    "inventory.v1.json",
}


def test_schemas_present_and_parse() -> None:
    names = {p.name for p in CONTRACTS.glob("*.json")}
    assert names == EXPECTED
    for name in names:
        schema = json.loads((CONTRACTS / name).read_text(encoding="utf-8"))
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"


def test_pinned_to_platform_commit() -> None:
    version = (CONTRACTS / "VERSION").read_text().strip()
    assert version.startswith("ManaraEngineering/manara-platform@")
    assert len(version.rsplit("@", 1)[1]) == 40
