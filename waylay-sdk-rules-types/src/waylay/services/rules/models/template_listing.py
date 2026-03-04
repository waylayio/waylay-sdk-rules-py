"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.template_details import TemplateDetails
from ..models.template_entity_metadata import TemplateEntityMetadata

TemplateListing: TypeAlias = TemplateEntityMetadata | TemplateDetails
"""TemplateListing."""
