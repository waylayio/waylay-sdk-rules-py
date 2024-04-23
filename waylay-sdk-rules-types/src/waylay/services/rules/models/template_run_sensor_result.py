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
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class TemplateRunSensorResult(WaylayBaseModel):
    """TemplateRunSensorResult."""

    result: StrictBool | None = Field(
        default=None,
        description="flag indicating if the sensor was successfully executed",
    )
    state: StrictStr | None = Field(
        default=None, description="observedState field returned by the sensor execution"
    )
    error: StrictStr | None = Field(
        default=None, description="error message in case of failure"
    )
    raw_data: Dict[str, Any] | None = Field(
        default=None,
        description="the rawData returned by the sensor execution",
        alias="rawData",
    )
    log: List[Dict[str, Any]] | None = None
    executed: StrictBool = Field(
        description="flag indicating if the sensor was executed"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
