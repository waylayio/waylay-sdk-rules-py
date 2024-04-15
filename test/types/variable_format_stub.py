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
    from waylay.services.rules.models.variable_format import VariableFormat

    VariableFormatAdapter = TypeAdapter(VariableFormat)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

variable_format_model_schema = json.loads(
    r"""{
  "title" : "VariableFormat",
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Type",
      "type" : "string",
      "example" : "resource"
    },
    "values" : {
      "title" : "Possible values (enum declaration)",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Possible_values__enum_declaration__inner"
      }
    }
  },
  "description" : "Format for a variable definition."
}
""",
    object_hook=with_example_provider,
)
variable_format_model_schema.update({"definitions": MODEL_DEFINITIONS})

variable_format_faker = JSF(variable_format_model_schema, allow_none_optionals=1)


class VariableFormatStub:
    """VariableFormat unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return variable_format_faker.generate()

    @classmethod
    def create_instance(cls) -> "VariableFormat":
        """Create VariableFormat stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return VariableFormatAdapter.validate_python(cls.create_json())