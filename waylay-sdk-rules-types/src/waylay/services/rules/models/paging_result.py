# coding: utf-8
"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class PagingResult(WaylayBaseModel):
    """PagingResult."""

    skip: StrictInt = Field(
        description="Number of items skipped before this page of results."
    )
    limit: StrictInt = Field(description="Size of one page of results.")
    total: StrictInt = Field(
        description="Total number of items matching the query of which this is one page of results."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
