"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.variable_format_value import VariableFormatValue

    VariableFormatValueAdapter = TypeAdapter(VariableFormatValue)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

variable_format_value_model_schema = json.loads(
    r"""{
  "title" : "VariableFormatValue",
  "oneOf" : [ {
    "type" : "string"
  }, {
    "type" : "number"
  }, {
    "type" : "object"
  } ]
}
""",
    object_hook=with_example_provider,
)
variable_format_value_model_schema.update({"definitions": MODEL_DEFINITIONS})

variable_format_value_faker = JSF(
    variable_format_value_model_schema, allow_none_optionals=1
)


class VariableFormatValueStub:
    """VariableFormatValue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return variable_format_value_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "VariableFormatValue":
        """Create VariableFormatValue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                VariableFormatValueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return VariableFormatValueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
