"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.template_plugins_upgraded import (
        TemplatePluginsUpgraded,
    )

    TemplatePluginsUpgradedAdapter = TypeAdapter(TemplatePluginsUpgraded)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

template_plugins_upgraded_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "successful" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TemplateId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
template_plugins_upgraded_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_plugins_upgraded_faker = JSF(
    template_plugins_upgraded_model_schema, allow_none_optionals=1
)


class TemplatePluginsUpgradedStub:
    """TemplatePluginsUpgraded unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_plugins_upgraded_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "TemplatePluginsUpgraded":
        """Create TemplatePluginsUpgraded stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                TemplatePluginsUpgradedAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return TemplatePluginsUpgradedAdapter.validate_python(
            json, context={"skip_validation": True}
        )
