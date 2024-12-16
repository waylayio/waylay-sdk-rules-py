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
    from waylay.services.rules.models.reactive_task_setting_type import (
        ReactiveTaskSettingType,
    )

    ReactiveTaskSettingTypeAdapter = TypeAdapter(ReactiveTaskSettingType)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

reactive_task_setting_type_model_schema = json.loads(
    r"""{
  "title" : "ReactiveTaskSetting_type",
  "type" : "string",
  "enum" : [ "reactive" ]
}
""",
    object_hook=with_example_provider,
)
reactive_task_setting_type_model_schema.update({"definitions": MODEL_DEFINITIONS})

reactive_task_setting_type_faker = JSF(
    reactive_task_setting_type_model_schema, allow_none_optionals=1
)


class ReactiveTaskSettingTypeStub:
    """ReactiveTaskSettingType unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return reactive_task_setting_type_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ReactiveTaskSettingType":
        """Create ReactiveTaskSettingType stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ReactiveTaskSettingTypeAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ReactiveTaskSettingTypeAdapter.validate_python(
            json, context={"skip_validation": True}
        )
