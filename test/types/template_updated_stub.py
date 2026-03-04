"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.template_updated import TemplateUpdated

    TemplateUpdatedAdapter = TypeAdapter(TemplateUpdated)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

template_updated_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityMetadata"
  }, {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  } ]
}
""",
    object_hook=with_example_provider,
)
template_updated_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_updated_faker = JSF(template_updated_model_schema, allow_none_optionals=1)


class TemplateUpdatedStub:
    """TemplateUpdated unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_updated_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "TemplateUpdated":
        """Create TemplateUpdated stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplateUpdatedAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplateUpdatedAdapter.validate_python(
            json, context={"skip_validation": True}
        )
