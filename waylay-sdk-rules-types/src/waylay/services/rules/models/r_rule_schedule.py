"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class RRuleSchedule(WaylayBaseModel):
    """RRuleSchedule."""

    rrule: StrictStr = Field(
        description="RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3)"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
