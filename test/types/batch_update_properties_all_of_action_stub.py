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
    from waylay.services.rules.models.batch_update_properties_all_of_action import (
        BatchUpdatePropertiesAllOfAction,
    )

    BatchUpdatePropertiesAllOfActionAdapter = TypeAdapter(
        BatchUpdatePropertiesAllOfAction
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

batch_update_properties_all_of_action_model_schema = json.loads(
    r"""{
  "title" : "BatchUpdateProperties_allOf_action",
  "type" : "string",
  "enum" : [ "updateProperties" ]
}
""",
    object_hook=with_example_provider,
)
batch_update_properties_all_of_action_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

batch_update_properties_all_of_action_faker = JSF(
    batch_update_properties_all_of_action_model_schema, allow_none_optionals=1
)


class BatchUpdatePropertiesAllOfActionStub:
    """BatchUpdatePropertiesAllOfAction unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return batch_update_properties_all_of_action_faker.generate()

    @classmethod
    def create_instance(cls) -> "BatchUpdatePropertiesAllOfAction":
        """Create BatchUpdatePropertiesAllOfAction stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return BatchUpdatePropertiesAllOfActionAdapter.validate_python(
            cls.create_json()
        )
