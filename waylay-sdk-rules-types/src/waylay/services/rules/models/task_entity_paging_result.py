"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_with_runtime_info import TaskWithRuntimeInfo


class TaskEntityPagingResult(WaylayBaseModel):
    """TaskEntityPagingResult."""

    skip: StrictInt = Field(
        description="Number of items skipped before this page of results."
    )
    limit: StrictInt = Field(description="Size of one page of results.")
    total: StrictInt = Field(
        description="Total number of items matching the query of which this is one page of results."
    )
    values: list[TaskWithRuntimeInfo] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
