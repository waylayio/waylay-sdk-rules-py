# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.operation_result_object_results import OperationResultObjectResults


class OperationResultObject(WaylayBaseModel):
    """Finished Batch Operation results."""

    finished_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="finishedTime",
    )
    results: OperationResultObjectResults

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )