"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.plugin_update_spec_any import PluginUpdateSpecAny

PluginUpdateSpecFromVersion: TypeAlias = str | PluginUpdateSpecAny
"""plugin version selection to upgrade."""
