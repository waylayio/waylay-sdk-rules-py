"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class TaskStatus(str, Enum):
    """Status of a task."""

    RUNNING = "running"
    PENDING = "pending"
    STOPPED = "stopped"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
