# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_task_command_all_of_action import BatchTaskCommandAllOfAction
from ..models.batch_task_entity import BatchTaskEntity
from ..models.batch_task_query import BatchTaskQuery


class BatchTaskCommand(WaylayBaseModel):
    """Execute command on multiple task."""

    entity: BatchTaskEntity
    action: BatchTaskCommandAllOfAction
    query: BatchTaskQuery

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
