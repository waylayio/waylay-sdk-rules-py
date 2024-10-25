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
    from waylay.services.rules.models.execute_plugs_specification import (
        ExecutePlugsSpecification,
    )

    ExecutePlugsSpecificationAdapter = TypeAdapter(ExecutePlugsSpecification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

execute_plugs_specification_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "properties" : {
      "title" : "specific input parameters",
      "type" : "object",
      "example" : {
        "threshold" : 20
      }
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "streamData" : {
      "title" : "Stream data",
      "type" : "object",
      "example" : {
        "temperature" : 21,
        "timestamp" : 1582988389
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
execute_plugs_specification_model_schema.update({"definitions": MODEL_DEFINITIONS})

execute_plugs_specification_faker = JSF(
    execute_plugs_specification_model_schema, allow_none_optionals=1
)


class ExecutePlugsSpecificationStub:
    """ExecutePlugsSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return execute_plugs_specification_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ExecutePlugsSpecification":
        """Create ExecutePlugsSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ExecutePlugsSpecificationAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ExecutePlugsSpecificationAdapter.validate_python(
            json, context={"skip_validation": True}
        )
