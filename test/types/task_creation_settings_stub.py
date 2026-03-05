"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.task_creation_settings import TaskCreationSettings

    TaskCreationSettingsAdapter = TypeAdapter(TaskCreationSettings)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

task_creation_settings_model_schema = json.loads(
    r"""{
  "title" : "TaskCreationSettings",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TaskSettings"
  }, {
    "required" : [ "name" ],
    "type" : "object",
    "properties" : {
      "start" : {
        "title" : "boolean to indicate whether task must be started after creation",
        "type" : "boolean",
        "default" : true
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
task_creation_settings_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_creation_settings_faker = JSF(
    task_creation_settings_model_schema, allow_none_optionals=1
)


class TaskCreationSettingsStub:
    """TaskCreationSettings unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_creation_settings_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TaskCreationSettings":
        """Create TaskCreationSettings stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TaskCreationSettingsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TaskCreationSettingsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
