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

from ..models.actuator_node import ActuatorNode
from ..models.note_element import NoteElement
from ..models.relation_node import RelationNode
from ..models.sensor_node import SensorNode
from ..models.task_defaults_element import TaskDefaultsElement
from ..models.trigger_type import TriggerType
from ..models.variable_declaration import VariableDeclaration


class TemplateUpdated(WaylayBaseModel):
    """TemplateUpdated."""

    name: StrictStr = Field(description="Unique template identifier")
    discovery_template: StrictBool = Field(
        description="flag to indicate if the template is the discovery template",
        alias="discoveryTemplate",
    )
    tags: dict[str, Any] | None = Field(
        default=None,
        description="Key-value pairs on which you can filter to finding templates back",
    )
    variables: list[VariableDeclaration] | None = Field(
        default=None, description="Variable declarations"
    )
    task_defaults: TaskDefaultsElement | None = Field(
        default=None, alias="taskDefaults"
    )
    description: StrictStr | None = Field(
        default=None, description="Description of the template"
    )
    icon_url: StrictStr | None = Field(
        default=None,
        description="URL to an icon representing the template",
        alias="iconURL",
    )
    protected: StrictBool | None = Field(
        default=False,
        description="Flag to indicate if the template is protected. Can be set only by user with protected permission. Modification or deletion of template is not allowed to user without protected permission.",
    )
    notes: list[NoteElement] | None = Field(
        default=None, description="List of notes as explanation for users"
    )
    user: StrictStr = Field(description="Creation user mail address")
    create_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createTime",
    )
    last_update_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="lastUpdateTime",
    )
    sensors: list[SensorNode] | None = Field(
        default=None, description="List of sensors with required properties"
    )
    actuators: list[ActuatorNode] | None = Field(
        default=None, description="List of actuators with required properties"
    )
    relations: list[RelationNode] | None = Field(
        default=None, description="List of relations (gates) between sensors"
    )
    triggers: list[TriggerType] | None = Field(
        default=None,
        description="List of conditions under which actuators/sensors get executed.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
