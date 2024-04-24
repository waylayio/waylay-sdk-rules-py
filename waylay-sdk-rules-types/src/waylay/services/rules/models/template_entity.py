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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.actuator_node import ActuatorNode
from ..models.note_element import NoteElement
from ..models.relation_node import RelationNode
from ..models.sensor_node import SensorNode
from ..models.simplified_graph_triggers_inner import SimplifiedGraphTriggersInner
from ..models.task_defaults_element import TaskDefaultsElement
from ..models.variable_declaration import VariableDeclaration


class TemplateEntity(WaylayBaseModel):
    """TemplateEntity."""

    name: StrictStr = Field(description="Unique template identifier")
    discovery_template: StrictBool | None = Field(
        default=None,
        description="flag to indicate if the template is the discovery template",
        alias="discoveryTemplate",
    )
    tags: Dict[str, Any] | None = Field(
        default=None,
        description="Key-value pairs on which you can filter to finding templates back",
    )
    variables: List[VariableDeclaration] | None = Field(
        default=None, description="Variable declarations"
    )
    task_defaults: TaskDefaultsElement | None = Field(
        default=None, alias="taskDefaults"
    )
    notes: List[NoteElement] | None = Field(
        default=None, description="List of notes as explanation for users"
    )
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

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
