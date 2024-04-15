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
    from waylay.services.rules.models.note_element import NoteElement

    NoteElementAdapter = TypeAdapter(NoteElement)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

note_element_model_schema = json.loads(
    r"""{
  "title" : "NoteElement",
  "required" : [ "position", "text" ],
  "type" : "object",
  "properties" : {
    "position" : {
      "$ref" : "#/components/schemas/Position"
    },
    "text" : {
      "title" : "Text",
      "type" : "string",
      "example" : "Example template having some sensors and gates"
    }
  },
  "additionalProperties" : false,
  "description" : "Representation of a note in a Rule Template."
}
""",
    object_hook=with_example_provider,
)
note_element_model_schema.update({"definitions": MODEL_DEFINITIONS})

note_element_faker = JSF(note_element_model_schema, allow_none_optionals=1)


class NoteElementStub:
    """NoteElement unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return note_element_faker.generate()

    @classmethod
    def create_instance(cls) -> "NoteElement":
        """Create NoteElement stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return NoteElementAdapter.validate_python(cls.create_json())