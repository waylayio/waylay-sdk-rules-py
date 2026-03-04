"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class StatesTrigger(WaylayBaseModel):
    """A trigger that is conditional on the states of the source.."""

    source_label: StrictStr = Field(
        description="Unique node label", alias="sourceLabel"
    )
    destination_label: StrictStr = Field(
        description="Unique node label", alias="destinationLabel"
    )
    invocation_policy: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=None, alias="invocationPolicy"
    )
    states_trigger: list[StrictStr] = Field(
        description="array of states of source node under which to fire",
        alias="statesTrigger",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
