"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class VariableType(str, Enum):
    """Value type for a template variable.."""

    STRING = "string"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    DOUBLE = "double"
    LONG = "long"
    FLOAT = "float"
    OBJECT = "object"

    def __str__(self) -> str:
        return str(self.value)
