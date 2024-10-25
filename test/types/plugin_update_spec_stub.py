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
    from waylay.services.rules.models.plugin_update_spec import PluginUpdateSpec

    PluginUpdateSpecAdapter = TypeAdapter(PluginUpdateSpec)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

plugin_update_spec_model_schema = json.loads(
    r"""{
  "required" : [ "fromVersion", "name", "toVersion" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Name of the plugin to update",
      "example" : "mySensor"
    },
    "fromVersion" : {
      "$ref" : "#/components/schemas/PluginUpdateSpec_fromVersion"
    },
    "toVersion" : {
      "description" : "Plugin version to upgrade to",
      "allOf" : [ {
        "$ref" : "#/components/schemas/Version"
      } ]
    }
  }
}
""",
    object_hook=with_example_provider,
)
plugin_update_spec_model_schema.update({"definitions": MODEL_DEFINITIONS})

plugin_update_spec_faker = JSF(plugin_update_spec_model_schema, allow_none_optionals=1)


class PluginUpdateSpecStub:
    """PluginUpdateSpec unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return plugin_update_spec_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "PluginUpdateSpec":
        """Create PluginUpdateSpec stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                PluginUpdateSpecAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return PluginUpdateSpecAdapter.validate_python(
            json, context={"skip_validation": True}
        )
