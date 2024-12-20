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
    from waylay.services.rules.models.actuator_execution_result import (
        ActuatorExecutionResult,
    )

    ActuatorExecutionResultAdapter = TypeAdapter(ActuatorExecutionResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

actuator_execution_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "result" : {
      "type" : "boolean",
      "description" : "flag indicating if the actuator was successfully executed"
    },
    "error" : {
      "type" : "string",
      "description" : "error message in case of failure"
    },
    "rawData" : {
      "type" : "object"
    },
    "log" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
actuator_execution_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

actuator_execution_result_faker = JSF(
    actuator_execution_result_model_schema, allow_none_optionals=1
)


class ActuatorExecutionResultStub:
    """ActuatorExecutionResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return actuator_execution_result_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ActuatorExecutionResult":
        """Create ActuatorExecutionResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ActuatorExecutionResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ActuatorExecutionResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
