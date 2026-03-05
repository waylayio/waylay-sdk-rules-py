"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.scheduled_task_setting_scheduled import (
        ScheduledTaskSettingScheduled,
    )

    ScheduledTaskSettingScheduledAdapter = TypeAdapter(ScheduledTaskSettingScheduled)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

scheduled_task_setting_scheduled_model_schema = json.loads(
    r"""{
  "title" : "ScheduledTaskSettingScheduled",
  "type" : "string",
  "enum" : [ "scheduled" ]
}
""",
    object_hook=with_example_provider,
)
scheduled_task_setting_scheduled_model_schema.update({"definitions": MODEL_DEFINITIONS})

scheduled_task_setting_scheduled_faker = JSF(
    scheduled_task_setting_scheduled_model_schema, allow_none_optionals=1
)


class ScheduledTaskSettingScheduledStub:
    """ScheduledTaskSettingScheduled unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return scheduled_task_setting_scheduled_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ScheduledTaskSettingScheduled":
        """Create ScheduledTaskSettingScheduled stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ScheduledTaskSettingScheduledAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ScheduledTaskSettingScheduledAdapter.validate_python(
            json, context={"skip_validation": True}
        )
