"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.validation_issue import ValidationIssue


class ErrorWithDetailsResponse(WaylayBaseModel):
    """ErrorWithDetailsResponse."""

    status_code: StrictInt = Field(alias="statusCode")
    error: StrictStr
    code: StrictStr | None = Field(default=None, description="Optional error code")
    details: list[ValidationIssue] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
