# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Dict, List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.logs_inner import LogsInner
from ..models.template_run_actuator_result import TemplateRunActuatorResult
from ..models.template_run_sensor_result import TemplateRunSensorResult


class TemplateRunInvocation(WaylayBaseModel):
    """TemplateRunInvocation."""

    task_id: StrictStr = Field(description="Unique task identifier", alias="taskId")
    invocation_id: StrictStr = Field(
        description="Unique invocation identifier", alias="invocationId"
    )
    sensors: Dict[str, TemplateRunSensorResult] = Field(
        description="The execution result for each of the sensors of the template"
    )
    actuators: Dict[str, TemplateRunActuatorResult] = Field(
        description="The execution result for each of the actuators of the template"
    )
    log: List[LogsInner]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )