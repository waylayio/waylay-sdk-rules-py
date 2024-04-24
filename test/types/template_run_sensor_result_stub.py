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
    from waylay.services.rules.models.template_run_sensor_result import (
        TemplateRunSensorResult,
    )

    TemplateRunSensorResultAdapter = TypeAdapter(TemplateRunSensorResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_run_sensor_result_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/SensorExecutionResult"
  }, {
    "required" : [ "executed" ],
    "type" : "object",
    "properties" : {
      "executed" : {
        "type" : "boolean",
        "description" : "flag indicating if the sensor was executed"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
template_run_sensor_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_run_sensor_result_faker = JSF(
    template_run_sensor_result_model_schema, allow_none_optionals=1
)


class TemplateRunSensorResultStub:
    """TemplateRunSensorResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_run_sensor_result_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TemplateRunSensorResult":
        """Create TemplateRunSensorResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateRunSensorResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateRunSensorResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
