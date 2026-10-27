"""Config flow for Manara Home."""

from __future__ import annotations

from typing import Any

import probatio
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN, TITLE


class ManaraHomeConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Manara Home. One instance per site."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Show an empty form, then create the entry."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=probatio.Schema({}))

        return self.async_create_entry(title=TITLE, data={})
