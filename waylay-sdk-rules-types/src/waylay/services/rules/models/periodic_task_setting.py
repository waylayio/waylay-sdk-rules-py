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
    StrictInt,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.periodic_task_setting_type import PeriodicTaskSettingType


class PeriodicTaskSetting(WaylayBaseModel):
    """PeriodicTaskSetting."""

    type: PeriodicTaskSettingType
    frequency: StrictInt = Field(description="polling frequency in milliseconds")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
