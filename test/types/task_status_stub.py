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
    from waylay.services.rules.models.task_status import TaskStatus

    TaskStatusAdapter = TypeAdapter(TaskStatus)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_status_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Status of a task",
  "enum" : [ "running", "stopped", "failed" ]
}
""",
    object_hook=with_example_provider,
)
task_status_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_status_faker = JSF(task_status_model_schema, allow_none_optionals=1)


class TaskStatusStub:
    """TaskStatus unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_status_faker.generate()

    @classmethod
    def create_instance(cls) -> "TaskStatus":
        """Create TaskStatus stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TaskStatusAdapter.validate_python(cls.create_json())