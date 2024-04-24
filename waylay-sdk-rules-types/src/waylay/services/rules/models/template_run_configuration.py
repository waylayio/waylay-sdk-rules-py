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
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class TemplateRunConfiguration(WaylayBaseModel):
    """Template run configurations."""

    execute_actuators: StrictBool | None = Field(
        default=False,
        description="Flag to trigger actual execution of actuators",
        alias="executeActuators",
    )
    resource: StrictStr | None = Field(
        default=None, description="Unique resource identifier"
    )
    reset_observations: StrictBool | None = Field(
        default=True,
        description="reset observations before injecting data",
        alias="resetObservations",
    )
    gates_need_full_observation: StrictBool | None = Field(
        default=False,
        description="Only evaluate gates when all inputs are observed",
        alias="gatesNeedFullObservation",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
