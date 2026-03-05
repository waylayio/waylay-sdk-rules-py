"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.list_tasks_tags_key import ListTasksTagsKey

    ListTasksTagsKeyAdapter = TypeAdapter(ListTasksTagsKey)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

list_tasks_tags_key_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "type" : "string"
  }, {
    "type" : "number"
  }, {
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
list_tasks_tags_key_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_tasks_tags_key_faker = JSF(
    list_tasks_tags_key_model_schema, allow_none_optionals=1
)


class ListTasksTagsKeyStub:
    """ListTasksTagsKey unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_tasks_tags_key_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ListTasksTagsKey":
        """Create ListTasksTagsKey stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListTasksTagsKeyAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListTasksTagsKeyAdapter.validate_python(
            json, context={"skip_validation": True}
        )
