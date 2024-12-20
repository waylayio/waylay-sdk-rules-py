# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.task_runtime_information_all_of_health import (
    TaskRuntimeInformationAllOfHealth,
)
from ..models.task_scenario_type import TaskScenarioType
from ..models.task_status import TaskStatus


class TaskListingInner(WaylayBaseModel):
    """TaskListingInner."""

    id: StrictStr = Field(description="Unique task identifier", alias="ID")
    name: StrictStr
    status: TaskStatus
    user: StrictStr = Field(
        description="Creation user mail address or 'system' for system generated tasks"
    )
    create_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createTime",
    )
    template: StrictStr | None = Field(
        default=None, description="Unique template identifier"
    )
    network: Dict[str, Any] = Field(
        description="The graph, either from the template or from the task definition. Depending on the `format` query parameter either BN or simplified format"
    )
    resource_ids: List[StrictStr] | None = Field(
        default=None,
        description="List of resources that are used in the task",
        alias="resourceIds",
    )
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
    finished_time: StrictInt | None = Field(
        default=None,
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="finishedTime",
    )
    invocation_count: StrictInt | None = Field(
        default=None,
        description="Number of times the task has been invoked",
        alias="invocationCount",
    )
    raw_data: Dict[str, Any] | None = Field(
        default=None, description="rawData of the task", alias="rawData"
    )
    last_execution_time: StrictInt | None = Field(
        default=None,
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="lastExecutionTime",
    )
    health: TaskRuntimeInformationAllOfHealth | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
