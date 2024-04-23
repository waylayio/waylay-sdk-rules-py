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
    from waylay.services.rules.models.template_details import TemplateDetails

    TemplateDetailsAdapter = TypeAdapter(TemplateDetails)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_details_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityMetadata"
  }, {
    "$ref" : "#/components/schemas/GraphDefinition"
  } ]
}
""",
    object_hook=with_example_provider,
)
template_details_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_details_faker = JSF(template_details_model_schema, allow_none_optionals=1)


class TemplateDetailsStub:
    """TemplateDetails unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_details_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TemplateDetails":
        """Create TemplateDetails stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateDetailsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateDetailsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
