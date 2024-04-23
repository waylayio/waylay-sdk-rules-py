# coding: utf-8
"""Waylay rules engine query parameters.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.run_template_log_level_parameter import RunTemplateLogLevelParameter


def _run_graph_query_alias_for(field_name: str) -> str:
    if field_name == "log_level":
        return "logLevel"
    if field_name == "target_node":
        return "targetNode"
    return field_name


class RunGraphQuery(WaylayBaseModel):
    """Model for `run_graph` query parameters."""

    log_level: Annotated[
        RunTemplateLogLevelParameter | None,
        Field(
            description="sets the log level for filtering out logs to requested log level or higher from the template run output. Value `NONE` will disable all logs. If not specified all logs will be returned."
        ),
    ] = None
    target_node: Annotated[
        List[StrictStr] | None,
        Field(
            description="The sensors and actuators part of response will contain only elements related to the asked node of the graph. The returned logs also will be filtered and contain only logs related to the asked node(s)."
        ),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_run_graph_query_alias_for,
        populate_by_name=True,
    )


def _run_query_alias_for(field_name: str) -> str:
    if field_name == "log_level":
        return "logLevel"
    if field_name == "target_node":
        return "targetNode"
    return field_name


class RunQuery(WaylayBaseModel):
    """Model for `run` query parameters."""

    log_level: Annotated[
        RunTemplateLogLevelParameter | None,
        Field(
            description="sets the log level for filtering out logs to requested log level or higher from the template run output. Value `NONE` will disable all logs. If not specified all logs will be returned."
        ),
    ] = None
    target_node: Annotated[
        List[StrictStr] | None,
        Field(
            description="The sensors and actuators part of response will contain only elements related to the asked node of the graph. The returned logs also will be filtered and contain only logs related to the asked node(s)."
        ),
    ] = None

    model_config = ConfigDict(
        protected_namespaces=(),
        extra="allow",
        alias_generator=_run_query_alias_for,
        populate_by_name=True,
    )
