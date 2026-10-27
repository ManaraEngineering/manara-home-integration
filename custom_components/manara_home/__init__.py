"""The Manara Home integration.

Skeleton only. Enrolment, device profiles, TV control, fleet health,
revocation, consent switches and publishing come in later phases;
see ManaraEngineering/manara-platform docs/adr/0004-site-integration.md.
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Manara Home from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
