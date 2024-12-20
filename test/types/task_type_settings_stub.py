# coding: utf-8
"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.task_type_settings import TaskTypeSettings

    TaskTypeSettingsAdapter = TypeAdapter(TaskTypeSettings)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_type_settings_model_schema = json.loads(
    r"""{
  "type" : "object",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ScheduledTaskSetting"
  }, {
    "$ref" : "#/components/schemas/PeriodicTaskSetting"
  }, {
    "$ref" : "#/components/schemas/OneTimeTaskSetting"
  }, {
    "$ref" : "#/components/schemas/ReactiveTaskSetting"
  } ]
}
""",
    object_hook=with_example_provider,
)
task_type_settings_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_type_settings_faker = JSF(task_type_settings_model_schema, allow_none_optionals=1)


class TaskTypeSettingsStub:
    """TaskTypeSettings unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_type_settings_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TaskTypeSettings":
        """Create TaskTypeSettings stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TaskTypeSettingsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TaskTypeSettingsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
