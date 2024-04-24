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
    from waylay.services.rules.models.list_tasks_format_parameter import (
        ListTasksFormatParameter,
    )

    ListTasksFormatParameterAdapter = TypeAdapter(ListTasksFormatParameter)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

list_tasks_format_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "bn",
  "enum" : [ "bn", "simplified" ]
}
""",
    object_hook=with_example_provider,
)
list_tasks_format_parameter_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_tasks_format_parameter_faker = JSF(
    list_tasks_format_parameter_model_schema, allow_none_optionals=1
)


class ListTasksFormatParameterStub:
    """ListTasksFormatParameter unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_tasks_format_parameter_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ListTasksFormatParameter":
        """Create ListTasksFormatParameter stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListTasksFormatParameterAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListTasksFormatParameterAdapter.validate_python(
            json, context={"skip_validation": True}
        )
