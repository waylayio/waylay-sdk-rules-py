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
    from waylay.services.rules.models.simplified_graph import SimplifiedGraph

    SimplifiedGraphAdapter = TypeAdapter(SimplifiedGraph)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

simplified_graph_model_schema = json.loads(
    r"""{
  "title" : "SimplifiedGraph",
  "type" : "object",
  "properties" : {
    "sensors" : {
      "title" : "sensors",
      "type" : "array",
      "description" : "List of sensors with required properties",
      "items" : {
        "$ref" : "#/components/schemas/SensorNode"
      }
    },
    "actuators" : {
      "title" : "actuators",
      "type" : "array",
      "description" : "List of actuators with required properties",
      "items" : {
        "$ref" : "#/components/schemas/ActuatorNode"
      }
    },
    "relations" : {
      "title" : "relations",
      "type" : "array",
      "description" : "List of relations (gates) between sensors",
      "items" : {
        "$ref" : "#/components/schemas/RelationNode"
      }
    },
    "triggers" : {
      "title" : "triggers",
      "type" : "array",
      "description" : "List of conditions under which actuators/sensors get executed.",
      "items" : {
        "$ref" : "#/components/schemas/SimplifiedGraph_triggers_inner"
      }
    }
  },
  "description" : "Graph in simplified format"
}
""",
    object_hook=with_example_provider,
)
simplified_graph_model_schema.update({"definitions": MODEL_DEFINITIONS})

simplified_graph_faker = JSF(simplified_graph_model_schema, allow_none_optionals=1)


class SimplifiedGraphStub:
    """SimplifiedGraph unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return simplified_graph_faker.generate()

    @classmethod
    def create_instance(cls) -> "SimplifiedGraph":
        """Create SimplifiedGraph stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SimplifiedGraphAdapter.validate_python(cls.create_json())