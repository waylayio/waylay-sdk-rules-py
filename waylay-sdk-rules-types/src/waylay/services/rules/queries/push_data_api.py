# coding: utf-8
"""Waylay rules engine query parameters.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


def _push_query_alias_for(field_name: str) -> str:
    return field_name


class PushQuery(WaylayBaseModel):
    """Model for `push` query parameters."""

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_push_query_alias_for,
        populate_by_name=True,
    )
