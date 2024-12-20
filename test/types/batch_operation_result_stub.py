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
    from waylay.services.rules.models.batch_operation_result import BatchOperationResult

    BatchOperationResultAdapter = TypeAdapter(BatchOperationResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_operation_result_model_schema = json.loads(
    r"""{
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe",
    "operation" : {
      "entity" : "task",
      "action" : "delete",
      "description" : "Remove tasks filtered by type=onetime AND status=stopped AND finishedBefore=1648738809733"
    },
    "queueTime" : 1663269720694,
    "finishedTime" : 1663269725784,
    "results" : {
      "success" : {
        "4bbec310-4b8a-4f82-954d-f6268e7736a3" : {
          "statusCode" : 200
        },
        "b637dc9c-b8fc-4d1e-8743-b1456364e559" : {
          "statusCode" : 200
        }
      },
      "failure" : {
        "0cf62e41-be40-42bf-a88f-6fc803bcb957" : {
          "statusCode" : 404,
          "error" : "No task with id 0cf62e41-be40-42bf-a88f-6fc803bcb957"
        }
      }
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchOperation"
  }, {
    "$ref" : "#/components/schemas/OperationResultObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
batch_operation_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

batch_operation_result_faker = JSF(
    batch_operation_result_model_schema, allow_none_optionals=1
)


class BatchOperationResultStub:
    """BatchOperationResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_operation_result_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "BatchOperationResult":
        """Create BatchOperationResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                BatchOperationResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return BatchOperationResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
