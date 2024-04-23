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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class UpgradePluginsTemplates200Response(WaylayBaseModel):
    """UpgradePluginsTemplates200Response."""

    successful: List[StrictStr] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
