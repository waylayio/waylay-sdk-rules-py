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
    from waylay.services.rules.models.template_run_specification import (
        TemplateRunSpecification,
    )

    TemplateRunSpecificationAdapter = TypeAdapter(TemplateRunSpecification)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

template_run_specification_model_schema = json.loads(
    r"""{
  "title" : "TemplateRunSpecification",
  "type" : "object",
  "properties" : {
    "data" : {
      "title" : "Data Set",
      "type" : "array",
      "description" : "The full dataset to process. If specified, template will be run as reactive template",
      "example" : [ [ {
        "resource" : "resource1",
        "temperature" : 20
      }, {
        "resource" : "resource2",
        "co2" : 100,
        "humidity" : 0.4
      } ], [ {
        "resource" : "resource1",
        "temperature" : 21
      } ] ],
      "items" : {
        "title" : "Dataset For One Invocation",
        "type" : "array",
        "description" : "dataset that will be processed by one invocation",
        "items" : {
          "$ref" : "#/components/schemas/ResourceDataInjection"
        }
      }
    },
    "conf" : {
      "$ref" : "#/components/schemas/TemplateRunConfiguration"
    },
    "variables" : {
      "title" : "Template variables",
      "type" : "object",
      "description" : "The values for the variables declared in the template",
      "example" : {
        "threshold" : 13
      }
    },
    "resourceMetaData" : {
      "title" : "Resource Metadata",
      "type" : "object",
      "additionalProperties" : {
        "type" : "object"
      },
      "description" : "Metadata for any of the resources used in the template.\n\nThe current metadata for all resources used in the template is fetched at the start of the template run.\nThis provided metadata is used to overwrite this current metadata",
      "example" : {
        "resource1" : {
          "name" : "outside_temperature",
          "inside_sensor" : {
            "$$ref" : "/resources/resource2"
          }
        }
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
template_run_specification_model_schema.update({"definitions": MODEL_DEFINITIONS})

template_run_specification_faker = JSF(
    template_run_specification_model_schema, allow_none_optionals=1
)


class TemplateRunSpecificationStub:
    """TemplateRunSpecification unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return template_run_specification_faker.generate()

    @classmethod
    def create_instance(cls) -> "TemplateRunSpecification":
        """Create TemplateRunSpecification stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return TemplateRunSpecificationAdapter.validate_python(cls.create_json())
