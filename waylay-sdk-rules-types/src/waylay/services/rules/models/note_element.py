"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class NoteElement(WaylayBaseModel):
    """Representation of a note in a Rule Template.."""

    position: Annotated[list[StrictInt], Field(min_length=2, max_length=2)]
    text: StrictStr

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
