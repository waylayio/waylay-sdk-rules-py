"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.batch_update_properties_action import (
        BatchUpdatePropertiesAction,
    )

    BatchUpdatePropertiesActionAdapter = TypeAdapter(BatchUpdatePropertiesAction)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_update_properties_action_model_schema = json.loads(
    r"""{
  "title" : "BatchUpdatePropertiesAction",
  "type" : "string",
  "enum" : [ "updateProperties" ]
}
""",
    object_hook=with_example_provider,
)
batch_update_properties_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_update_properties_action_faker = JSF(
    batch_update_properties_action_model_schema, allow_none_optionals=1
)


class BatchUpdatePropertiesActionStub:
    """BatchUpdatePropertiesAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_update_properties_action_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchUpdatePropertiesAction":
        """Create BatchUpdatePropertiesAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchUpdatePropertiesActionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchUpdatePropertiesActionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
