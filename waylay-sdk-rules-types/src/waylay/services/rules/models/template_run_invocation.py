"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.log_entry import LogEntry
from ..models.template_run_actuator_result import TemplateRunActuatorResult
from ..models.template_run_sensor_result import TemplateRunSensorResult


class TemplateRunInvocation(WaylayBaseModel):
    """TemplateRunInvocation."""

    task_id: StrictStr = Field(description="Unique task identifier", alias="taskId")
    invocation_id: StrictStr = Field(
        description="Unique invocation identifier", alias="invocationId"
    )
    sensors: dict[str, TemplateRunSensorResult] = Field(
        description="The execution result for each of the sensors of the template"
    )
    actuators: dict[str, TemplateRunActuatorResult] = Field(
        description="The execution result for each of the actuators of the template"
    )
    log: list[LogEntry]
    task_output: dict[str, Any] | None = Field(
        default=None,
        description="The task output for the invocation. Only there if template uses TaskOutput sensor",
        alias="taskOutput",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
