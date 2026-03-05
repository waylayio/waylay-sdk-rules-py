"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.batch_operation_action import BatchOperationAction

    BatchOperationActionAdapter = TypeAdapter(BatchOperationAction)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_operation_action_model_schema = json.loads(
    r"""{
  "title" : "BatchOperationAction",
  "type" : "string",
  "example" : "delete",
  "enum" : [ "updatePlugins", "delete", "start", "restart", "stop", "reload", "updateProperties" ]
}
""",
    object_hook=with_example_provider,
)
batch_operation_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_action_faker = JSF(
    batch_operation_action_model_schema, allow_none_optionals=1
)


class BatchOperationActionStub:
    """BatchOperationAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_action_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchOperationAction":
        """Create BatchOperationAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchOperationActionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchOperationActionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
