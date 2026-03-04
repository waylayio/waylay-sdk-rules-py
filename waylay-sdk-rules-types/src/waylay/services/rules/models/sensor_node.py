"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

import re
from typing import Annotated, Any

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.retry_config import RetryConfig


class SensorNode(WaylayBaseModel):
    """Representation of a sensor in a Rule Template.."""

    label: StrictStr = Field(description="Unique node label")
    name: StrictStr
    version: Annotated[str, Field(strict=True)]
    icon_url: StrictStr | None = Field(
        default=None,
        description="URL to an icon representing the sensor",
        alias="iconURL",
    )
    properties: dict[str, Any] | None = None
    resource: StrictStr | None = Field(
        default=None, description="Unique resource identifier"
    )
    sequence: StrictInt | None = 1
    position: Annotated[list[StrictInt], Field(min_length=2, max_length=2)] | None = None
    data_trigger: StrictBool | None = Field(default=True, alias="dataTrigger")
    tick_trigger: StrictBool | None = Field(default=True, alias="tickTrigger")
    eviction_time: Annotated[int, Field(strict=True, ge=0)] | None = Field(
        default=None, alias="evictionTime"
    )
    polling_period: Annotated[int, Field(strict=True, ge=1)] | None = Field(
        default=None, alias="pollingPeriod"
    )
    schedule: StrictStr | None = Field(
        default=None,
        description="Either a valid cron or RRule expression to set the sensor's own tick",
    )
    timeout: StrictStr | None = "PT50S"
    timeout_state: StrictStr | None = Field(default=None, alias="timeoutState")
    loop_def: Annotated[str, Field(strict=True)] | None = Field(
        default=None,
        description="A loop definition is a string that defines items over which node will be iterated multiple times. The string is an JSON array of JSON objects.During template execution the sensor node with such a defined loop definition will be invoked for every JSON Object in the JSON array. Parameter is optional. Node will be executed only once if loop definition is not defined.",
        alias="loopDef",
    )
    retry_config: RetryConfig | None = Field(default=None, alias="retryConfig")
    pause_execution: StrictBool | None = Field(default=False, alias="pauseExecution")
    pause_execution_timeout: StrictStr | None = Field(
        default="PT1H", alias="pauseExecutionTimeout"
    )
    description: StrictStr | None = None

    @field_validator("version")
    @classmethod
    def version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"\d+\.\d+\.\d+", value):
            raise ValueError(r"must validate the regular expression /\d+\.\d+\.\d+/")
        return value

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
