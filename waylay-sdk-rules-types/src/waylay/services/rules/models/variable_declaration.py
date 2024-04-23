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
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.variable_declaration_default_value import VariableDeclarationDefaultValue
from ..models.variable_format import VariableFormat
from ..models.variable_type import VariableType


class VariableDeclaration(WaylayBaseModel):
    """Variable declaration.."""

    name: StrictStr = Field(description="Variable Name")
    display_name: StrictStr | None = Field(
        default=None,
        description="Display name. Will default to the name if not specified",
        alias="displayName",
    )
    type: VariableType
    format: VariableFormat | None = None
    mandatory: StrictBool | None = Field(
        default=False,
        description="flag to indicate if value for variable is mandatory or not",
    )
    default_value: VariableDeclarationDefaultValue | None = Field(
        default=None, alias="defaultValue"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
