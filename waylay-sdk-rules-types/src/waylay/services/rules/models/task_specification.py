"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.task_from_template import TaskFromTemplate
from ..models.task_with_rule import TaskWithRule

TaskSpecification: TypeAlias = TaskFromTemplate | TaskWithRule
"""TaskSpecification."""
