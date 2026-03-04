"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class ReactiveTaskSettingType(str, Enum):
    """ReactiveTaskSettingType."""

    REACTIVE = "reactive"

    def __str__(self) -> str:
        return str(self.value)
