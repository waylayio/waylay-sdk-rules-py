"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.plugin_update_spec import PluginUpdateSpec
from ..models.template_modification_operation import TemplateModificationOperation


class TemplateModification(WaylayBaseModel):
    """TemplateModification."""

    operation: TemplateModificationOperation
    updates: list[PluginUpdateSpec]
    reload_tasks: StrictBool | None = Field(
        default=False,
        description="Should all tasks created from the template be reloaded",
        alias="reloadTasks",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
