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
    from waylay.services.rules.models.get_batch_operation200_response import (
        GetBatchOperation200Response,
    )

    GetBatchOperation200ResponseAdapter = TypeAdapter(GetBatchOperation200Response)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

get_batch_operation_200_response_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
get_batch_operation_200_response_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_batch_operation_200_response_faker = JSF(
    get_batch_operation_200_response_model_schema, allow_none_optionals=1
)


class GetBatchOperation200ResponseStub:
    """GetBatchOperation200Response unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_batch_operation_200_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "GetBatchOperation200Response":
        """Create GetBatchOperation200Response stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return GetBatchOperation200ResponseAdapter.validate_python(cls.create_json())