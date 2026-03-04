"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.actuator_node import ActuatorNode
from ..models.relation_node import RelationNode
from ..models.sensor_node import SensorNode
from ..models.trigger_type import TriggerType


class SimplifiedGraph(WaylayBaseModel):
    """Graph in simplified format."""

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
