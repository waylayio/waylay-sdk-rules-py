# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_scenario_type import TaskScenarioType
from ..models.task_status import TaskStatus


class BatchQuery(WaylayBaseModel):
    """BatchQuery."""

    name: StrictStr | None = None
    resource: StrictStr | None = Field(
        default=None, description="Unique resource identifier"
    )
    type: TaskScenarioType | None = None
    status: TaskStatus | None = None
    template: StrictStr | None = Field(
        default=None, description="Unique template identifier"
    )
    plugin: StrictStr | None = Field(
        default=None,
        description="either name of a plugin (e.g. `mySensor`), or full version specification of the plug (e.g `mySensor:1.0.3`)",
    )
    user: StrictStr | None = Field(
        default=None,
        description="Creation user mail address or 'system' for system generated tasks",
    )
    finished_before: StrictInt | None = Field(
        default=None,
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="finishedBefore",
    )
    created_after: StrictInt | None = Field(
        default=None,
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createdAfter",
    )
    created_before: StrictInt | None = Field(
        default=None,
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createdBefore",
    )
    tags: Dict[str, Any] | None = Field(
        default=None,
        description="Key-value pairs on which you can set at task creation and later filter tasks",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
