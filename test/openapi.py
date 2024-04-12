import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/rules.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_a_tasks_batch_operation_specification_model_schema = json.loads(
    r"""{
  "title" : "a tasks batch operation specification",
  "type" : "object",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchUpdatePlugin"
  }, {
    "$ref" : "#/components/schemas/BatchTaskCommand"
  }, {
    "$ref" : "#/components/schemas/BatchUpdateProperties"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "a_tasks_batch_operation_specification": _a_tasks_batch_operation_specification_model_schema
})

_actuator_execution_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "result" : {
      "type" : "boolean",
      "description" : "flag indicating if the actuator was successfully executed"
    },
    "error" : {
      "type" : "string",
      "description" : "error message in case of failure"
    },
    "rawData" : {
      "type" : "object"
    },
    "log" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ActuatorExecutionResult": _actuator_execution_result_model_schema
})

_actuator_node_model_schema = json.loads(
    r"""{
  "title" : "ActuatorNode",
  "required" : [ "label", "name", "version" ],
  "type" : "object",
  "properties" : {
    "label" : {
      "$ref" : "#/components/schemas/NodeId"
    },
    "name" : {
      "title" : "Name of actuator",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/Version"
    },
    "properties" : {
      "title" : "Key-value object of required properties",
      "type" : "object"
    },
    "sequence" : {
      "title" : "Sequence",
      "type" : "integer"
    },
    "position" : {
      "$ref" : "#/components/schemas/Position"
    },
    "timeout" : {
      "title" : "Time (in ISO 8601 duration format) before the plugin times out, defaults to PT50S (50 seconds)",
      "type" : "string",
      "default" : "PT50S"
    }
  },
  "additionalProperties" : false,
  "description" : "Representation of an actuator in a Rule Template.",
  "example" : {
    "label" : "debugDialog_1",
    "name" : "debugDialog",
    "version" : "1.0.0",
    "properties" : {
      "message" : "Dice 1 has value ONE"
    },
    "position" : [ 827, 323 ]
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ActuatorNode": _actuator_node_model_schema})

_batch_id_query_model_schema = json.loads(
    r"""{
  "required" : [ "ids" ],
  "type" : "object",
  "properties" : {
    "ids" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TaskId"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchIdQuery": _batch_id_query_model_schema})

_batch_operation_model_schema = json.loads(
    r"""{
  "required" : [ "id", "operation", "queueTime", "user" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "$ref" : "#/components/schemas/BatchId"
    },
    "user" : {
      "type" : "string",
      "description" : "User id of the user who started the operation",
      "example" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe"
    },
    "operation" : {
      "$ref" : "#/components/schemas/BatchOperation_operation"
    },
    "queueTime" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    }
  },
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe",
    "operation" : {
      "entity" : "task",
      "action" : "delete",
      "description" : "Remove tasks filtered by type=onetime AND status=stopped AND finishedBefore=1648738809733"
    },
    "queueTime" : 1663269720694
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchOperation": _batch_operation_model_schema})

_batch_operation_enqueued_model_schema = json.loads(
    r"""{
  "title" : "Batch operation enqueued",
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 202
    },
    "uri" : {
      "type" : "string",
      "description" : "URI where the batch operation status can be followed",
      "format" : "uri",
      "example" : "/rules/v1/batch/afcea5a1-81df-44f6-bd34-e0b602a2cf3d"
    },
    "entity" : {
      "$ref" : "#/components/schemas/BatchOperation"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Batch_operation_enqueued": _batch_operation_enqueued_model_schema
})

_batch_operation_operation_model_schema = json.loads(
    r"""{
  "title" : "BatchOperation_operation",
  "required" : [ "action", "description", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchTask_entity"
    },
    "action" : {
      "$ref" : "#/components/schemas/BatchOperation_operation_action"
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "description of the operations",
      "example" : "Remove tasks filtered by ids=808aec38-3fb3-4163-a45e-1890e94081ea"
    }
  },
  "description" : "Summary of the batch operation"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchOperation_operation": _batch_operation_operation_model_schema
})

_batch_operation_operation_action_model_schema = json.loads(
    r"""{
  "title" : "BatchOperation_operation_action",
  "type" : "string",
  "example" : "delete",
  "enum" : [ "updatePlugins", "delete", "start", "restart", "stop", "reload", "updateProperties" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchOperation_operation_action": _batch_operation_operation_action_model_schema
})

_batch_operation_result_model_schema = json.loads(
    r"""{
  "example" : {
    "id" : "afcea5a1-81df-44f6-bd34-e0b602a2cf3d",
    "user" : "user/22f6dfdf-a50c-4eab-953e-8d2e56891dbe",
    "operation" : {
      "entity" : "task",
      "action" : "delete",
      "description" : "Remove tasks filtered by type=onetime AND status=stopped AND finishedBefore=1648738809733"
    },
    "queueTime" : 1663269720694,
    "finishedTime" : 1663269725784,
    "results" : {
      "success" : {
        "4bbec310-4b8a-4f82-954d-f6268e7736a3" : {
          "statusCode" : 200
        },
        "b637dc9c-b8fc-4d1e-8743-b1456364e559" : {
          "statusCode" : 200
        }
      },
      "failure" : {
        "0cf62e41-be40-42bf-a88f-6fc803bcb957" : {
          "statusCode" : 404,
          "error" : "No task with id 0cf62e41-be40-42bf-a88f-6fc803bcb957"
        }
      }
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchOperation"
  }, {
    "$ref" : "#/components/schemas/OperationResultObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchOperationResult": _batch_operation_result_model_schema})

_batch_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TaskName"
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "type" : {
      "$ref" : "#/components/schemas/TaskScenarioType"
    },
    "status" : {
      "$ref" : "#/components/schemas/TaskStatus"
    },
    "template" : {
      "$ref" : "#/components/schemas/TemplateId"
    },
    "plugin" : {
      "type" : "string",
      "description" : "either name of a plugin (e.g. `mySensor`), or full version specification of the plug (e.g `mySensor:1.0.3`)",
      "example" : "mySensor:1.0.3"
    },
    "user" : {
      "$ref" : "#/components/schemas/TaskUser"
    },
    "finishedBefore" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "tags" : {
      "$ref" : "#/components/schemas/TagsTaskObject"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchQuery": _batch_query_model_schema})

_batch_task_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/BatchTask_entity"
    },
    "action" : {
      "type" : "string"
    },
    "query" : {
      "$ref" : "#/components/schemas/BatchTask_query"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchTask": _batch_task_model_schema})

_batch_task_command_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Execute command on multiple task",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchTask"
  }, {
    "required" : [ "action", "entity", "query" ],
    "properties" : {
      "action" : {
        "$ref" : "#/components/schemas/BatchTaskCommand_allOf_action"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchTaskCommand": _batch_task_command_model_schema})

_batch_task_command_all_of_action_model_schema = json.loads(
    r"""{
  "title" : "BatchTaskCommand_allOf_action",
  "type" : "string",
  "enum" : [ "delete", "start", "restart", "stop", "reload", "stopAndDelete" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchTaskCommand_allOf_action": _batch_task_command_all_of_action_model_schema
})

_batch_task_entity_model_schema = json.loads(
    r"""{
  "title" : "BatchTask_entity",
  "type" : "string",
  "enum" : [ "task" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchTask_entity": _batch_task_entity_model_schema})

_batch_task_query_model_schema = json.loads(
    r"""{
  "title" : "BatchTask_query",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchIdQuery"
  }, {
    "$ref" : "#/components/schemas/BatchQuery"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchTask_query": _batch_task_query_model_schema})

_batch_update_plugin_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Upgrade plugins on multiple tasks",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchTask"
  }, {
    "required" : [ "action", "actionParameters", "entity", "query" ],
    "properties" : {
      "action" : {
        "$ref" : "#/components/schemas/TemplateModification_operation"
      },
      "actionParameters" : {
        "$ref" : "#/components/schemas/PluginUpdateSpec"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchUpdatePlugin": _batch_update_plugin_model_schema})

_batch_update_properties_model_schema = json.loads(
    r"""{
  "type" : "object",
  "description" : "Update variables and/or tags of multiple tasks",
  "allOf" : [ {
    "$ref" : "#/components/schemas/BatchTask"
  }, {
    "required" : [ "action", "actionParameters", "entity", "query" ],
    "properties" : {
      "action" : {
        "$ref" : "#/components/schemas/BatchUpdateProperties_allOf_action"
      },
      "actionParameters" : {
        "$ref" : "#/components/schemas/PropertyUpdatesSpec"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchUpdateProperties": _batch_update_properties_model_schema
})

_batch_update_properties_all_of_action_model_schema = json.loads(
    r"""{
  "title" : "BatchUpdateProperties_allOf_action",
  "type" : "string",
  "enum" : [ "updateProperties" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "BatchUpdateProperties_allOf_action": _batch_update_properties_all_of_action_model_schema
})

_bayesian_graph_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "nodes" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    },
    "posterior" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  },
  "description" : "Graph in BN format"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BayesianGraph": _bayesian_graph_model_schema})

_create_task_201_response_model_schema = json.loads(
    r"""{
  "required" : [ "ID" ],
  "type" : "object",
  "properties" : {
    "ID" : {
      "$ref" : "#/components/schemas/TaskId"
    },
    "warnings" : {
      "type" : "array",
      "description" : "List of task warning issues. Will only be there if query parameter `returnWarnings` was set to `true`",
      "items" : {
        "$ref" : "#/components/schemas/ValidationIssue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "create_task_201_response": _create_task_201_response_model_schema
})

_create_template_201_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 201
    },
    "uri" : {
      "type" : "string",
      "format" : "uri",
      "example" : "/rules/v1/templates/internet.json"
    },
    "entity" : {
      "$ref" : "#/components/schemas/TemplateEntity"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "create_template_201_response": _create_template_201_response_model_schema
})

_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "integer",
      "example" : 400
    },
    "error" : {
      "type" : "string"
    },
    "code" : {
      "type" : "string",
      "description" : "Optional error code"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ErrorResponse": _error_response_model_schema})

_error_with_details_response_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ErrorResponse"
  }, {
    "properties" : {
      "details" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/ValidationIssue"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ErrorWithDetailsResponse": _error_with_details_response_model_schema
})

_execute_plugs_specification_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "properties" : {
      "title" : "specific input parameters",
      "type" : "object",
      "example" : {
        "threshold" : 20
      }
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "streamData" : {
      "title" : "Stream data",
      "type" : "object",
      "example" : {
        "temperature" : 21,
        "timestamp" : 1582988389
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExecutePlugsSpecification": _execute_plugs_specification_model_schema
})

_execution_trigger_model_schema = json.loads(
    r"""{
  "description" : "A trigger that always executes on successful execution of the source.",
  "example" : {
    "sourceLabel" : "AND_1",
    "destinationLabel" : "debugDialog_3"
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericTrigger"
  }, {
    "required" : [ "destinationLabel", "sourceLabel" ],
    "type" : "object"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ExecutionTrigger": _execution_trigger_model_schema})

_failure_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "FailureOperationResult_value",
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    },
    "error" : {
      "title" : "error",
      "type" : "string",
      "description" : "Error description of what went wrong."
    }
  },
  "description" : "The keys will be task ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "FailureOperationResult_value": _failure_operation_result_value_model_schema
})

_gate_type_model_schema = json.loads(
    r"""{
  "title" : "GateType",
  "type" : "string",
  "description" : "Supported gate types.",
  "enum" : [ "AND", "OR", "GENERAL", "NAND" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GateType": _gate_type_model_schema})

_generic_task_settings_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TaskName"
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "resetObservations" : {
      "title" : "whether to clear observations before next invocation",
      "type" : "boolean",
      "default" : true
    },
    "parallel" : {
      "title" : "whether to run sensors in parallel or sequentially",
      "type" : "boolean",
      "default" : true
    },
    "gatesNeedFullObservation" : {
      "title" : "Only evaluate gates when all inputs are observed",
      "type" : "boolean",
      "default" : false
    },
    "tags" : {
      "$ref" : "#/components/schemas/TagsTaskObject"
    },
    "variables" : {
      "$ref" : "#/components/schemas/VariablesTaskObject"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GenericTaskSettings": _generic_task_settings_model_schema})

_generic_trigger_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "sourceLabel" : {
      "title" : "Label of source sensor or gate",
      "allOf" : [ {
        "$ref" : "#/components/schemas/NodeId"
      } ]
    },
    "destinationLabel" : {
      "title" : "Label of the destination sensor or actuator",
      "allOf" : [ {
        "$ref" : "#/components/schemas/NodeId"
      } ]
    },
    "invocationPolicy" : {
      "title" : "Time (in seconds) that defines how long to wait before firing the same actuator again, even if the condition is met.",
      "minimum" : 1,
      "type" : "integer"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GenericTrigger": _generic_trigger_model_schema})

_get_batch_operation_200_response_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/BatchOperationResult"
  }, {
    "$ref" : "#/components/schemas/BatchOperation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "get_batch_operation_200_response": _get_batch_operation_200_response_model_schema
})

_graph_definition_model_schema = json.loads(
    r"""{
  "title" : "GraphDefinition",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  }, {
    "$ref" : "#/components/schemas/BayesianGraph"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GraphDefinition": _graph_definition_model_schema})

_list_tasks_format_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "bn",
  "enum" : [ "bn", "simplified" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "list_tasks_format_parameter": _list_tasks_format_parameter_model_schema
})

_list_tasks_tags_key_parameter_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "type" : "string"
  }, {
    "type" : "number"
  }, {
    "type" : "boolean"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "list_tasks_tags_key_parameter": _list_tasks_tags_key_parameter_model_schema
})

_log_level_model_schema = json.loads(
    r"""{
  "type" : "string",
  "example" : "INFO",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR", "NONE" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LogLevel": _log_level_model_schema})

_logs_inner_model_schema = json.loads(
    r"""{
  "title" : "Logs_inner",
  "required" : [ "level", "message", "time" ],
  "type" : "object",
  "properties" : {
    "time" : {
      "$ref" : "#/components/schemas/SO8601Timestamp"
    },
    "level" : {
      "$ref" : "#/components/schemas/Logs_inner_level"
    },
    "message" : {
      "title" : "message",
      "type" : "string",
      "example" : "SMS sent"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Logs_inner": _logs_inner_model_schema})

_logs_inner_level_model_schema = json.loads(
    r"""{
  "title" : "Logs_inner_level",
  "type" : "string",
  "example" : "INFO",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Logs_inner_level": _logs_inner_level_model_schema})

_node_state_specification_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "state" : {
      "type" : "string",
      "description" : "State to set. Should be one of the supported states of the sensor"
    },
    "rawData" : {
      "type" : "object",
      "description" : "rawData to set"
    }
  },
  "example" : {
    "state" : "THREE",
    "rawData" : {
      "randomValue" : 0.3458795
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NodeStateSpecification": _node_state_specification_model_schema
})

_note_element_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"NoteElement": _note_element_model_schema})

_one_time_task_setting_model_schema = json.loads(
    r"""{
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/OneTimeTaskSetting_type"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"OneTimeTaskSetting": _one_time_task_setting_model_schema})

_one_time_task_setting_type_model_schema = json.loads(
    r"""{
  "title" : "OneTimeTaskSetting_type",
  "type" : "string",
  "enum" : [ "onetime" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OneTimeTaskSetting_type": _one_time_task_setting_type_model_schema
})

_operation_result_object_model_schema = json.loads(
    r"""{
  "required" : [ "finishedTime", "results" ],
  "type" : "object",
  "properties" : {
    "finishedTime" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "results" : {
      "$ref" : "#/components/schemas/OperationResultObject_results"
    }
  },
  "description" : "Finished Batch Operation results"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OperationResultObject": _operation_result_object_model_schema
})

_operation_result_object_results_model_schema = json.loads(
    r"""{
  "title" : "OperationResultObject_results",
  "required" : [ "failure", "success" ],
  "type" : "object",
  "properties" : {
    "success" : {
      "$ref" : "#/components/schemas/SuccessOperationResult"
    },
    "failure" : {
      "$ref" : "#/components/schemas/FailureOperationResult"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OperationResultObject_results": _operation_result_object_results_model_schema
})

_paging_result_model_schema = json.loads(
    r"""{
  "required" : [ "limit", "skip", "total" ],
  "type" : "object",
  "properties" : {
    "skip" : {
      "$ref" : "#/components/schemas/PagingSkip"
    },
    "limit" : {
      "$ref" : "#/components/schemas/PagingLimit"
    },
    "total" : {
      "$ref" : "#/components/schemas/PagingTotal"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PagingResult": _paging_result_model_schema})

_periodic_task_setting_model_schema = json.loads(
    r"""{
  "required" : [ "frequency", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PeriodicTaskSetting_type"
    },
    "frequency" : {
      "type" : "integer",
      "description" : "polling frequency in milliseconds",
      "example" : 900000
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PeriodicTaskSetting": _periodic_task_setting_model_schema})

_periodic_task_setting_type_model_schema = json.loads(
    r"""{
  "title" : "PeriodicTaskSetting_type",
  "type" : "string",
  "enum" : [ "periodic" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PeriodicTaskSetting_type": _periodic_task_setting_type_model_schema
})

_plugin_update_spec_model_schema = json.loads(
    r"""{
  "required" : [ "fromVersion", "name", "toVersion" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Name of the plugin to update",
      "example" : "mySensor"
    },
    "fromVersion" : {
      "$ref" : "#/components/schemas/PluginUpdateSpec_fromVersion"
    },
    "toVersion" : {
      "description" : "Plugin version to upgrade to",
      "allOf" : [ {
        "$ref" : "#/components/schemas/Version"
      } ]
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PluginUpdateSpec": _plugin_update_spec_model_schema})

_plugin_update_spec_from_version_model_schema = json.loads(
    r"""{
  "title" : "PluginUpdateSpec_fromVersion",
  "description" : "plugin version selection to upgrade",
  "example" : "any",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/Version"
  }, {
    "$ref" : "#/components/schemas/PluginUpdateSpec_fromVersion_oneOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PluginUpdateSpec_fromVersion": _plugin_update_spec_from_version_model_schema
})

_plugin_update_spec_from_version_one_of_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PluginUpdateSpec_fromVersion_oneOf": _plugin_update_spec_from_version_one_of_model_schema
})

_possible_values__enum_declaration__inner_model_schema = json.loads(
    r"""{
  "title" : "Possible_values__enum_declaration__inner",
  "oneOf" : [ {
    "type" : "string"
  }, {
    "type" : "number"
  }, {
    "type" : "object"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Possible_values__enum_declaration__inner": _possible_values__enum_declaration__inner_model_schema
})

_property_updates_spec_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "variables" : {
      "type" : "object",
      "description" : "Set of variables to update.\nWill be merged with the current variables.\nTo delete any of the current variables (and fall back to the default value from the template) set the value to `null`"
    },
    "tags" : {
      "type" : "object",
      "description" : "Key-value pairs.\nWill be merged with the current tags.\nTo delete any of the current tags set the value to `null`"
    }
  },
  "nullable" : true,
  "anyOf" : [ ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PropertyUpdatesSpec": _property_updates_spec_model_schema})

_reactive_task_setting_model_schema = json.loads(
    r"""{
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/ReactiveTaskSetting_type"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ReactiveTaskSetting": _reactive_task_setting_model_schema})

_reactive_task_setting_type_model_schema = json.loads(
    r"""{
  "title" : "ReactiveTaskSetting_type",
  "type" : "string",
  "enum" : [ "reactive" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ReactiveTaskSetting_type": _reactive_task_setting_type_model_schema
})

_relation_node_model_schema = json.loads(
    r"""{
  "title" : "RelationNode",
  "required" : [ "combinations", "label", "parentLabels", "type" ],
  "type" : "object",
  "properties" : {
    "label" : {
      "title" : "label",
      "example" : "AND_1",
      "allOf" : [ {
        "$ref" : "#/components/schemas/NodeId"
      } ]
    },
    "type" : {
      "$ref" : "#/components/schemas/GateType"
    },
    "parentLabels" : {
      "title" : "Labels of the sensors that are attached to this gate",
      "type" : "array",
      "example" : [ "dice_1", "dice_2" ],
      "items" : {
        "$ref" : "#/components/schemas/NodeId"
      }
    },
    "combinations" : {
      "title" : "Combinations of connected sensor's states",
      "type" : "array",
      "items" : {
        "type" : "array",
        "example" : [ "ONE", "TWO" ],
        "items" : {
          "type" : "string",
          "description" : "State of one of the connected sensors"
        }
      }
    },
    "position" : {
      "$ref" : "#/components/schemas/Position"
    }
  },
  "additionalProperties" : false,
  "description" : "Representation of a gate in a Rule Template."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RelationNode": _relation_node_model_schema})

_replace_template_200_response_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityMetadata"
  }, {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "replace_template_200_response": _replace_template_200_response_model_schema
})

_resource_data_injection_model_schema = json.loads(
    r"""{
  "title" : "ResourceDataInjection",
  "required" : [ "resource" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "timestamp" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    }
  },
  "additionalProperties" : true,
  "description" : "data to inject per resource"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ResourceDataInjection": _resource_data_injection_model_schema
})

_retry_config_model_schema = json.loads(
    r"""{
  "required" : [ "maxBackoff", "maxRetries", "minBackoff" ],
  "type" : "object",
  "properties" : {
    "maxRetries" : {
      "minimum" : 0,
      "type" : "integer",
      "example" : 3
    },
    "minBackoff" : {
      "type" : "string",
      "format" : "duration",
      "example" : "PT1S"
    },
    "maxBackoff" : {
      "type" : "string",
      "format" : "duration",
      "example" : "PT10S"
    },
    "errorState" : {
      "type" : "string",
      "description" : "Optional sensor state which will be used to set the state of the node when the maxRetries is reached.",
      "format" : "string",
      "example" : "Error"
    }
  },
  "description" : "Configuration for retrying a template node.\nThe node execution will be retried `maxRetries` times.\nThe delay between retries will be exponentially increased starting from `minBackoff` to `maxBackoff`.\nIf the node execution fails after `maxRetries` retries, the node state will be set to `errorState` if it that property is provided.\nOtherwise node execution will fail. Error state should be one of the possible states defined by the sensor node."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RetryConfig": _retry_config_model_schema})

_run_template_log_level_parameter_model_schema = json.loads(
    r"""{
  "type" : "string",
  "default" : "DEBUG",
  "enum" : [ "DEBUG", "INFO", "WARN", "ERROR" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "run_template_logLevel_parameter": _run_template_log_level_parameter_model_schema
})

_scheduled_task_setting_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "required" : [ "type" ],
    "properties" : {
      "type" : {
        "$ref" : "#/components/schemas/ScheduledTaskSetting_allOf_type"
      },
      "timeZone" : {
        "$ref" : "#/components/schemas/TimeZoneId"
      }
    }
  }, {
    "nullable" : true,
    "oneOf" : [ ]
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ScheduledTaskSetting": _scheduled_task_setting_model_schema})

_scheduled_task_setting_all_of_type_model_schema = json.loads(
    r"""{
  "title" : "ScheduledTaskSetting_allOf_type",
  "type" : "string",
  "enum" : [ "scheduled" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ScheduledTaskSetting_allOf_type": _scheduled_task_setting_all_of_type_model_schema
})

_sensor_execution_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "result" : {
      "type" : "boolean",
      "description" : "flag indicating if the sensor was successfully executed"
    },
    "state" : {
      "type" : "string",
      "description" : "observedState field returned by the sensor execution"
    },
    "error" : {
      "type" : "string",
      "description" : "error message in case of failure"
    },
    "rawData" : {
      "type" : "object",
      "description" : "the rawData returned by the sensor execution"
    },
    "log" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SensorExecutionResult": _sensor_execution_result_model_schema
})

_sensor_node_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"SensorNode": _sensor_node_model_schema})

_simplified_graph_model_schema = json.loads(
    r"""{
  "title" : "SimplifiedGraph",
  "type" : "object",
  "properties" : {
    "sensors" : {
      "title" : "sensors",
      "type" : "array",
      "description" : "List of sensors with required properties",
      "items" : {
        "$ref" : "#/components/schemas/SensorNode"
      }
    },
    "actuators" : {
      "title" : "actuators",
      "type" : "array",
      "description" : "List of actuators with required properties",
      "items" : {
        "$ref" : "#/components/schemas/ActuatorNode"
      }
    },
    "relations" : {
      "title" : "relations",
      "type" : "array",
      "description" : "List of relations (gates) between sensors",
      "items" : {
        "$ref" : "#/components/schemas/RelationNode"
      }
    },
    "triggers" : {
      "title" : "triggers",
      "type" : "array",
      "description" : "List of conditions under which actuators/sensors get executed.",
      "items" : {
        "$ref" : "#/components/schemas/SimplifiedGraph_triggers_inner"
      }
    }
  },
  "description" : "Graph in simplified format"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SimplifiedGraph": _simplified_graph_model_schema})

_simplified_graph_triggers_inner_model_schema = json.loads(
    r"""{
  "title" : "SimplifiedGraph_triggers_inner",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/StateChangeTrigger"
  }, {
    "$ref" : "#/components/schemas/StatesTrigger"
  }, {
    "$ref" : "#/components/schemas/ExecutionTrigger"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SimplifiedGraph_triggers_inner": _simplified_graph_triggers_inner_model_schema
})

_state_change_trigger_model_schema = json.loads(
    r"""{
  "description" : "A trigger that executes on state change.",
  "example" : {
    "sourceLabel" : "AND_1",
    "destinationLabel" : "debugDialog_1",
    "stateChangeTrigger" : {
      "stateFrom" : "FALSE",
      "stateTo" : "*"
    }
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericTrigger"
  }, {
    "required" : [ "destinationLabel", "sourceLabel", "stateChangeTrigger" ],
    "properties" : {
      "stateChangeTrigger" : {
        "$ref" : "#/components/schemas/TriggerStateChange"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StateChangeTrigger": _state_change_trigger_model_schema})

_states_trigger_model_schema = json.loads(
    r"""{
  "description" : "A trigger that is conditional on the states of the source.",
  "example" : {
    "sourceLabel" : "AND_1",
    "destinationLabel" : "debugDialog_2",
    "statesTrigger" : [ "TRUE" ]
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericTrigger"
  }, {
    "required" : [ "destinationLabel", "sourceLabel", "statesTrigger" ],
    "properties" : {
      "statesTrigger" : {
        "type" : "array",
        "description" : "array of states of source node under which to fire",
        "items" : {
          "type" : "string"
        }
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatesTrigger": _states_trigger_model_schema})

_stream_data_model_schema = json.loads(
    r"""{
  "title" : "stream data",
  "required" : [ "data", "resource" ],
  "type" : "object",
  "properties" : {
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "data" : {
      "$ref" : "#/components/schemas/stream_data_data"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"stream_data": _stream_data_model_schema})

_stream_data_data_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"stream_data_data": _stream_data_data_model_schema})

_success_operation_result_value_model_schema = json.loads(
    r"""{
  "title" : "SuccessOperationResult_value",
  "required" : [ "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "title" : "statusCode",
      "type" : "integer",
      "description" : "The statusCode of the operation"
    }
  },
  "description" : "The keys will be task ids."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "SuccessOperationResult_value": _success_operation_result_value_model_schema
})

_task_defaults_element_model_schema = json.loads(
    r"""{
  "title" : "TaskDefaultsElement",
  "type" : "object",
  "properties" : {
    "tags" : {
      "$ref" : "#/components/schemas/TagsTaskObject"
    },
    "type" : {
      "$ref" : "#/components/schemas/TaskScenarioType"
    },
    "resetObservations" : {
      "type" : "boolean"
    },
    "parallel" : {
      "type" : "boolean"
    },
    "gatesNeedFullObservation" : {
      "type" : "boolean"
    },
    "cron" : {
      "$ref" : "#/components/schemas/CronExpression"
    },
    "rrule" : {
      "$ref" : "#/components/schemas/RRuleExpression"
    },
    "timeZone" : {
      "$ref" : "#/components/schemas/TimeZoneId"
    },
    "frequency" : {
      "type" : "integer",
      "description" : "polling frequency in milliseconds"
    }
  },
  "description" : "default task settings that will be applied when creating a task from the template",
  "example" : {
    "type" : "periodic",
    "frequency" : 900000,
    "resetObservations" : false
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskDefaultsElement": _task_defaults_element_model_schema})

_task_entity_model_schema = json.loads(
    r"""{
  "required" : [ "ID", "createTime", "name", "network", "status", "user" ],
  "type" : "object",
  "properties" : {
    "ID" : {
      "$ref" : "#/components/schemas/TaskId"
    },
    "name" : {
      "$ref" : "#/components/schemas/TaskName"
    },
    "status" : {
      "$ref" : "#/components/schemas/TaskStatus"
    },
    "user" : {
      "$ref" : "#/components/schemas/TaskUser"
    },
    "createTime" : {
      "$ref" : "#/components/schemas/UnixEpochMillis"
    },
    "template" : {
      "$ref" : "#/components/schemas/TemplateId"
    },
    "network" : {
      "type" : "object",
      "description" : "The graph, either from the template or from the task definition. Depending on the `format` query parameter either BN or simplified format"
    },
    "resourceIds" : {
      "$ref" : "#/components/schemas/TaskResourceIds"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskEntity": _task_entity_model_schema})

_task_entity_paging_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "properties" : {
      "values" : {
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/TaskEntity"
        }
      }
    }
  }, {
    "$ref" : "#/components/schemas/PagingResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TaskEntityPagingResult": _task_entity_paging_result_model_schema
})

_task_from_template_model_schema = json.loads(
    r"""{
  "type" : "object",
  "example" : {
    "name" : "myTask",
    "template" : "myTemplate",
    "type" : "reactive"
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/TaskSettings"
  }, {
    "required" : [ "name", "template" ],
    "properties" : {
      "start" : {
        "title" : "boolean to indicate whether task must be started after creation",
        "type" : "boolean",
        "default" : true
      },
      "template" : {
        "$ref" : "#/components/schemas/TemplateId"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskFromTemplate": _task_from_template_model_schema})

_task_scenario_type_model_schema = json.loads(
    r"""{
  "title" : "TaskScenarioType",
  "type" : "string",
  "description" : "Triggering deployment scenario for a task.",
  "enum" : [ "scheduled", "periodic", "onetime", "reactive" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskScenarioType": _task_scenario_type_model_schema})

_task_settings_model_schema = json.loads(
    r"""{
  "title" : "TaskSettings",
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/GenericTaskSettings"
  }, {
    "$ref" : "#/components/schemas/TaskTypeSettings"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskSettings": _task_settings_model_schema})

_task_specification_model_schema = json.loads(
    r"""{
  "oneOf" : [ {
    "$ref" : "#/components/schemas/TaskFromTemplate"
  }, {
    "$ref" : "#/components/schemas/TaskWithRule"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskSpecification": _task_specification_model_schema})

_task_status_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Status of a task",
  "enum" : [ "running", "stopped", "failed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskStatus": _task_status_model_schema})

_task_type_settings_model_schema = json.loads(
    r"""{
  "type" : "object",
  "oneOf" : [ {
    "$ref" : "#/components/schemas/ScheduledTaskSetting"
  }, {
    "$ref" : "#/components/schemas/PeriodicTaskSetting"
  }, {
    "$ref" : "#/components/schemas/OneTimeTaskSetting"
  }, {
    "$ref" : "#/components/schemas/ReactiveTaskSetting"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskTypeSettings": _task_type_settings_model_schema})

_task_with_rule_model_schema = json.loads(
    r"""{
  "type" : "object",
  "example" : {
    "task" : {
      "name" : "myTask",
      "type" : "reactive"
    },
    "sensors" : [ ],
    "relations" : [ ],
    "triggers" : [ ]
  },
  "allOf" : [ {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  }, {
    "required" : [ "task" ],
    "properties" : {
      "notes" : {
        "title" : "List of notes as explanation for users",
        "type" : "array",
        "items" : {
          "$ref" : "#/components/schemas/NoteElement"
        }
      },
      "task" : {
        "$ref" : "#/components/schemas/TaskWithRule_allOf_task"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaskWithRule": _task_with_rule_model_schema})

_task_with_rule_all_of_task_model_schema = json.loads(
    r"""{
  "title" : "TaskWithRule_allOf_task",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TaskSettings"
  }, {
    "required" : [ "name" ],
    "type" : "object",
    "properties" : {
      "start" : {
        "title" : "boolean to indicate whether task must be started after creation",
        "type" : "boolean",
        "default" : true
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TaskWithRule_allOf_task": _task_with_rule_all_of_task_model_schema
})

_template_details_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityMetadata"
  }, {
    "$ref" : "#/components/schemas/GraphDefinition"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TemplateDetails": _template_details_model_schema})

_template_entity_model_schema = json.loads(
    r"""{
  "type" : "object",
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateEntityCommonAttributes"
  }, {
    "$ref" : "#/components/schemas/SimplifiedGraph"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TemplateEntity": _template_entity_model_schema})

_template_entity_common_attributes_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TemplateId"
    },
    "discoveryTemplate" : {
      "type" : "boolean",
      "description" : "flag to indicate if the template is the discovery template",
      "example" : false
    },
    "tags" : {
      "$ref" : "#/components/schemas/TemplateTags"
    },
    "variables" : {
      "type" : "array",
      "description" : "Variable declarations",
      "items" : {
        "$ref" : "#/components/schemas/VariableDeclaration"
      }
    },
    "taskDefaults" : {
      "$ref" : "#/components/schemas/TaskDefaultsElement"
    },
    "notes" : {
      "type" : "array",
      "description" : "List of notes as explanation for users",
      "items" : {
        "$ref" : "#/components/schemas/NoteElement"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateEntityCommonAttributes": _template_entity_common_attributes_model_schema
})

_template_entity_metadata_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({
    "TemplateEntityMetadata": _template_entity_metadata_model_schema
})

_template_modification_model_schema = json.loads(
    r"""{
  "required" : [ "operation", "updates" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "$ref" : "#/components/schemas/TemplateModification_operation"
    },
    "updates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/PluginUpdateSpec"
      }
    },
    "reloadTasks" : {
      "type" : "boolean",
      "description" : "Should all tasks created from the template be reloaded",
      "example" : true,
      "default" : false
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TemplateModification": _template_modification_model_schema})

_template_modification_operation_model_schema = json.loads(
    r"""{
  "title" : "TemplateModification_operation",
  "type" : "string",
  "enum" : [ "updatePlugins" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateModification_operation": _template_modification_operation_model_schema
})

_template_run_actuator_result_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/ActuatorExecutionResult"
  }, {
    "required" : [ "executed" ],
    "type" : "object",
    "properties" : {
      "executed" : {
        "type" : "boolean",
        "description" : "flag indicating if the actuator was executed"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateRunActuatorResult": _template_run_actuator_result_model_schema
})

_template_run_configuration_model_schema = json.loads(
    r"""{
  "title" : "TemplateRunConfiguration",
  "type" : "object",
  "properties" : {
    "executeActuators" : {
      "title" : "executeActuators",
      "type" : "boolean",
      "description" : "Flag to trigger actual execution of actuators",
      "default" : false
    },
    "resource" : {
      "$ref" : "#/components/schemas/ResourceId"
    },
    "resetObservations" : {
      "title" : "resetObservations",
      "type" : "boolean",
      "description" : "reset observations before injecting data",
      "default" : true
    },
    "gatesNeedFullObservation" : {
      "title" : "gatesNeedFullObservation",
      "type" : "boolean",
      "description" : "Only evaluate gates when all inputs are observed",
      "default" : false
    }
  },
  "description" : "Template run configurations"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateRunConfiguration": _template_run_configuration_model_schema
})

_template_run_invocation_model_schema = json.loads(
    r"""{
  "required" : [ "actuators", "invocationId", "log", "sensors", "taskId" ],
  "type" : "object",
  "properties" : {
    "taskId" : {
      "$ref" : "#/components/schemas/TaskId"
    },
    "invocationId" : {
      "$ref" : "#/components/schemas/InvocationId"
    },
    "sensors" : {
      "title" : "Sensors Results",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/TemplateRunSensorResult"
      },
      "description" : "The execution result for each of the sensors of the template",
      "example" : {
        "alarm" : {
          "executed" : true,
          "result" : true,
          "state" : "OK",
          "rawData" : { },
          "log" : [ ]
        },
        "streamingDataSensor" : {
          "executed" : true,
          "result" : true,
          "state" : "ABOVE",
          "rawData" : {
            "parameter" : "temperature",
            "threshold" : 20
          }
        }
      }
    },
    "actuators" : {
      "title" : "Actuator Results",
      "type" : "object",
      "additionalProperties" : {
        "$ref" : "#/components/schemas/TemplateRunActuatorResult"
      },
      "description" : "The execution result for each of the actuators of the template",
      "example" : {
        "send_sms" : {
          "executed" : true,
          "result" : true,
          "log" : [ ]
        }
      }
    },
    "log" : {
      "title" : "Logs",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Logs_inner"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateRunInvocation": _template_run_invocation_model_schema
})

_template_run_sensor_result_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/SensorExecutionResult"
  }, {
    "required" : [ "executed" ],
    "type" : "object",
    "properties" : {
      "executed" : {
        "type" : "boolean",
        "description" : "flag indicating if the sensor was executed"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateRunSensorResult": _template_run_sensor_result_model_schema
})

_template_run_specification_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({
    "TemplateRunSpecification": _template_run_specification_model_schema
})

_template_run_with_graph_specification_model_schema = json.loads(
    r"""{
  "allOf" : [ {
    "$ref" : "#/components/schemas/TemplateRunSpecification"
  }, {
    "required" : [ "graph" ],
    "type" : "object",
    "properties" : {
      "graph" : {
        "$ref" : "#/components/schemas/GraphDefinition"
      }
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TemplateRunWithGraphSpecification": _template_run_with_graph_specification_model_schema
})

_transformer_execution_result_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "result" : {
      "type" : "boolean",
      "description" : "flag indicating if the actuator was Successfully Executed"
    },
    "error" : {
      "type" : "string",
      "description" : "error message in case of failure"
    },
    "data" : {
      "type" : "object"
    },
    "log" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "TransformerExecutionResult": _transformer_execution_result_model_schema
})

_trigger_state_change_model_schema = json.loads(
    r"""{
  "required" : [ "stateFrom", "stateTo" ],
  "type" : "object",
  "properties" : {
    "stateFrom" : {
      "title" : "State from which to trigger, or '*'",
      "type" : "string"
    },
    "stateTo" : {
      "title" : "State to, or '*'",
      "type" : "string"
    }
  },
  "description" : "State change specification under which to trigger the next node."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TriggerStateChange": _trigger_state_change_model_schema})

_upgrade_plugins_templates_200_response_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({
    "upgradePlugins_templates_200_response": _upgrade_plugins_templates_200_response_model_schema
})

_validation_issue_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({"ValidationIssue": _validation_issue_model_schema})

_validation_issue_severity_model_schema = json.loads(
    r"""{
  "title" : "ValidationIssue_severity",
  "type" : "string",
  "description" : "Severity of the issue. ERROR means that object cannot be created if the issue is not fixed. WARNING means that the object can be created, but that errors might be encountered at runtime",
  "example" : "WARNING",
  "enum" : [ "ERROR", "WARNING" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ValidationIssue_severity": _validation_issue_severity_model_schema
})

_variable_declaration_model_schema = json.loads(
    r"""{
  "title" : "VariableDeclaration",
  "required" : [ "name", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Variable Name"
    },
    "displayName" : {
      "type" : "string",
      "description" : "Display name. Will default to the name if not specified"
    },
    "type" : {
      "$ref" : "#/components/schemas/VariableType"
    },
    "format" : {
      "$ref" : "#/components/schemas/VariableFormat"
    },
    "mandatory" : {
      "type" : "boolean",
      "description" : "flag to indicate if value for variable is mandatory or not",
      "default" : false
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/VariableDeclaration_defaultValue"
    }
  },
  "description" : "Variable declaration.",
  "example" : {
    "name" : "city",
    "displayName" : "City",
    "type" : "string",
    "mandatory" : true
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VariableDeclaration": _variable_declaration_model_schema})

_variable_declaration_default_value_model_schema = json.loads(
    r"""{
  "title" : "VariableDeclaration_defaultValue",
  "description" : "Default value for the variable",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "number"
  }, {
    "type" : "boolean"
  }, {
    "type" : "object"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "VariableDeclaration_defaultValue": _variable_declaration_default_value_model_schema
})

_variable_format_model_schema = json.loads(
    r"""{
  "title" : "VariableFormat",
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "title" : "Type",
      "type" : "string",
      "example" : "resource"
    },
    "values" : {
      "title" : "Possible values (enum declaration)",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Possible_values__enum_declaration__inner"
      }
    }
  },
  "description" : "Format for a variable definition."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VariableFormat": _variable_format_model_schema})

_variable_type_model_schema = json.loads(
    r"""{
  "title" : "VariableType",
  "type" : "string",
  "description" : "Value type for a template variable.",
  "enum" : [ "string", "boolean", "integer", "double", "long", "float", "object" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VariableType": _variable_type_model_schema})

_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "status", "version" ],
  "type" : "object",
  "properties" : {
    "version" : {
      "type" : "string",
      "example" : "5.12.1"
    },
    "name" : {
      "type" : "string",
      "example" : "waylay-engine"
    },
    "startTime" : {
      "type" : "string",
      "format" : "date-time",
      "example" : "2011-09-06T12:03:27.845Z"
    },
    "uptime" : {
      "type" : "integer",
      "format" : "int64",
      "example" : 12703737
    },
    "status" : {
      "$ref" : "#/components/schemas/VersionResponse_status"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionResponse": _version_response_model_schema})

_version_response_status_model_schema = json.loads(
    r"""{
  "title" : "VersionResponse_status",
  "type" : "string",
  "example" : "STARTED",
  "enum" : [ "STARTING", "STARTED", "FAILED" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "VersionResponse_status": _version_response_status_model_schema
})
