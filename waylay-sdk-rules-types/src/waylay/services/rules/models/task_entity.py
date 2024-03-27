# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_status import TaskStatus


class TaskEntity(WaylayBaseModel):
    """TaskEntity."""

    id: StrictStr = Field(description="Unique task identifier", alias="ID")
    name: StrictStr
    status: TaskStatus
    user: StrictStr = Field(
        description="Creation user mail address or 'system' for system generated tasks"
    )
    create_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createTime",
    )
    template: StrictStr | None = Field(
        default=None, description="Unique template identifier"
    )
    network: Dict[str, Any] = Field(
        description="The graph, either from the template or from the task definition. Depending on the `format` query parameter either BN or simplified format"
    )
    resource_ids: List[StrictStr] | None = Field(
        default=None,
        description="List of resources that are used in the task",
        alias="resourceIds",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
