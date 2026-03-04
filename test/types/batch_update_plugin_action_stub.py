"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.batch_update_plugin_action import (
        BatchUpdatePluginAction,
    )

    BatchUpdatePluginActionAdapter = TypeAdapter(BatchUpdatePluginAction)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

batch_update_plugin_action_model_schema = json.loads(
    r"""{
  "title" : "BatchUpdatePluginAction",
  "type" : "string",
  "enum" : [ "updatePlugins" ]
}
""",
    object_hook=with_example_provider,
)
batch_update_plugin_action_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_update_plugin_action_faker = JSF(
    batch_update_plugin_action_model_schema, allow_none_optionals=1
)


class BatchUpdatePluginActionStub:
    """BatchUpdatePluginAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_update_plugin_action_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchUpdatePluginAction":
        """Create BatchUpdatePluginAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchUpdatePluginActionAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchUpdatePluginActionAdapter.validate_python(
            json, context={"skip_validation": True}
        )
