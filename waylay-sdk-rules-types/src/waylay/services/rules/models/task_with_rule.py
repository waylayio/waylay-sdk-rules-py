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
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.actuator_node import ActuatorNode
from ..models.note_element import NoteElement
from ..models.relation_node import RelationNode
from ..models.sensor_node import SensorNode
from ..models.simplified_graph_triggers_inner import SimplifiedGraphTriggersInner
from ..models.task_with_rule_all_of_task import TaskWithRuleAllOfTask


class TaskWithRule(WaylayBaseModel):
    """TaskWithRule."""

    sensors: List[SensorNode] | None = Field(
        default=None, description="List of sensors with required properties"
    )
    actuators: List[ActuatorNode] | None = Field(
        default=None, description="List of actuators with required properties"
    )
    relations: List[RelationNode] | None = Field(
        default=None, description="List of relations (gates) between sensors"
    )
    triggers: List[SimplifiedGraphTriggersInner] | None = Field(
        default=None,
        description="List of conditions under which actuators/sensors get executed.",
    )
    notes: List[NoteElement] | None = None
    task: TaskWithRuleAllOfTask

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
