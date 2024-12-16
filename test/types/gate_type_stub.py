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
    from waylay.services.rules.models.gate_type import GateType

    GateTypeAdapter = TypeAdapter(GateType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

gate_type_model_schema = json.loads(
    r"""{
  "title" : "GateType",
  "type" : "string",
  "description" : "Supported gate types.",
  "enum" : [ "AND", "OR", "GENERAL", "NAND" ]
}
""",
    object_hook=with_example_provider,
)
gate_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

gate_type_faker = JSF(gate_type_model_schema, allow_none_optionals=1)


class GateTypeStub:
    """GateType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return gate_type_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GateType":
        """Create GateType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(GateTypeAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GateTypeAdapter.validate_python(json, context={"skip_validation": True})
