"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.trigger_type import TriggerType

    TriggerTypeAdapter = TypeAdapter(TriggerType)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

trigger_type_model_schema = json.loads(
    r"""{
  "title" : "TriggerType",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/StateChangeTrigger"
  }, {
    "$ref" : "#/components/schemas/StatesTrigger"
  }, {
    "$ref" : "#/components/schemas/ExecutionTrigger"
  } ]
}
""",
    object_hook=with_example_provider,
)
trigger_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

trigger_type_faker = JSF(trigger_type_model_schema, allow_none_optionals=1)


class TriggerTypeStub:
    """TriggerType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return trigger_type_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TriggerType":
        """Create TriggerType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(TriggerTypeAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TriggerTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
