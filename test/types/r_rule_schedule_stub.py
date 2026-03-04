"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.r_rule_schedule import RRuleSchedule

    RRuleScheduleAdapter = TypeAdapter(RRuleSchedule)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

r_rule_schedule_model_schema = json.loads(
    r"""{
  "title" : "RRuleSchedule",
  "required" : [ "rrule" ],
  "type" : "object",
  "properties" : {
    "rrule" : {
      "$ref" : "#/components/schemas/RRuleExpression"
    }
  }
}
""",
    object_hook=with_example_provider,
)
r_rule_schedule_model_schema.update({"definitions": MODEL_DEFINITIONS})

r_rule_schedule_faker = JSF(r_rule_schedule_model_schema, allow_none_optionals=1)


class RRuleScheduleStub:
    """RRuleSchedule unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return r_rule_schedule_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "RRuleSchedule":
        """Create RRuleSchedule stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                RRuleScheduleAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return RRuleScheduleAdapter.validate_python(
            json, context={"skip_validation": True}
        )
