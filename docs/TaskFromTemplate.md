# TaskFromTemplate


**Source:** `waylay.services.rules.models.task_from_template`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]
**gates_need_full_observation** | **bool** |  | [optional] [default to False]
**protected** | **bool** |  | [optional] [default to False]
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**variables** | **object** | set of variables which will be used when starting a task and will automatically be injected in the template before starting a task. | [optional] 
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**rrule** | **str** | RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3) | 
**cron** | **str** | cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06) | 
**frequency** | **int** | polling frequency in milliseconds | 
**start** | **bool** |  | [optional] [default to True]
**template** | **str** | Unique template identifier | 


## Example

```python
from waylay.services.rules.models.task_from_template import TaskFromTemplate

task_from_template = TaskFromTemplate(
    name=...,
    resource=...,
    reset_observations=...,
    parallel=...,
    gates_need_full_observation=...,
    protected=...,
    tags=...,
    variables=...,
    type=...,
    time_zone=...,
    rrule=...,
    cron=...,
    frequency=...,
    start=...,
    template=...,
)

# Create from JSON
task_from_template = TaskFromTemplate.from_json(
    '{ "name": ..., "resource": ..., "resetObservations": ..., "parallel": ..., "gatesNeedFullObservation": ..., "protected": ..., "tags": ..., "variables": ..., "type": ..., "timeZone": ..., "rrule": ..., "cron": ..., "frequency": ..., "start": ..., "template": ... }'
)

# Export to dictionary
task_from_template_dict = task_from_template.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


