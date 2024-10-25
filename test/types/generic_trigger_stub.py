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
    from waylay.services.rules.models.generic_trigger import GenericTrigger

    GenericTriggerAdapter = TypeAdapter(GenericTrigger)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

generic_trigger_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "sourceLabel" : {
      "title" : "Label of source sensor or gate",
      "allOf" : [ {
        "$ref" : "#/components/schemas/NodeId"
      } ]
    },
    "destinationLabel" : {
      "title" : "Label of the destination sensor or actuator",
      "allOf" : [ {
        "$ref" : "#/components/schemas/NodeId"
      } ]
    },
    "invocationPolicy" : {
      "title" : "Time (in seconds) that defines how long to wait before firing the same actuator again, even if the condition is met.",
      "minimum" : 1,
      "type" : "integer"
    }
  }
}
""",
    object_hook=with_example_provider,
)
generic_trigger_model_schema.update({"definitions": MODEL_DEFINITIONS})

generic_trigger_faker = JSF(generic_trigger_model_schema, allow_none_optionals=1)


class GenericTriggerStub:
    """GenericTrigger unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return generic_trigger_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "GenericTrigger":
        """Create GenericTrigger stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GenericTriggerAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GenericTriggerAdapter.validate_python(
            json, context={"skip_validation": True}
        )
