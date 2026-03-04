# Waylay Rules Service
The REST api to manage rule tasks and rule templates in the Waylay platform.

This Python package is automatically generated based on the 
Waylay Rules OpenAPI specification (API version: 6.20.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/rules.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-rules` sub-package contains the Rules api methods.
- The `waylay-sdk-rules-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-rules`.

## Requirements.
This package requires Python 3.10+.

## Installation

Normally this package is installed together with support for other services using the [waylay-sdk](https://pypi.org/project/waylay-sdk/) umbrella package:
* `pip install waylay-sdk` will install `waylay-sdk-rules` together with the SDK api packages for other services.
* `pip install waylay-sdk[types-rules]` will additionally install the types package `waylay-sdk-rules-types`.
* `pip install waylay-sdk[types]` will install the types packages for this and all other services.

Alternatively, you can install support for this _rules_ service only, installing or extending an existing [waylay-sdk-core](https://pypi.org/project/waylay-sdk-core/):

- `pip install waylay-sdk-rules` to only install api support for _rules_.
- `pip install waylay-sdk-rules[types]` to additionally install type support for _rules_.

## Usage

```python
# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.version_response import VersionResponse

try:
    # Get Service Information
    # calls `GET /rules/v1`
    api_response = await waylay_client.rules.about.get()
    print(f"Response: {api_response}")
except ApiError as e:
    print("Exception when calling rules.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/sdk/waylay-sdk/).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

SDK Path | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
**waylay_client.rules.about** | [**get**](docs/AboutApi.md#get) | **GET** /rules/v1 | Get Service Information
 | | |
**waylay_client.rules.plugs_execution** | [**execute_actuator**](docs/PlugsExecutionApi.md#execute_actuator) | **POST** /rules/v1/actions/{name} | Execute Latest Actuator Version
**waylay_client.rules.plugs_execution** | [**execute_actuator_version**](docs/PlugsExecutionApi.md#execute_actuator_version) | **POST** /rules/v1/actions/{name}/versions/{version} | Execute Specified Actuator Version
**waylay_client.rules.plugs_execution** | [**execute_sensor**](docs/PlugsExecutionApi.md#execute_sensor) | **POST** /rules/v1/sensors/{name} | Execute Latest Sensor Version
**waylay_client.rules.plugs_execution** | [**execute_sensor_version**](docs/PlugsExecutionApi.md#execute_sensor_version) | **POST** /rules/v1/sensors/{name}/versions/{version} | Execute Specified Sensor Version
**waylay_client.rules.plugs_execution** | [**execute_transformer**](docs/PlugsExecutionApi.md#execute_transformer) | **POST** /rules/v1/transformers/{name} | Execute Latest Transformer Version
**waylay_client.rules.plugs_execution** | [**execute_transformer_version**](docs/PlugsExecutionApi.md#execute_transformer_version) | **POST** /rules/v1/transformers/{name}/versions/{version} | Execute Specified Transformer Version
 | | |
**waylay_client.rules.push_data** | [**push**](docs/PushDataApi.md#push) | **POST** /rules/v1/data | Push Streaming Data
 | | |
**waylay_client.rules.task_nodes** | [**get_states**](docs/TaskNodesApi.md#get_states) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId}/states | Get Supported States
**waylay_client.rules.task_nodes** | [**get**](docs/TaskNodesApi.md#get) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Get Current States
**waylay_client.rules.task_nodes** | [**patch**](docs/TaskNodesApi.md#patch) | **PATCH** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Node State
**waylay_client.rules.task_nodes** | [**post**](docs/TaskNodesApi.md#post) | **POST** /rules/v1/tasks/callback | Finalize Asynchronous Execution With Token
**waylay_client.rules.task_nodes** | [**update**](docs/TaskNodesApi.md#update) | **POST** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Current State
 | | |
**waylay_client.rules.tasks** | [**create**](docs/TasksApi.md#create) | **POST** /rules/v1/tasks | Create Task
**waylay_client.rules.tasks** | [**delete**](docs/TasksApi.md#delete) | **DELETE** /rules/v1/tasks/{taskId} | Delete Task
**waylay_client.rules.tasks** | [**get_configuration**](docs/TasksApi.md#get_configuration) | **GET** /rules/v1/tasks/{taskId}/conf | Get Task Configuration
**waylay_client.rules.tasks** | [**get**](docs/TasksApi.md#get) | **GET** /rules/v1/tasks/{taskId} | Retrieve Task Details
**waylay_client.rules.tasks** | [**list**](docs/TasksApi.md#list) | **GET** /rules/v1/tasks | Query Multiple Tasks
**waylay_client.rules.tasks** | [**replace**](docs/TasksApi.md#replace) | **PUT** /rules/v1/tasks/{taskId} | Update Task
**waylay_client.rules.tasks** | [**start**](docs/TasksApi.md#start) | **POST** /rules/v1/tasks/{taskId}/command/start | Start Task
**waylay_client.rules.tasks** | [**stop**](docs/TasksApi.md#stop) | **POST** /rules/v1/tasks/{taskId}/command/stop | Stop Task
 | | |
**waylay_client.rules.tasks_batch_operations** | [**get**](docs/TasksBatchOperationsApi.md#get) | **GET** /rules/v1/batch/{batchId} | Get Tasks Batch Operation Status
**waylay_client.rules.tasks_batch_operations** | [**start**](docs/TasksBatchOperationsApi.md#start) | **POST** /rules/v1/batch | Start Batch Operations
 | | |
**waylay_client.rules.template_runs** | [**debug_graph**](docs/TemplateRunsApi.md#debug_graph) | **POST** /rules/v1/templates/debug | Debug Graph Or Bayesian Network
**waylay_client.rules.template_runs** | [**debug**](docs/TemplateRunsApi.md#debug) | **POST** /rules/v1/templates/{name}/debug | Debug Template
**waylay_client.rules.template_runs** | [**run_graph**](docs/TemplateRunsApi.md#run_graph) | **POST** /rules/v1/templates/run | Run Graph Or Bayesian Network
**waylay_client.rules.template_runs** | [**run**](docs/TemplateRunsApi.md#run) | **POST** /rules/v1/templates/{name}/run | Run Template
 | | |
**waylay_client.rules.templates** | [**copy**](docs/TemplatesApi.md#copy) | **PATCH** /rules/v1/templates/{name} | Copy Template
**waylay_client.rules.templates** | [**create**](docs/TemplatesApi.md#create) | **POST** /rules/v1/templates | Create Template
**waylay_client.rules.templates** | [**delete**](docs/TemplatesApi.md#delete) | **DELETE** /rules/v1/templates/{name} | Delete Template
**waylay_client.rules.templates** | [**get_discovery**](docs/TemplatesApi.md#get_discovery) | **GET** /rules/v1/discoveryTemplate | Retrieve Discovery Template
**waylay_client.rules.templates** | [**get**](docs/TemplatesApi.md#get) | **GET** /rules/v1/templates/{name} | Retrieve Template Details
**waylay_client.rules.templates** | [**list**](docs/TemplatesApi.md#list) | **GET** /rules/v1/templates | List Templates
**waylay_client.rules.templates** | [**replace**](docs/TemplatesApi.md#replace) | **PUT** /rules/v1/templates/{name} | Update Template
**waylay_client.rules.templates** | [**set**](docs/TemplatesApi.md#set) | **PUT** /rules/v1/discoveryTemplate | Set Discovery Template
**waylay_client.rules.templates** | [**upgrade_plugins**](docs/TemplatesApi.md#upgrade_plugins) | **PATCH** /rules/v1/templates | Upgrade Plugins


## Documentation For Models

 - [ActuatorExecutionResult](docs/ActuatorExecutionResult.md)
 - [ActuatorNode](docs/ActuatorNode.md)
 - [BatchIdQuery](docs/BatchIdQuery.md)
 - [BatchOperation](docs/BatchOperation.md)
 - [BatchOperationAction](docs/BatchOperationAction.md)
 - [BatchOperationEnqueued](docs/BatchOperationEnqueued.md)
 - [BatchOperationResult](docs/BatchOperationResult.md)
 - [BatchOperationResults](docs/BatchOperationResults.md)
 - [BatchOperationStatus](docs/BatchOperationStatus.md)
 - [BatchOperationSummary](docs/BatchOperationSummary.md)
 - [BatchQuery](docs/BatchQuery.md)
 - [BatchTask](docs/BatchTask.md)
 - [BatchTaskCommand](docs/BatchTaskCommand.md)
 - [BatchTaskCommandAction](docs/BatchTaskCommandAction.md)
 - [BatchTaskEntity](docs/BatchTaskEntity.md)
 - [BatchTaskQuery](docs/BatchTaskQuery.md)
 - [BatchTaskSpec](docs/BatchTaskSpec.md)
 - [BatchUpdatePlugin](docs/BatchUpdatePlugin.md)
 - [BatchUpdatePluginAction](docs/BatchUpdatePluginAction.md)
 - [BatchUpdateProperties](docs/BatchUpdateProperties.md)
 - [BatchUpdatePropertiesAction](docs/BatchUpdatePropertiesAction.md)
 - [BayesianGraph](docs/BayesianGraph.md)
 - [CronSchedule](docs/CronSchedule.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorWithDetailsResponse](docs/ErrorWithDetailsResponse.md)
 - [ExecutePlugsSpecification](docs/ExecutePlugsSpecification.md)
 - [ExecutionTrigger](docs/ExecutionTrigger.md)
 - [FailureOperationResultValue](docs/FailureOperationResultValue.md)
 - [GateType](docs/GateType.md)
 - [GenericTaskSettings](docs/GenericTaskSettings.md)
 - [GenericTrigger](docs/GenericTrigger.md)
 - [GraphDefinition](docs/GraphDefinition.md)
 - [GraphFormat](docs/GraphFormat.md)
 - [ListTasksTagsKey](docs/ListTasksTagsKey.md)
 - [LogEntry](docs/LogEntry.md)
 - [LogEntryLevel](docs/LogEntryLevel.md)
 - [LogLevel](docs/LogLevel.md)
 - [NodeStateSpecification](docs/NodeStateSpecification.md)
 - [NoteElement](docs/NoteElement.md)
 - [OneTimeTaskSetting](docs/OneTimeTaskSetting.md)
 - [OneTimeTaskSettingType](docs/OneTimeTaskSettingType.md)
 - [OperationResultObject](docs/OperationResultObject.md)
 - [PagingResult](docs/PagingResult.md)
 - [PeriodicTaskSetting](docs/PeriodicTaskSetting.md)
 - [PeriodicTaskSettingType](docs/PeriodicTaskSettingType.md)
 - [PluginUpdateSpec](docs/PluginUpdateSpec.md)
 - [PluginUpdateSpecAny](docs/PluginUpdateSpecAny.md)
 - [PluginUpdateSpecFromVersion](docs/PluginUpdateSpecFromVersion.md)
 - [PropertyUpdatesSpec](docs/PropertyUpdatesSpec.md)
 - [RRuleSchedule](docs/RRuleSchedule.md)
 - [ReactiveTaskSetting](docs/ReactiveTaskSetting.md)
 - [ReactiveTaskSettingType](docs/ReactiveTaskSettingType.md)
 - [RelationNode](docs/RelationNode.md)
 - [ResourceDataInjection](docs/ResourceDataInjection.md)
 - [RetryConfig](docs/RetryConfig.md)
 - [ScheduledTaskSetting](docs/ScheduledTaskSetting.md)
 - [ScheduledTaskSettingScheduled](docs/ScheduledTaskSettingScheduled.md)
 - [SensorExecutionResult](docs/SensorExecutionResult.md)
 - [SensorNode](docs/SensorNode.md)
 - [SimplifiedGraph](docs/SimplifiedGraph.md)
 - [StateChangeTrigger](docs/StateChangeTrigger.md)
 - [StatesTrigger](docs/StatesTrigger.md)
 - [StreamData](docs/StreamData.md)
 - [StreamDataPayload](docs/StreamDataPayload.md)
 - [SuccessOperationResultValue](docs/SuccessOperationResultValue.md)
 - [TaskCreated](docs/TaskCreated.md)
 - [TaskCreationSettings](docs/TaskCreationSettings.md)
 - [TaskDefaultsElement](docs/TaskDefaultsElement.md)
 - [TaskEntity](docs/TaskEntity.md)
 - [TaskEntityPagingResult](docs/TaskEntityPagingResult.md)
 - [TaskFromTemplate](docs/TaskFromTemplate.md)
 - [TaskHealth](docs/TaskHealth.md)
 - [TaskRuntimeInformation](docs/TaskRuntimeInformation.md)
 - [TaskScenarioType](docs/TaskScenarioType.md)
 - [TaskSettings](docs/TaskSettings.md)
 - [TaskSpecification](docs/TaskSpecification.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskTypeSettings](docs/TaskTypeSettings.md)
 - [TaskWithRule](docs/TaskWithRule.md)
 - [TaskWithRuntimeInfo](docs/TaskWithRuntimeInfo.md)
 - [TemplateCopied](docs/TemplateCopied.md)
 - [TemplateCreated](docs/TemplateCreated.md)
 - [TemplateDetails](docs/TemplateDetails.md)
 - [TemplateEntity](docs/TemplateEntity.md)
 - [TemplateEntityCommonAttributes](docs/TemplateEntityCommonAttributes.md)
 - [TemplateEntityMetadata](docs/TemplateEntityMetadata.md)
 - [TemplateListing](docs/TemplateListing.md)
 - [TemplateModification](docs/TemplateModification.md)
 - [TemplateModificationOperation](docs/TemplateModificationOperation.md)
 - [TemplatePluginsUpgraded](docs/TemplatePluginsUpgraded.md)
 - [TemplateRunActuatorResult](docs/TemplateRunActuatorResult.md)
 - [TemplateRunConfiguration](docs/TemplateRunConfiguration.md)
 - [TemplateRunInvocation](docs/TemplateRunInvocation.md)
 - [TemplateRunLogLevel](docs/TemplateRunLogLevel.md)
 - [TemplateRunSensorResult](docs/TemplateRunSensorResult.md)
 - [TemplateRunSpecification](docs/TemplateRunSpecification.md)
 - [TemplateRunWithGraphSpecification](docs/TemplateRunWithGraphSpecification.md)
 - [TemplateUpdated](docs/TemplateUpdated.md)
 - [TransformerExecutionResult](docs/TransformerExecutionResult.md)
 - [TriggerStateChange](docs/TriggerStateChange.md)
 - [TriggerType](docs/TriggerType.md)
 - [ValidationIssue](docs/ValidationIssue.md)
 - [ValidationIssueSeverity](docs/ValidationIssueSeverity.md)
 - [VariableDeclaration](docs/VariableDeclaration.md)
 - [VariableDeclarationDefaultValue](docs/VariableDeclarationDefaultValue.md)
 - [VariableFormat](docs/VariableFormat.md)
 - [VariableFormatValue](docs/VariableFormatValue.md)
 - [VariableType](docs/VariableType.md)
 - [VersionResponse](docs/VersionResponse.md)
 - [VersionResponseStatus](docs/VersionResponseStatus.md)

