# TaskRuntimeInformation


**Source:** `waylay.services.rules.models.task_runtime_information`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**type** | [**TaskScenarioType**](TaskScenarioType.md) |  | [optional] 
**reset_observations** | **bool** |  | [optional] 
**parallel** | **bool** |  | [optional] 
**gates_need_full_observation** | **bool** |  | [optional] 
**cron** | **str** | cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06) | [optional] 
**rrule** | **str** | RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3) | [optional] 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**frequency** | **int** | polling frequency in milliseconds | [optional] 
**finished_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 
**invocation_count** | **int** | Number of times the task has been invoked | [optional] 
**raw_data** | **object** | rawData of the task | [optional] 
**last_execution_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 
**health** | [**TaskHealth**](TaskHealth.md) |  | [optional] 
**pending_nodes** | **object** | returns the nodes that are pending to be resumed. Every key in the object is the node name. Can be multiple pending nodes in the task. | [optional] 


## Example

```python
from waylay.services.rules.models.task_runtime_information import TaskRuntimeInformation

task_runtime_information = TaskRuntimeInformation(
    tags=...,
    type=...,
    reset_observations=...,
    parallel=...,
    gates_need_full_observation=...,
    cron=...,
    rrule=...,
    time_zone=...,
    frequency=...,
    finished_time=...,
    invocation_count=...,
    raw_data=...,
    last_execution_time=...,
    health=...,
    pending_nodes=...,
)

# Create from JSON
task_runtime_information = TaskRuntimeInformation.from_json(
    '{ "tags": ..., "type": ..., "resetObservations": ..., "parallel": ..., "gatesNeedFullObservation": ..., "cron": ..., "rrule": ..., "timeZone": ..., "frequency": ..., "finishedTime": ..., "invocationCount": ..., "rawData": ..., "lastExecutionTime": ..., "health": ..., "pendingNodes": ... }'
)

# Export to dictionary
task_runtime_information_dict = task_runtime_information.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


