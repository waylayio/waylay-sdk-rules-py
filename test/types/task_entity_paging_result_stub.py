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
    from waylay.services.rules.models.task_entity_paging_result import (
        TaskEntityPagingResult,
    )

    TaskEntityPagingResultAdapter = TypeAdapter(TaskEntityPagingResult)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

task_entity_paging_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/TaskEntity"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
task_entity_paging_result_model_schema.update({"definitions": MODEL_DEFINITIONS})

task_entity_paging_result_faker = JSF(
    task_entity_paging_result_model_schema, allow_none_optionals=1
)


class TaskEntityPagingResultStub:
    """TaskEntityPagingResult unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return task_entity_paging_result_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TaskEntityPagingResult":
        """Create TaskEntityPagingResult stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TaskEntityPagingResultAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TaskEntityPagingResultAdapter.validate_python(
            json, context={"skip_validation": True}
        )
