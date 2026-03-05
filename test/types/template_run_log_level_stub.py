"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.template_run_log_level import TemplateRunLogLevel

    TemplateRunLogLevelAdapter = TypeAdapter(TemplateRunLogLevel)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

template_run_log_level_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "DEBUG",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR" ]
}
""",
    object_hook=with_example_provider,
)
template_run_log_level_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_run_log_level_faker = JSF(
    template_run_log_level_model_schema, allow_none_optionals=1
)


class TemplateRunLogLevelStub:
    """TemplateRunLogLevel unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_run_log_level_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TemplateRunLogLevel":
        """Create TemplateRunLogLevel stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateRunLogLevelAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateRunLogLevelAdapter.validate_python(
            json, context={"skip_validation": True}
        )
