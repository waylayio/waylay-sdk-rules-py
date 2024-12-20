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
    from waylay.services.rules.models.one_time_task_setting import OneTimeTaskSetting

    OneTimeTaskSettingAdapter = TypeAdapter(OneTimeTaskSetting)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

one_time_task_setting_model_schema = json.loads(
    r"""{
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/OneTimeTaskSetting_type"
    }
  }
}
""",
    object_hook=with_example_provider,
)
one_time_task_setting_model_schema.update({"definitions": MODEL_DEFINITIONS})

one_time_task_setting_faker = JSF(
    one_time_task_setting_model_schema, allow_none_optionals=1
)


class OneTimeTaskSettingStub:
    """OneTimeTaskSetting unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return one_time_task_setting_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "OneTimeTaskSetting":
        """Create OneTimeTaskSetting stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                OneTimeTaskSettingAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return OneTimeTaskSettingAdapter.validate_python(
            json, context={"skip_validation": True}
        )
