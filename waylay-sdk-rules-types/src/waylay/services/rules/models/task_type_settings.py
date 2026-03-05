"""Waylay rules engine models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.one_time_task_setting import OneTimeTaskSetting
from ..models.periodic_task_setting import PeriodicTaskSetting
from ..models.reactive_task_setting import ReactiveTaskSetting
from ..models.scheduled_task_setting import ScheduledTaskSetting

TaskTypeSettings: TypeAlias = ScheduledTaskSetting | PeriodicTaskSetting | OneTimeTaskSetting | ReactiveTaskSetting
"""TaskTypeSettings."""
