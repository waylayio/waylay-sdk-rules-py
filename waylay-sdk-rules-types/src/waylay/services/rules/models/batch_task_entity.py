"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class BatchTaskEntity(str, Enum):
    """BatchTaskEntity."""

    TASK = "task"

    def __str__(self) -> str:
        return str(self.value)
