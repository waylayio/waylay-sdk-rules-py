# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import datetime

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.version_response_status import VersionResponseStatus


class VersionResponse(WaylayBaseModel):
    """VersionResponse."""

    version: StrictStr
    name: StrictStr
    start_time: datetime | None = Field(default=None, alias="startTime")
    uptime: StrictInt | None = None
    status: VersionResponseStatus

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
