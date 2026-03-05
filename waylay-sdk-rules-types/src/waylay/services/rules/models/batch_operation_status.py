"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_operation import BatchOperation
from ..models.batch_operation_result import BatchOperationResult

BatchOperationStatus: TypeAlias = BatchOperationResult | BatchOperation
"""BatchOperationStatus."""
