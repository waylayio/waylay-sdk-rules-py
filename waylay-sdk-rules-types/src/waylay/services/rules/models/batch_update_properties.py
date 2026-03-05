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

from ..models.batch_task_entity import BatchTaskEntity
from ..models.batch_task_query import BatchTaskQuery
from ..models.batch_update_properties_action import BatchUpdatePropertiesAction
from ..models.property_updates_spec import PropertyUpdatesSpec


class BatchUpdateProperties(WaylayBaseModel):
    """Update variables and/or tags of multiple tasks."""

    entity: BatchTaskEntity
    action: BatchUpdatePropertiesAction
    query: BatchTaskQuery
    action_parameters: PropertyUpdatesSpec | None = Field(alias="actionParameters")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
