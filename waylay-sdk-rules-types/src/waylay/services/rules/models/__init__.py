# coding: utf-8
"""Waylay rules engine: REST Models.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

version: 6.5.0

The REST api to manage rule tasks and rule templates in the Waylay platform.

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "6.5.0.20240415"

# import models into model package
from .a_tasks_batch_operation_specification import ATasksBatchOperationSpecification
from .actuator_execution_result import ActuatorExecutionResult
from .actuator_node import ActuatorNode
from .batch_id_query import BatchIdQuery
from .batch_operation import BatchOperation
from .batch_operation_enqueued import BatchOperationEnqueued
from .batch_operation_operation import BatchOperationOperation
from .batch_operation_operation_action import BatchOperationOperationAction
from .batch_operation_result import BatchOperationResult
from .batch_query import BatchQuery
from .batch_task import BatchTask
from .batch_task_command import BatchTaskCommand
from .batch_task_command_all_of_action import BatchTaskCommandAllOfAction
from .batch_task_entity import BatchTaskEntity
from .batch_task_query import BatchTaskQuery
from .batch_update_plugin import BatchUpdatePlugin
from .batch_update_properties import BatchUpdateProperties
from .batch_update_properties_all_of_action import BatchUpdatePropertiesAllOfAction
from .bayesian_graph import BayesianGraph
from .create_task201_response import CreateTask201Response
from .create_template201_response import CreateTemplate201Response
from .error_response import ErrorResponse
from .error_with_details_response import ErrorWithDetailsResponse
from .execute_plugs_specification import ExecutePlugsSpecification
from .execution_trigger import ExecutionTrigger
from .failure_operation_result_value import FailureOperationResultValue
from .gate_type import GateType
from .generic_task_settings import GenericTaskSettings
from .generic_trigger import GenericTrigger
from .get_batch_operation200_response import GetBatchOperation200Response
from .graph_definition import GraphDefinition
from .list_tasks_format_parameter import ListTasksFormatParameter
from .list_tasks_tags_key_parameter import ListTasksTagsKeyParameter
from .log_level import LogLevel
from .logs_inner import LogsInner
from .logs_inner_level import LogsInnerLevel
from .node_state_specification import NodeStateSpecification
from .note_element import NoteElement
from .one_time_task_setting import OneTimeTaskSetting
from .one_time_task_setting_type import OneTimeTaskSettingType
from .operation_result_object import OperationResultObject
from .operation_result_object_results import OperationResultObjectResults
from .paging_result import PagingResult
from .periodic_task_setting import PeriodicTaskSetting
from .periodic_task_setting_type import PeriodicTaskSettingType
from .plugin_update_spec import PluginUpdateSpec
from .plugin_update_spec_from_version import PluginUpdateSpecFromVersion
from .plugin_update_spec_from_version_one_of import PluginUpdateSpecFromVersionOneOf
from .possible_values_enum_declaration_inner import PossibleValuesEnumDeclarationInner
from .property_updates_spec import PropertyUpdatesSpec
from .reactive_task_setting import ReactiveTaskSetting
from .reactive_task_setting_type import ReactiveTaskSettingType
from .relation_node import RelationNode
from .replace_template200_response import ReplaceTemplate200Response
from .resource_data_injection import ResourceDataInjection
from .retry_config import RetryConfig
from .run_template_log_level_parameter import RunTemplateLogLevelParameter
from .scheduled_task_setting import ScheduledTaskSetting
from .scheduled_task_setting_all_of_type import ScheduledTaskSettingAllOfType
from .sensor_execution_result import SensorExecutionResult
from .sensor_node import SensorNode
from .simplified_graph import SimplifiedGraph
from .simplified_graph_triggers_inner import SimplifiedGraphTriggersInner
from .state_change_trigger import StateChangeTrigger
from .states_trigger import StatesTrigger
from .stream_data import StreamData
from .stream_data_data import StreamDataData
from .success_operation_result_value import SuccessOperationResultValue
from .task_defaults_element import TaskDefaultsElement
from .task_entity import TaskEntity
from .task_entity_paging_result import TaskEntityPagingResult
from .task_from_template import TaskFromTemplate
from .task_scenario_type import TaskScenarioType
from .task_settings import TaskSettings
from .task_specification import TaskSpecification
from .task_status import TaskStatus
from .task_type_settings import TaskTypeSettings
from .task_with_rule import TaskWithRule
from .task_with_rule_all_of_task import TaskWithRuleAllOfTask
from .template_details import TemplateDetails
from .template_entity import TemplateEntity
from .template_entity_common_attributes import TemplateEntityCommonAttributes
from .template_entity_metadata import TemplateEntityMetadata
from .template_modification import TemplateModification
from .template_modification_operation import TemplateModificationOperation
from .template_run_actuator_result import TemplateRunActuatorResult
from .template_run_configuration import TemplateRunConfiguration
from .template_run_invocation import TemplateRunInvocation
from .template_run_sensor_result import TemplateRunSensorResult
from .template_run_specification import TemplateRunSpecification
from .template_run_with_graph_specification import TemplateRunWithGraphSpecification
from .transformer_execution_result import TransformerExecutionResult
from .trigger_state_change import TriggerStateChange
from .upgrade_plugins_templates200_response import UpgradePluginsTemplates200Response
from .validation_issue import ValidationIssue
from .validation_issue_severity import ValidationIssueSeverity
from .variable_declaration import VariableDeclaration
from .variable_declaration_default_value import VariableDeclarationDefaultValue
from .variable_format import VariableFormat
from .variable_type import VariableType
from .version_response import VersionResponse
from .version_response_status import VersionResponseStatus

__all__ = [
    "__version__",
    "ATasksBatchOperationSpecification",
    "ActuatorExecutionResult",
    "ActuatorNode",
    "BatchIdQuery",
    "BatchOperation",
    "BatchOperationEnqueued",
    "BatchOperationOperation",
    "BatchOperationOperationAction",
    "BatchOperationResult",
    "BatchQuery",
    "BatchTask",
    "BatchTaskCommand",
    "BatchTaskCommandAllOfAction",
    "BatchTaskEntity",
    "BatchTaskQuery",
    "BatchUpdatePlugin",
    "BatchUpdateProperties",
    "BatchUpdatePropertiesAllOfAction",
    "BayesianGraph",
    "CreateTask201Response",
    "CreateTemplate201Response",
    "ErrorResponse",
    "ErrorWithDetailsResponse",
    "ExecutePlugsSpecification",
    "ExecutionTrigger",
    "FailureOperationResultValue",
    "GateType",
    "GenericTaskSettings",
    "GenericTrigger",
    "GetBatchOperation200Response",
    "GraphDefinition",
    "ListTasksFormatParameter",
    "ListTasksTagsKeyParameter",
    "LogLevel",
    "LogsInner",
    "LogsInnerLevel",
    "NodeStateSpecification",
    "NoteElement",
    "OneTimeTaskSetting",
    "OneTimeTaskSettingType",
    "OperationResultObject",
    "OperationResultObjectResults",
    "PagingResult",
    "PeriodicTaskSetting",
    "PeriodicTaskSettingType",
    "PluginUpdateSpec",
    "PluginUpdateSpecFromVersion",
    "PluginUpdateSpecFromVersionOneOf",
    "PossibleValuesEnumDeclarationInner",
    "PropertyUpdatesSpec",
    "ReactiveTaskSetting",
    "ReactiveTaskSettingType",
    "RelationNode",
    "ReplaceTemplate200Response",
    "ResourceDataInjection",
    "RetryConfig",
    "RunTemplateLogLevelParameter",
    "ScheduledTaskSetting",
    "ScheduledTaskSettingAllOfType",
    "SensorExecutionResult",
    "SensorNode",
    "SimplifiedGraph",
    "SimplifiedGraphTriggersInner",
    "StateChangeTrigger",
    "StatesTrigger",
    "StreamData",
    "StreamDataData",
    "SuccessOperationResultValue",
    "TaskDefaultsElement",
    "TaskEntity",
    "TaskEntityPagingResult",
    "TaskFromTemplate",
    "TaskScenarioType",
    "TaskSettings",
    "TaskSpecification",
    "TaskStatus",
    "TaskTypeSettings",
    "TaskWithRule",
    "TaskWithRuleAllOfTask",
    "TemplateDetails",
    "TemplateEntity",
    "TemplateEntityCommonAttributes",
    "TemplateEntityMetadata",
    "TemplateModification",
    "TemplateModificationOperation",
    "TemplateRunActuatorResult",
    "TemplateRunConfiguration",
    "TemplateRunInvocation",
    "TemplateRunSensorResult",
    "TemplateRunSpecification",
    "TemplateRunWithGraphSpecification",
    "TransformerExecutionResult",
    "TriggerStateChange",
    "UpgradePluginsTemplates200Response",
    "ValidationIssue",
    "ValidationIssueSeverity",
    "VariableDeclaration",
    "VariableDeclarationDefaultValue",
    "VariableFormat",
    "VariableType",
    "VersionResponse",
    "VersionResponseStatus",
]
