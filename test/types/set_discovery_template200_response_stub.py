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
    from waylay.services.rules.models.set_discovery_template200_response import (
        SetDiscoveryTemplate200Response,
    )

    SetDiscoveryTemplate200ResponseAdapter = TypeAdapter(
        SetDiscoveryTemplate200Response
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

set_discovery_template_200_response_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityMetadata"
  }, {
    "$ref" : "#/components/schemas/GraphDefinition"
  }, {
    "type" : "object",
    "properties" : {
      "name" : {
        "type" : "string",
        "example" : "discoverResourceType"
      },
      "discoveryTemplate" : {
        "type" : "boolean",
        "example" : true
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
set_discovery_template_200_response_model_schema.update({
    "definitions": MODEL_DEFINITIONS
})

set_discovery_template_200_response_faker = JSF(
    set_discovery_template_200_response_model_schema, allow_none_optionals=1
)


class SetDiscoveryTemplate200ResponseStub:
    """SetDiscoveryTemplate200Response unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return set_discovery_template_200_response_faker.generate()

    @classmethod
    def create_instance(cls) -> "SetDiscoveryTemplate200Response":
        """Create SetDiscoveryTemplate200Response stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SetDiscoveryTemplate200ResponseAdapter.validate_python(cls.create_json())