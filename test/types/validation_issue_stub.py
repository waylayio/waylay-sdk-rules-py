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
    from waylay.services.rules.models.validation_issue import ValidationIssue

    ValidationIssueAdapter = TypeAdapter(ValidationIssue)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

validation_issue_model_schema = json.loads(
    r"""{
  "required" : [ "message", "severity", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "type" : "string",
      "description" : "Indication of \"area\" where validation issue is situated",
      "example" : "BINDING"
    },
    "message" : {
      "type" : "string",
      "description" : "Description of the issue",
      "example" : "rawData fas no field status"
    },
    "severity" : {
      "$ref" : "#/components/schemas/ValidationIssue_severity"
    },
    "details" : {
      "type" : "object",
      "description" : "Object containing identifying information on what gives the issue",
      "example" : {
        "nodeId" : "debugDialog_1",
        "property" : "message",
        "binding" : "${nodes.dice_1.rawData.status}"
      }
    },
    "suggestion" : {
      "type" : "string",
      "description" : "Suggestion on how to change the object to get the issue fixed",
      "example" : "maybe you are looking for one of these: state, randomValue"
    }
  }
}
""",
    object_hook=with_example_provider,
)
validation_issue_model_schema.update({"definitions": MODEL_DEFINITIONS})

validation_issue_faker = JSF(validation_issue_model_schema, allow_none_optionals=1)


class ValidationIssueStub:
    """ValidationIssue unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return validation_issue_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ValidationIssue":
        """Create ValidationIssue stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ValidationIssueAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ValidationIssueAdapter.validate_python(
            json, context={"skip_validation": True}
        )
