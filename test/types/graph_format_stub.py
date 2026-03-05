"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.graph_format import GraphFormat

    GraphFormatAdapter = TypeAdapter(GraphFormat)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

graph_format_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "bn",
  "enum" : [ "bn", "simplified" ]
}
""",
    object_hook=with_example_provider,
)
graph_format_model_schema.update({"definitions": MODEL_DEFINITIONS})

graph_format_faker = JSF(graph_format_model_schema, allow_none_optionals=1)


class GraphFormatStub:
    """GraphFormat unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return graph_format_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GraphFormat":
        """Create GraphFormat stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(GraphFormatAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GraphFormatAdapter.validate_python(
            json, context={"skip_validation": True}
        )
