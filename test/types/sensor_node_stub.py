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
    from waylay.services.rules.models.sensor_node import SensorNode

    SensorNodeAdapter = TypeAdapter(SensorNode)
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

sensor_node_model_schema = json.loads(
    r"""{
  "title" : "SensorNode",
  "required" : [ "label", "name", "version" ],
  "type" : "object",
  "properties" : {
    "label" : {
      "$ref" : "#/components/schemas/NodeId"
    },
    "name" : {
      "title" : "Name of sensor",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/Version"
    },
    "properties" : {
      "title" : "Key-value object of required properties",
      "type" : "object"
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "sequence" : {
      "title" : "Sequence number if omitted default is 1",
      "type" : "integer",
      "default" : 1
    },
    "position" : {
      "$ref" : "#/components/schemas/Position"
    },
    "dataTrigger" : {
      "title" : "Boolean to indicate if sensor needs to be executed if data for `resource` is received",
      "type" : "boolean",
      "default" : true
    },
    "tickTrigger" : {
      "title" : "Boolean to indicate if sensor needs to be executed on task tick",
      "type" : "boolean",
      "default" : true
    },
    "evictionTime" : {
      "title" : "Time (in milliseconds) after which sensor goes back to default state",
      "minimum" : 0,
      "type" : "integer"
    },
    "pollingPeriod" : {
      "title" : "Time (in milliseconds) to give sensor it’s own tick",
      "minimum" : 1,
      "type" : "integer"
    },
    "schedule" : {
      "title" : "Schedule",
      "type" : "string",
      "description" : "Either a valid cron or RRule expression to set the sensor's own tick"
    },
    "timeout" : {
      "title" : "Time (in ISO 8601 duration format) before the plugin times out, defaults to PT50S (50 seconds)",
      "type" : "string",
      "default" : "PT50S"
    },
    "timeoutState" : {
      "title" : "State that will be returned as result if plug execution times out",
      "type" : "string"
    },
    "loopDef" : {
      "title" : "Loop definition",
      "minimum" : 0,
      "type" : "string",
      "description" : "A loop definition is a string that defines items over which node will be iterated multiple times.\nThe string is an JSON array of JSON objects.During template execution the sensor node with such\na defined loop definition will be invoked for every JSON Object in the JSON array.\nParameter is optional. Node will be executed only once if loop definition is not defined.",
      "example" : "[{\"name\": \"alpha\"}, {\"name\": \"beta\"}]"
    },
    "retryConfig" : {
      "$ref" : "#/components/schemas/RetryConfig"
    }
  },
  "additionalProperties" : false,
  "description" : "Representation of a sensor in a Rule Template.",
  "example" : {
    "label" : "dice_1",
    "name" : "dice",
    "version" : "1.0.9",
    "position" : [ 100, 150 ],
    "dataTrigger" : false,
    "tickTrigger" : true,
    "timeout" : "PT5S"
  }
}
""",
    object_hook=with_example_provider,
)
sensor_node_model_schema.update({"definitions": MODEL_DEFINITIONS})

sensor_node_faker = JSF(sensor_node_model_schema, allow_none_optionals=1)


class SensorNodeStub:
    """SensorNode unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return sensor_node_faker.generate()

    @classmethod
    def create_instance(cls) -> "SensorNode":
        """Create SensorNode stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return SensorNodeAdapter.validate_python(cls.create_json())
