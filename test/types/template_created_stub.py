"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.template_created import TemplateCreated

    TemplateCreatedAdapter = TypeAdapter(TemplateCreated)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

template_created_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/rules/v1/templates/internet.json"
    },
    "entity" : {
      "$ref" : "#/components/schemas/TemplateEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
template_created_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_created_faker = JSF(template_created_model_schema, allow_none_optionals=1)


class TemplateCreatedStub:
    """TemplateCreated unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_created_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TemplateCreated":
        """Create TemplateCreated stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateCreatedAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateCreatedAdapter.validate_python(
            json, context={"skip_validation": True}
        )
