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

from ..models.batch_operation_results import BatchOperationResults


class OperationResultObject(WaylayBaseModel):
    """Finished Batch Operation results."""

    finished_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="finishedTime",
    )
    results: BatchOperationResults

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
