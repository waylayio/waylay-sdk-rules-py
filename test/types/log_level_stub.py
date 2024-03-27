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
    from waylay.services.rules.models.log_level import LogLevel

    LogLevelAdapter = TypeAdapter(LogLevel)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

log_level_model_schema = json.loads(
    r"""{
  "type" : "string",
  "example" : "INFO",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR", "NONE" ]
}
""",
    object_hook=with_example_provider,
)
log_level_model_schema.update({"definitions": MODEL_DEFINITIONS})

log_level_faker = JSF(log_level_model_schema, allow_none_optionals=1)


class LogLevelStub:
    """LogLevel unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return log_level_faker.generate()

    @classmethod
    def create_instance(cls) -> "LogLevel":
        """Create LogLevel stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return LogLevelAdapter.validate_python(cls.create_json())
