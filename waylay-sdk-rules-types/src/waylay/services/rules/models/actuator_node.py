"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

import re
from typing import Annotated, Any

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
    field_validator,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ActuatorNode(WaylayBaseModel):
    """Representation of an actuator in a Rule Template.."""

    label: StrictStr = Field(description="Unique node label")
    name: StrictStr
    version: Annotated[str, Field(strict=True)]
    properties: dict[str, Any] | None = None
    sequence: StrictInt | None = None
    position: Annotated[list[StrictInt], Field(min_length=2, max_length=2)] | None = None
    timeout: StrictStr | None = "PT50S"
    description: StrictStr | None = None

    @field_validator("version")
    @classmethod
    def version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"\d+\.\d+\.\d+", value):
            raise ValueError(r"must validate the regular expression /\d+\.\d+\.\d+/")
        return value

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
