"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.log_entry_level import LogEntryLevel

    LogEntryLevelAdapter = TypeAdapter(LogEntryLevel)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

log_entry_level_model_schema = json.loads(
    r"""{
  "title" : "LogEntryLevel",
  "type" : "string",
  "example" : "INFO",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR" ]
}
""",
    object_hook=with_example_provider,
)
log_entry_level_model_schema.update({"definitions": MODEL_DEFINITIONS})

log_entry_level_faker = JSF(log_entry_level_model_schema, allow_none_optionals=1)


class LogEntryLevelStub:
    """LogEntryLevel unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return log_entry_level_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LogEntryLevel":
        """Create LogEntryLevel stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                LogEntryLevelAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LogEntryLevelAdapter.validate_python(
            json, context={"skip_validation": True}
        )
