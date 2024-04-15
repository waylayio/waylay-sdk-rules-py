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
    from waylay.services.rules.models.batch_task_command import BatchTaskCommand

    BatchTaskCommandAdapter = TypeAdapter(BatchTaskCommand)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_task_command_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Execute command on multiple task",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchTask"
  }, {
    "required" : [ "action", "entity", "query" ],
    "properties" : {
      "action" : {
        "$ref" : "#/components/schemas/BatchTaskCommand_allOf_action"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
batch_task_command_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_task_command_faker = JSF(batch_task_command_model_schema, allow_none_optionals=1)


class BatchTaskCommandStub:
    """BatchTaskCommand unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_task_command_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchTaskCommand":
        """Create BatchTaskCommand stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchTaskCommandAdapter.validate_python(cls.create_json())