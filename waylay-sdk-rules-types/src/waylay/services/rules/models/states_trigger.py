# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
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
    states_trigger: List[StrictStr] = Field(
        description="array of states of source node under which to fire",
        alias="statesTrigger",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )