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
    from waylay.services.rules.models.variable_declaration import VariableDeclaration

    VariableDeclarationAdapter = TypeAdapter(VariableDeclaration)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

variable_declaration_model_schema = json.loads(
    r"""{
  "title" : "VariableDeclaration",
  "required" : [ "name", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Variable Name"
    },
    "displayName" : {
      "type" : "string",
      "description" : "Display name. Will default to the name if not specified"
    },
    "type" : {
      "$ref" : "#/components/schemas/VariableType"
    },
    "format" : {
      "$ref" : "#/components/schemas/VariableFormat"
    },
    "mandatory" : {
      "type" : "boolean",
      "description" : "flag to indicate if value for variable is mandatory or not",
      "default" : false
    },
    "description" : {
      "type" : "string",
      "description" : "Description of the variable"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/VariableDeclaration_defaultValue"
    }
  },
  "description" : "Variable declaration.",
  "example" : {
    "name" : "city",
    "displayName" : "City",
    "type" : "string",
    "mandatory" : true
  }
}
""",
    object_hook=with_example_provider,
)
variable_declaration_model_schema.update({"definitions": MODEL_DEFINITIONS})

variable_declaration_faker = JSF(
    variable_declaration_model_schema, allow_none_optionals=1
)


class VariableDeclarationStub:
    """VariableDeclaration unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return variable_declaration_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "VariableDeclaration":
        """Create VariableDeclaration stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                VariableDeclarationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return VariableDeclarationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
