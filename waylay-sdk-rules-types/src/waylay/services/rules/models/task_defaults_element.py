# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_scenario_type import TaskScenarioType


class TaskDefaultsElement(WaylayBaseModel):
    """default task settings that will be applied when creating a task from the template."""

    tags: Dict[str, Any] | None = Field(
        default=None,
        description="Key-value pairs on which you can set at task creation and later filter tasks",
    )
    type: TaskScenarioType | None = None
    reset_observations: StrictBool | None = Field(
        default=None, alias="resetObservations"
    )
    parallel: StrictBool | None = None
    gates_need_full_observation: StrictBool | None = Field(
        default=None, alias="gatesNeedFullObservation"
    )
    cron: StrictStr | None = Field(
        default=None,
        description="cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06)",
    )
    rrule: StrictStr | None = Field(
        default=None,
        description="RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3)",
    )
    time_zone: StrictStr | None = Field(
        default=None,
        description="Optional identifier of the time zone in which the schedule expression is to be interpreted",
        alias="timeZone",
    )
    frequency: StrictInt | None = Field(
        default=None, description="polling frequency in milliseconds"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
