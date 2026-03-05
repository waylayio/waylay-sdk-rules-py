"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.batch_operation_action import BatchOperationAction
from ..models.batch_task_entity import BatchTaskEntity


class BatchOperationSummary(WaylayBaseModel):
    """Summary of the batch operation."""

    entity: BatchTaskEntity
    action: BatchOperationAction
    description: StrictStr = Field(description="description of the operations")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
