"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.reactive_task_setting_type import ReactiveTaskSettingType


class TaskSettings(WaylayBaseModel):
    """TaskSettings."""

    name: StrictStr | None = None
    resource: StrictStr | None = Field(
        default=None, description="Unique resource identifier"
    )
    reset_observations: StrictBool | None = Field(
        default=True, alias="resetObservations"
    )
    parallel: StrictBool | None = True
    gates_need_full_observation: StrictBool | None = Field(
        default=False, alias="gatesNeedFullObservation"
    )
    protected: StrictBool | None = False
    tags: dict[str, Any] | None = Field(
        default=None,
        description="Key-value pairs on which you can set at task creation and later filter tasks",
    )
    variables: dict[str, Any] | None = Field(
        default=None,
        description="set of variables which will be used when starting a task and will automatically be injected in the template before starting a task.",
    )
    type: ReactiveTaskSettingType
    time_zone: StrictStr | None = Field(
        default=None,
        description="Optional identifier of the time zone in which the schedule expression is to be interpreted",
        alias="timeZone",
    )
    rrule: StrictStr = Field(
        description="RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3)"
    )
    cron: StrictStr = Field(
        description="cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06)"
    )
    frequency: StrictInt = Field(description="polling frequency in milliseconds")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
