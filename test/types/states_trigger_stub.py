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
    from waylay.services.rules.models.states_trigger import StatesTrigger

    StatesTriggerAdapter = TypeAdapter(StatesTrigger)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

states_trigger_model_schema = json.loads(
    r"""{
  "description" : "A trigger that is conditional on the states of the source.",
  "example" : {
    "sourceLabel" : "AND_1",
    "destinationLabel" : "debugDialog_2",
    "statesTrigger" : [ "TRUE" ]
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericTrigger"
  }, {
    "required" : [ "destinationLabel", "sourceLabel", "statesTrigger" ],
    "properties" : {
      "statesTrigger" : {
        "type" : "array",
        "description" : "array of states of source node under which to fire",
        "items" : {
          "type" : "string"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
states_trigger_model_schema.update({"definitions": MODEL_DEFINITIONS})

states_trigger_faker = JSF(states_trigger_model_schema, allow_none_optionals=1)


class StatesTriggerStub:
    """StatesTrigger unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return states_trigger_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "StatesTrigger":
        """Create StatesTrigger stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                StatesTriggerAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StatesTriggerAdapter.validate_python(
            json, context={"skip_validation": True}
        )
