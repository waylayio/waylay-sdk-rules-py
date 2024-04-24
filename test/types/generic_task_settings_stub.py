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
    from waylay.services.rules.models.generic_task_settings import GenericTaskSettings

    GenericTaskSettingsAdapter = TypeAdapter(GenericTaskSettings)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

generic_task_settings_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TaskName"
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "resetObservations" : {
      "title" : "whether to clear observations before next invocation",
      "type" : "boolean",
      "default" : true
    },
    "parallel" : {
      "title" : "whether to run sensors in parallel or sequentially",
      "type" : "boolean",
      "default" : true
    },
    "gatesNeedFullObservation" : {
      "title" : "Only evaluate gates when all inputs are observed",
      "type" : "boolean",
      "default" : false
    },
    "tags" : {
      "$ref" : "#/components/schemas/TagsTaskObject"
    },
    "variables" : {
      "$ref" : "#/components/schemas/VariablesTaskObject"
    }
  }
}
""",
    object_hook=with_example_provider,
)
generic_task_settings_model_schema.update({"definitions": MODEL_DEFINITIONS})

generic_task_settings_faker = JSF(
    generic_task_settings_model_schema, allow_none_optionals=1
)


class GenericTaskSettingsStub:
    """GenericTaskSettings unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return generic_task_settings_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GenericTaskSettings":
        """Create GenericTaskSettings stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if not json:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GenericTaskSettingsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GenericTaskSettingsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
