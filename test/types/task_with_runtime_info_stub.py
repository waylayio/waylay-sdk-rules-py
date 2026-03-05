"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.task_with_runtime_info import TaskWithRuntimeInfo

    TaskWithRuntimeInfoAdapter = TypeAdapter(TaskWithRuntimeInfo)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

task_with_runtime_info_model_schema = json.loads(
    r"""{
  "title" : "TaskWithRuntimeInfo",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TaskEntity"
  }, {
    "$ref" : "#/components/schemas/TaskRuntimeInformation"
  } ]
}
""",
    object_hook=with_example_provider,
)
task_with_runtime_info_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_with_runtime_info_faker = JSF(
    task_with_runtime_info_model_schema, allow_none_optionals=1
)


class TaskWithRuntimeInfoStub:
    """TaskWithRuntimeInfo unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_with_runtime_info_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TaskWithRuntimeInfo":
        """Create TaskWithRuntimeInfo stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TaskWithRuntimeInfoAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TaskWithRuntimeInfoAdapter.validate_python(
            json, context={"skip_validation": True}
        )
