"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ActuatorExecutionResult(WaylayBaseModel):
    """ActuatorExecutionResult."""

    result: StrictBool | None = Field(
        default=None,
        description="flag indicating if the actuator was successfully executed",
    )
    error: StrictStr | None = Field(
        default=None, description="error message in case of failure"
    )
    raw_data: dict[str, Any] | None = Field(default=None, alias="rawData")
    log: list[dict[str, Any]] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
