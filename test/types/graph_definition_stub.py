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
    from waylay.services.rules.models.graph_definition import GraphDefinition

    GraphDefinitionAdapter = TypeAdapter(GraphDefinition)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

graph_definition_model_schema = json.loads(
    r"""{
  "title" : "GraphDefinition",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  }, {
    "$ref" : "#/components/schemas/BayesianGraph"
  } ]
}
""",
    object_hook=with_example_provider,
)
graph_definition_model_schema.update({"definitions": MODEL_DEFINITIONS})

graph_definition_faker = JSF(graph_definition_model_schema, allow_none_optionals=1)


class GraphDefinitionStub:
    """GraphDefinition unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return graph_definition_faker.generate()

    @classmethod
    def create_instance(cls) -> "GraphDefinition":
        """Create GraphDefinition stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GraphDefinitionAdapter.validate_python(cls.create_json())