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
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class RetryConfig(WaylayBaseModel):
    """Configuration for retrying a template node. The node execution will be retried `maxRetries` times. The delay between retries will be exponentially increased starting from `minBackoff` to `maxBackoff`. If the node execution fails after `maxRetries` retries, the node state will be set to `errorState` if it that property is provided. Otherwise node execution will fail. Error state should be one of the possible states defined by the sensor node.."""

    max_retries: Annotated[int, Field(strict=True, ge=0)] = Field(alias="maxRetries")
    min_backoff: StrictStr = Field(alias="minBackoff")
    max_backoff: StrictStr = Field(alias="maxBackoff")
    error_state: StrictStr | None = Field(
        default=None,
        description="Optional sensor state which will be used to set the state of the node when the maxRetries is reached.",
        alias="errorState",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
