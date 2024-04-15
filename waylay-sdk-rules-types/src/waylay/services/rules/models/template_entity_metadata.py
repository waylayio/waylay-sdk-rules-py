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

from ..models.note_element import NoteElement
from ..models.task_defaults_element import TaskDefaultsElement
from ..models.variable_declaration import VariableDeclaration


class TemplateEntityMetadata(WaylayBaseModel):
    """TemplateEntityMetadata."""

    name: StrictStr = Field(description="Unique template identifier")
    discovery_template: StrictBool = Field(
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
    user: StrictStr = Field(description="Creation user mail address")
    create_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="createTime",
    )
    last_update_time: StrictInt = Field(
        description="Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds.",
        alias="lastUpdateTime",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )