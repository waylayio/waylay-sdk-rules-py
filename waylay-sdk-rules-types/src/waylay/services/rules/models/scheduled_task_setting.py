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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.scheduled_task_setting_all_of_type import ScheduledTaskSettingAllOfType


class ScheduledTaskSetting(WaylayBaseModel):
    """ScheduledTaskSetting."""

    type: ScheduledTaskSettingAllOfType
    time_zone: StrictStr | None = Field(
        default=None,
        description="Optional identifier of the time zone in which the schedule expression is to be interpreted",
        alias="timeZone",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )