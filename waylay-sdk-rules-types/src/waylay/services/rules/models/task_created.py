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

from ..models.validation_issue import ValidationIssue


class TaskCreated(WaylayBaseModel):
    """TaskCreated."""

    id: StrictStr = Field(description="Unique task identifier", alias="ID")
    warnings: list[ValidationIssue] | None = Field(
        default=None,
        description="List of task warning issues. Will only be there if query parameter `returnWarnings` was set to `true`",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
