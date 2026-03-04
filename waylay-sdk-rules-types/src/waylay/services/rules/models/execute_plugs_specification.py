"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ExecutePlugsSpecification(WaylayBaseModel):
    """ExecutePlugsSpecification."""

    properties: dict[str, Any] | None = None
    resource: StrictStr | None = Field(
        default=None, description="Unique resource identifier"
    )
    stream_data: dict[str, Any] | None = Field(default=None, alias="streamData")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
