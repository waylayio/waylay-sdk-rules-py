"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.stream_data_payload import StreamDataPayload

    StreamDataPayloadAdapter = TypeAdapter(StreamDataPayload)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

stream_data_payload_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "type" : "object",
    "example" : {
      "parameterName" : "temperature",
      "value" : 23,
      "collectedTime" : 1420629467
    }
  }, {
    "type" : "array",
    "example" : [ {
      "parameterName" : "latitude",
      "value" : 51
    }, {
      "parameterName" : "longitude",
      "value" : 3.73
    } ],
    "items" : {
      "type" : "object"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
stream_data_payload_model_schema.update({"definitions": MODEL_DEFINITIONS})

stream_data_payload_faker = JSF(
    stream_data_payload_model_schema, allow_none_optionals=1
)


class StreamDataPayloadStub:
    """StreamDataPayload unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return stream_data_payload_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "StreamDataPayload":
        """Create StreamDataPayload stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                StreamDataPayloadAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return StreamDataPayloadAdapter.validate_python(
            json, context={"skip_validation": True}
        )
