"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_task_command import BatchTaskCommand
from ..models.batch_update_plugin import BatchUpdatePlugin
from ..models.batch_update_properties import BatchUpdateProperties

BatchTaskSpec: TypeAlias = BatchUpdatePlugin | BatchTaskCommand | BatchUpdateProperties
"""BatchTaskSpec."""
