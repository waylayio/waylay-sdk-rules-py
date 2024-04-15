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
    from waylay.services.rules.models.template_modification import TemplateModification

    TemplateModificationAdapter = TypeAdapter(TemplateModification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_modification_model_schema = json.loads(
    r"""{
  "required" : [ "operation", "updates" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "$ref" : "#/components/schemas/TemplateModification_operation"
    },
    "updates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/PluginUpdateSpec"
      }
    },
    "reloadTasks" : {
      "type" : "boolean",
      "description" : "Should all tasks created from the template be reloaded",
      "example" : true,
      "default" : false
    }
  }
}
""",
    object_hook=with_example_provider,
)
template_modification_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_modification_faker = JSF(
    template_modification_model_schema, allow_none_optionals=1
)


class TemplateModificationStub:
    """TemplateModification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_modification_faker.generate()

    @classmethod
    def create_instance(cls) -> "TemplateModification":
        """Create TemplateModification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TemplateModificationAdapter.validate_python(cls.create_json())