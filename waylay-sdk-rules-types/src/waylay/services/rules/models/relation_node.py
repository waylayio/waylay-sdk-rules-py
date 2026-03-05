"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.gate_type import GateType


class RelationNode(WaylayBaseModel):
    """Representation of a gate in a Rule Template.."""

    label: StrictStr = Field(description="Unique node label")
    type: GateType
    parent_labels: list[StrictStr] = Field(alias="parentLabels")
    combinations: list[list[StrictStr]]
    position: Annotated[list[StrictInt], Field(min_length=2, max_length=2)] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
