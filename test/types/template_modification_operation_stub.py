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
    from waylay.services.rules.models.template_modification_operation import (
        TemplateModificationOperation,
    )

    TemplateModificationOperationAdapter = TypeAdapter(TemplateModificationOperation)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_modification_operation_model_schema = json.loads(
    r"""{
  "title" : "TemplateModification_operation",
  "type" : "string",
  "enum" : [ "updatePlugins" ]
}
""",
    object_hook=with_example_provider,
)
template_modification_operation_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_modification_operation_faker = JSF(
    template_modification_operation_model_schema, allow_none_optionals=1
)


class TemplateModificationOperationStub:
    """TemplateModificationOperation unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_modification_operation_faker.generate()

    @classmethod
    def create_instance(cls) -> "TemplateModificationOperation":
        """Create TemplateModificationOperation stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TemplateModificationOperationAdapter.validate_python(cls.create_json())
