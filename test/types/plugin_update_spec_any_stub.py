"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.plugin_update_spec_any import PluginUpdateSpecAny

    PluginUpdateSpecAnyAdapter = TypeAdapter(PluginUpdateSpecAny)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

plugin_update_spec_any_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
plugin_update_spec_any_model_schema.update({"definitions": MODEL_DEFINITIONS})

plugin_update_spec_any_faker = JSF(
    plugin_update_spec_any_model_schema, allow_none_optionals=1
)


class PluginUpdateSpecAnyStub:
    """PluginUpdateSpecAny unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plugin_update_spec_any_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "PluginUpdateSpecAny":
        """Create PluginUpdateSpecAny stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PluginUpdateSpecAnyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PluginUpdateSpecAnyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
