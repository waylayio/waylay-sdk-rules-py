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
    from waylay.services.rules.models.task_specification import TaskSpecification

    TaskSpecificationAdapter = TypeAdapter(TaskSpecification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_specification_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TaskFromTemplate"
  }, {
    "$ref" : "#/components/schemas/TaskWithRule"
  } ]
}
""",
    object_hook=with_example_provider,
)
task_specification_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_specification_faker = JSF(task_specification_model_schema, allow_none_optionals=1)


class TaskSpecificationStub:
    """TaskSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_specification_faker.generate()

    @classmethod
    def create_instance(cls) -> "TaskSpecification":
        """Create TaskSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TaskSpecificationAdapter.validate_python(cls.create_json())