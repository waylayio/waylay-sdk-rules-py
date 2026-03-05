"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.task_health import TaskHealth

    TaskHealthAdapter = TypeAdapter(TaskHealth)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

task_health_model_schema = json.loads(
    r"""{
  "title" : "TaskHealth",
  "required" : [ "errorsCount", "errorsRate" ],
  "type" : "object",
  "properties" : {
    "errorsCount" : {
      "title" : "errorsCount",
      "type" : "integer",
      "description" : "Number of errors during last 64 task invocations",
      "format" : "int32"
    },
    "errorsRate" : {
      "title" : "errorsRate",
      "type" : "number",
      "description" : "Error rate during last 64 task invocations. 0.0 means no errors, 1.0 means all errors",
      "format" : "float"
    }
  },
  "description" : "Health of the task"
}
""",
    object_hook=with_example_provider,
)
task_health_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_health_faker = JSF(task_health_model_schema, allow_none_optionals=1)


class TaskHealthStub:
    """TaskHealth unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_health_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TaskHealth":
        """Create TaskHealth stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(TaskHealthAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TaskHealthAdapter.validate_python(
            json, context={"skip_validation": True}
        )
