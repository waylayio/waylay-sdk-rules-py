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
    from waylay.services.rules.models.template_run_with_graph_specification import (
        TemplateRunWithGraphSpecification,
    )

    TemplateRunWithGraphSpecificationAdapter = TypeAdapter(
        TemplateRunWithGraphSpecification
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_run_with_graph_specification_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateRunSpecification"
  }, {
    "required" : [ "graph" ],
    "type" : "object",
    "properties" : {
      "graph" : {
        "$ref" : "#/components/schemas/GraphDefinition"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
template_run_with_graph_specification_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

template_run_with_graph_specification_faker = JSF(
    template_run_with_graph_specification_model_schema, allow_none_optionals=1
)


class TemplateRunWithGraphSpecificationStub:
    """TemplateRunWithGraphSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_run_with_graph_specification_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TemplateRunWithGraphSpecification":
        """Create TemplateRunWithGraphSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateRunWithGraphSpecificationAdapter.json_schema(),
                allow_none_optionals=1,
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateRunWithGraphSpecificationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
