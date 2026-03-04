"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.log_entry import LogEntry

    LogEntryAdapter = TypeAdapter(LogEntry)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

log_entry_model_schema = json.loads(
    r"""{
  "title" : "LogEntry",
  "required" : [ "level", "message", "time" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/ISO8601Timestamp"
    },
    "level" : {
      "$ref" : "#/components/schemas/LogEntryLevel"
    },
    "message" : {
      "title" : "message",
      "type" : "string",
      "example" : "SMS sent"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
log_entry_model_schema.update({"definitions": MODEL_DEFINITIONS})

log_entry_faker = JSF(log_entry_model_schema, allow_none_optionals=1)


class LogEntryStub:
    """LogEntry unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return log_entry_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "LogEntry":
        """Create LogEntry stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(LogEntryAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return LogEntryAdapter.validate_python(json, context={"skip_validation": True})
