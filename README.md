# Waylay Rules Service
The REST api to manage rule tasks and rule templates in the Waylay platform.

This Python package is automatically generated based on the 
Waylay Rules OpenAPI specification (API version: 6.5.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/rules.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-rules` sub-package contains the Rules api methods.
- The `waylay-sdk-rules-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-rules`.

## Requirements.
This package requires Python 3.9+.

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
from pprint import pprint

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
    api_response = await waylay_client.rules.about.get(
    )
    print("The response of rules.about.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**get**](docs/AboutApi.md#get) | **GET** /rules/v1 | Get Service Information
*PlugsExecutionApi* | [**execute_actuator**](docs/PlugsExecutionApi.md#execute_actuator) | **POST** /rules/v1/actions/{name} | Execute Latest Actuator Version
*PlugsExecutionApi* | [**execute_actuator_version**](docs/PlugsExecutionApi.md#execute_actuator_version) | **POST** /rules/v1/actions/{name}/versions/{version} | Execute Specified Actuator Version
*PlugsExecutionApi* | [**execute_sensor**](docs/PlugsExecutionApi.md#execute_sensor) | **POST** /rules/v1/sensors/{name} | Execute Latest Sensor Version
*PlugsExecutionApi* | [**execute_sensor_version**](docs/PlugsExecutionApi.md#execute_sensor_version) | **POST** /rules/v1/sensors/{name}/versions/{version} | Execute Specified Sensor Version
*PlugsExecutionApi* | [**execute_transformer**](docs/PlugsExecutionApi.md#execute_transformer) | **POST** /rules/v1/transformers/{name} | Execute Latest Transformer Version
*PlugsExecutionApi* | [**execute_transformer_version**](docs/PlugsExecutionApi.md#execute_transformer_version) | **POST** /rules/v1/transformers/{name}/versions/{version} | Execute Specified Transformer Version
*PushDataApi* | [**push**](docs/PushDataApi.md#push) | **POST** /rules/v1/data | Push Streaming Data
*TaskNodesApi* | [**get_states**](docs/TaskNodesApi.md#get_states) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId}/states | Get Supported States
*TaskNodesApi* | [**get**](docs/TaskNodesApi.md#get) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Get Current States
*TaskNodesApi* | [**patch**](docs/TaskNodesApi.md#patch) | **PATCH** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Node State
*TaskNodesApi* | [**update**](docs/TaskNodesApi.md#update) | **POST** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Current State
*TasksApi* | [**create**](docs/TasksApi.md#create) | **POST** /rules/v1/tasks | Create Task
*TasksApi* | [**delete**](docs/TasksApi.md#delete) | **DELETE** /rules/v1/tasks/{taskId} | Delete Task
*TasksApi* | [**get_configuration**](docs/TasksApi.md#get_configuration) | **GET** /rules/v1/tasks/{taskId}/conf | Get Task Configuration
*TasksApi* | [**get**](docs/TasksApi.md#get) | **GET** /rules/v1/tasks/{taskId} | Retrieve Task Details
*TasksApi* | [**list**](docs/TasksApi.md#list) | **GET** /rules/v1/tasks | Query Multiple Tasks
*TasksApi* | [**replace**](docs/TasksApi.md#replace) | **PUT** /rules/v1/tasks/{taskId} | Update Task
*TasksApi* | [**start**](docs/TasksApi.md#start) | **POST** /rules/v1/tasks/{taskId}/command/start | Start Task
*TasksApi* | [**stop**](docs/TasksApi.md#stop) | **POST** /rules/v1/tasks/{taskId}/command/stop | Stop Task
*TasksBatchOperationsApi* | [**get**](docs/TasksBatchOperationsApi.md#get) | **GET** /rules/v1/batch/{batchId} | Get Tasks Batch Operation Status
*TasksBatchOperationsApi* | [**start**](docs/TasksBatchOperationsApi.md#start) | **POST** /rules/v1/batch | Start Batch Operations
*TemplateRunsApi* | [**run_graph**](docs/TemplateRunsApi.md#run_graph) | **POST** /rules/v1/templates/run | Run Graph Or Bayesian Network
*TemplateRunsApi* | [**run**](docs/TemplateRunsApi.md#run) | **POST** /rules/v1/templates/{name}/run | Run Template
*TemplatesApi* | [**create**](docs/TemplatesApi.md#create) | **POST** /rules/v1/templates | Create Template
*TemplatesApi* | [**delete**](docs/TemplatesApi.md#delete) | **DELETE** /rules/v1/templates/{name} | Delete Template
*TemplatesApi* | [**get_discovery**](docs/TemplatesApi.md#get_discovery) | **GET** /rules/v1/discoveryTemplate | Retrieve Discovery Template
*TemplatesApi* | [**get**](docs/TemplatesApi.md#get) | **GET** /rules/v1/templates/{name} | Retrieve Template Details
*TemplatesApi* | [**list**](docs/TemplatesApi.md#list) | **GET** /rules/v1/templates | List Templates
*TemplatesApi* | [**replace**](docs/TemplatesApi.md#replace) | **PUT** /rules/v1/templates/{name} | Update Template
*TemplatesApi* | [**set**](docs/TemplatesApi.md#set) | **PUT** /rules/v1/discoveryTemplate | Set Discovery Template
*TemplatesApi* | [**upgrade_plugins**](docs/TemplatesApi.md#upgrade_plugins) | **PATCH** /rules/v1/templates | Upgrade Plugins


## Documentation For Models

 - [ATasksBatchOperationSpecification](docs/ATasksBatchOperationSpecification.md)
 - [ActuatorExecutionResult](docs/ActuatorExecutionResult.md)
 - [ActuatorNode](docs/ActuatorNode.md)
 - [BatchIdQuery](docs/BatchIdQuery.md)
 - [BatchOperation](docs/BatchOperation.md)
 - [BatchOperationEnqueued](docs/BatchOperationEnqueued.md)
 - [BatchOperationOperation](docs/BatchOperationOperation.md)
 - [BatchOperationOperationAction](docs/BatchOperationOperationAction.md)
 - [BatchOperationResult](docs/BatchOperationResult.md)
 - [BatchQuery](docs/BatchQuery.md)
 - [BatchTask](docs/BatchTask.md)
 - [BatchTaskCommand](docs/BatchTaskCommand.md)
 - [BatchTaskCommandAllOfAction](docs/BatchTaskCommandAllOfAction.md)
 - [BatchTaskEntity](docs/BatchTaskEntity.md)
 - [BatchTaskQuery](docs/BatchTaskQuery.md)
 - [BatchUpdatePlugin](docs/BatchUpdatePlugin.md)
 - [BatchUpdateProperties](docs/BatchUpdateProperties.md)
 - [BatchUpdatePropertiesAllOfAction](docs/BatchUpdatePropertiesAllOfAction.md)
 - [BayesianGraph](docs/BayesianGraph.md)
 - [CreateTask201Response](docs/CreateTask201Response.md)
 - [CreateTemplate201Response](docs/CreateTemplate201Response.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorWithDetailsResponse](docs/ErrorWithDetailsResponse.md)
 - [ExecutePlugsSpecification](docs/ExecutePlugsSpecification.md)
 - [ExecutionTrigger](docs/ExecutionTrigger.md)
 - [FailureOperationResultValue](docs/FailureOperationResultValue.md)
 - [GateType](docs/GateType.md)
 - [GenericTaskSettings](docs/GenericTaskSettings.md)
 - [GenericTrigger](docs/GenericTrigger.md)
 - [GetBatchOperation200Response](docs/GetBatchOperation200Response.md)
 - [GraphDefinition](docs/GraphDefinition.md)
 - [ListTasksFormatParameter](docs/ListTasksFormatParameter.md)
 - [ListTasksTagsKeyParameter](docs/ListTasksTagsKeyParameter.md)
 - [LogLevel](docs/LogLevel.md)
 - [LogsInner](docs/LogsInner.md)
 - [LogsInnerLevel](docs/LogsInnerLevel.md)
 - [NodeStateSpecification](docs/NodeStateSpecification.md)
 - [NoteElement](docs/NoteElement.md)
 - [OneTimeTaskSetting](docs/OneTimeTaskSetting.md)
 - [OneTimeTaskSettingType](docs/OneTimeTaskSettingType.md)
 - [OperationResultObject](docs/OperationResultObject.md)
 - [OperationResultObjectResults](docs/OperationResultObjectResults.md)
 - [PagingResult](docs/PagingResult.md)
 - [PeriodicTaskSetting](docs/PeriodicTaskSetting.md)
 - [PeriodicTaskSettingType](docs/PeriodicTaskSettingType.md)
 - [PluginUpdateSpec](docs/PluginUpdateSpec.md)
 - [PluginUpdateSpecFromVersion](docs/PluginUpdateSpecFromVersion.md)
 - [PluginUpdateSpecFromVersionOneOf](docs/PluginUpdateSpecFromVersionOneOf.md)
 - [PossibleValuesEnumDeclarationInner](docs/PossibleValuesEnumDeclarationInner.md)
 - [PropertyUpdatesSpec](docs/PropertyUpdatesSpec.md)
 - [ReactiveTaskSetting](docs/ReactiveTaskSetting.md)
 - [ReactiveTaskSettingType](docs/ReactiveTaskSettingType.md)
 - [RelationNode](docs/RelationNode.md)
 - [ReplaceTemplate200Response](docs/ReplaceTemplate200Response.md)
 - [ResourceDataInjection](docs/ResourceDataInjection.md)
 - [RetryConfig](docs/RetryConfig.md)
 - [RunTemplateLogLevelParameter](docs/RunTemplateLogLevelParameter.md)
 - [ScheduledTaskSetting](docs/ScheduledTaskSetting.md)
 - [ScheduledTaskSettingAllOfType](docs/ScheduledTaskSettingAllOfType.md)
 - [SensorExecutionResult](docs/SensorExecutionResult.md)
 - [SensorNode](docs/SensorNode.md)
 - [SimplifiedGraph](docs/SimplifiedGraph.md)
 - [SimplifiedGraphTriggersInner](docs/SimplifiedGraphTriggersInner.md)
 - [StateChangeTrigger](docs/StateChangeTrigger.md)
 - [StatesTrigger](docs/StatesTrigger.md)
 - [StreamData](docs/StreamData.md)
 - [StreamDataData](docs/StreamDataData.md)
 - [SuccessOperationResultValue](docs/SuccessOperationResultValue.md)
 - [TaskDefaultsElement](docs/TaskDefaultsElement.md)
 - [TaskEntity](docs/TaskEntity.md)
 - [TaskEntityPagingResult](docs/TaskEntityPagingResult.md)
 - [TaskFromTemplate](docs/TaskFromTemplate.md)
 - [TaskScenarioType](docs/TaskScenarioType.md)
 - [TaskSettings](docs/TaskSettings.md)
 - [TaskSpecification](docs/TaskSpecification.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskTypeSettings](docs/TaskTypeSettings.md)
 - [TaskWithRule](docs/TaskWithRule.md)
 - [TaskWithRuleAllOfTask](docs/TaskWithRuleAllOfTask.md)
 - [TemplateDetails](docs/TemplateDetails.md)
 - [TemplateEntity](docs/TemplateEntity.md)
 - [TemplateEntityCommonAttributes](docs/TemplateEntityCommonAttributes.md)
 - [TemplateEntityMetadata](docs/TemplateEntityMetadata.md)
 - [TemplateModification](docs/TemplateModification.md)
 - [TemplateModificationOperation](docs/TemplateModificationOperation.md)
 - [TemplateRunActuatorResult](docs/TemplateRunActuatorResult.md)
 - [TemplateRunConfiguration](docs/TemplateRunConfiguration.md)
 - [TemplateRunInvocation](docs/TemplateRunInvocation.md)
 - [TemplateRunSensorResult](docs/TemplateRunSensorResult.md)
 - [TemplateRunSpecification](docs/TemplateRunSpecification.md)
 - [TemplateRunWithGraphSpecification](docs/TemplateRunWithGraphSpecification.md)
 - [TransformerExecutionResult](docs/TransformerExecutionResult.md)
 - [TriggerStateChange](docs/TriggerStateChange.md)
 - [UpgradePluginsTemplates200Response](docs/UpgradePluginsTemplates200Response.md)
 - [ValidationIssue](docs/ValidationIssue.md)
 - [ValidationIssueSeverity](docs/ValidationIssueSeverity.md)
 - [VariableDeclaration](docs/VariableDeclaration.md)
 - [VariableDeclarationDefaultValue](docs/VariableDeclarationDefaultValue.md)
 - [VariableFormat](docs/VariableFormat.md)
 - [VariableType](docs/VariableType.md)
 - [VersionResponse](docs/VersionResponse.md)
 - [VersionResponseStatus](docs/VersionResponseStatus.md)

