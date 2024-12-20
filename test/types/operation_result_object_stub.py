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
    from waylay.services.rules.models.operation_result_object import (
        OperationResultObject,
    )

    OperationResultObjectAdapter = TypeAdapter(OperationResultObject)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

operation_result_object_model_schema = json.loads(
    r"""{
  "required" : [ "finishedTime", "results" ],
  "type" : "object",
  "properties" : {
    "finishedTime" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "results" : {
      "$ref" : "#/components/schemas/OperationResultObject_results"
    }
  },
  "description" : "Finished Batch Operation results"
}
""",
    object_hook=with_example_provider,
)
operation_result_object_model_schema.update({"definitions": MODEL_DEFINITIONS})

operation_result_object_faker = JSF(
    operation_result_object_model_schema, allow_none_optionals=1
)


class OperationResultObjectStub:
    """OperationResultObject unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return operation_result_object_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "OperationResultObject":
        """Create OperationResultObject stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                OperationResultObjectAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return OperationResultObjectAdapter.validate_python(
            json, context={"skip_validation": True}
        )
