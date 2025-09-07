"""The first_integration integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType

# For your initial PR, limit it to 1 platform.
_PLATFORMS: list[Platform] = [Platform.LIGHT]


class MyApi:
    """Placeholder for your integration's API client."""


type FirstIntegrationConfigEntry = ConfigEntry[MyApi]

DOMAIN = "first_integration"

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the first_integration integration from yaml (if supported)."""
    hass.states.async_set("first_integration.world", "Johan")
    return True
