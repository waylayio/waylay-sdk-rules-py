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
    from waylay.services.rules.models.node_state_specification import (
        NodeStateSpecification,
    )

    NodeStateSpecificationAdapter = TypeAdapter(NodeStateSpecification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

node_state_specification_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "state" : {
      "type" : "string",
      "description" : "State to set. Should be one of the supported states of the sensor"
    },
    "rawData" : {
      "type" : "object",
      "description" : "rawData to set"
    }
  },
  "example" : {
    "state" : "THREE",
    "rawData" : {
      "randomValue" : 0.3458795
    }
  }
}
""",
    object_hook=with_example_provider,
)
node_state_specification_model_schema.update({"definitions": MODEL_DEFINITIONS})

node_state_specification_faker = JSF(
    node_state_specification_model_schema, allow_none_optionals=1
)


class NodeStateSpecificationStub:
    """NodeStateSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return node_state_specification_faker.generate()

    @classmethod
    def create_instance(cls) -> "NodeStateSpecification":
        """Create NodeStateSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NodeStateSpecificationAdapter.validate_python(cls.create_json())
