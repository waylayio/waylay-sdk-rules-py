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
    from waylay.services.rules.models.template_entity_metadata import (
        TemplateEntityMetadata,
    )

    TemplateEntityMetadataAdapter = TypeAdapter(TemplateEntityMetadata)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_entity_metadata_model_schema = json.loads(
    r"""{
  "example" : {
    "name" : "aTemplate",
    "user" : "user/xxxx",
    "createTime" : 1647953373000,
    "lastUpdateTime" : 1653828573000,
    "discoveryTemplate" : false
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityCommonAttributes"
  }, {
    "required" : [ "createTime", "discoveryTemplate", "lastUpdateTime", "name", "user" ],
    "type" : "object",
    "properties" : {
      "user" : {
        "$ref" : "#/components/schemas/TemplateUser"
      },
      "createTime" : {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      },
      "lastUpdateTime" : {
        "$ref" : "#/components/schemas/UnixEpochMillis"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
template_entity_metadata_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_entity_metadata_faker = JSF(
    template_entity_metadata_model_schema, allow_none_optionals=1
)


class TemplateEntityMetadataStub:
    """TemplateEntityMetadata unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_entity_metadata_faker.generate()

    @classmethod
    def create_instance(cls) -> "TemplateEntityMetadata":
        """Create TemplateEntityMetadata stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TemplateEntityMetadataAdapter.validate_python(cls.create_json())
