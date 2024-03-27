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
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_data_injection import ResourceDataInjection
from ..models.template_run_configuration import TemplateRunConfiguration


class TemplateRunSpecification(WaylayBaseModel):
    """TemplateRunSpecification."""

    data: List[List[ResourceDataInjection]] | None = Field(
        default=None,
        description="The full dataset to process. If specified, template will be run as reactive template",
    )
    conf: TemplateRunConfiguration | None = None
    variables: Dict[str, Any] | None = Field(
        default=None,
        description="The values for the variables declared in the template",
    )
    resource_meta_data: Dict[str, Dict[str, Any]] | None = Field(
        default=None,
        description="Metadata for any of the resources used in the template.  The current metadata for all resources used in the template is fetched at the start of the template run. This provided metadata is used to overwrite this current metadata",
        alias="resourceMetaData",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
