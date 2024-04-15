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
    from waylay.services.rules.models.plugin_update_spec_from_version_one_of import (
        PluginUpdateSpecFromVersionOneOf,
    )

    PluginUpdateSpecFromVersionOneOfAdapter = TypeAdapter(
        PluginUpdateSpecFromVersionOneOf
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

plugin_update_spec_from_version_one_of_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
plugin_update_spec_from_version_one_of_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

plugin_update_spec_from_version_one_of_faker = JSF(
    plugin_update_spec_from_version_one_of_model_schema, allow_none_optionals=1
)


class PluginUpdateSpecFromVersionOneOfStub:
    """PluginUpdateSpecFromVersionOneOf unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plugin_update_spec_from_version_one_of_faker.generate()

    @classmethod
    def create_instance(cls) -> "PluginUpdateSpecFromVersionOneOf":
        """Create PluginUpdateSpecFromVersionOneOf stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return PluginUpdateSpecFromVersionOneOfAdapter.validate_python(
            cls.create_json()
        )