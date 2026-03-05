"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class BatchOperationAction(str, Enum):
    """BatchOperationAction."""

    UPDATEPLUGINS = "updatePlugins"
    DELETE = "delete"
    START = "start"
    RESTART = "restart"
    STOP = "stop"
    RELOAD = "reload"
    UPDATEPROPERTIES = "updateProperties"

    def __str__(self) -> str:
        return str(self.value)
