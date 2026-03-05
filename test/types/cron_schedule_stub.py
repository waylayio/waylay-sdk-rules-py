"""Waylay rules engine model tests.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.rules.models.cron_schedule import CronSchedule

    CronScheduleAdapter = TypeAdapter(CronSchedule)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

cron_schedule_model_schema = json.loads(
    r"""{
  "title" : "CronSchedule",
  "required" : [ "cron" ],
  "type" : "object",
  "properties" : {
    "cron" : {
      "$ref" : "#/components/schemas/CronExpression"
    }
  }
}
""",
    object_hook=with_example_provider,
)
cron_schedule_model_schema.update({"definitions": MODEL_DEFINITIONS})

cron_schedule_faker = JSF(cron_schedule_model_schema, allow_none_optionals=1)


class CronScheduleStub:
    """CronSchedule unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return cron_schedule_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "CronSchedule":
        """Create CronSchedule stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                CronScheduleAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return CronScheduleAdapter.validate_python(
            json, context={"skip_validation": True}
        )
