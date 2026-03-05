"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.execution_trigger import ExecutionTrigger
from ..models.state_change_trigger import StateChangeTrigger
from ..models.states_trigger import StatesTrigger

TriggerType: TypeAlias = StateChangeTrigger | StatesTrigger | ExecutionTrigger
"""TriggerType."""
