# TaskEntityPagingResultAllOfValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique task identifier | 
**name** | **str** |  | 
**status** | [**TaskStatus**](TaskStatus.md) |  | 
**user** | **str** | Creation user mail address or &#39;system&#39; for system generated tasks | 
**create_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**template** | **str** | Unique template identifier | [optional] 
**network** | **object** | The graph, either from the template or from the task definition. Depending on the &#x60;format&#x60; query parameter either BN or simplified format | 
**resource_ids** | **List[str]** | List of resources that are used in the task | [optional] 
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
**health** | [**TaskRuntimeInformationAllOfHealth**](TaskRuntimeInformationAllOfHealth.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.task_entity_paging_result_all_of_values import TaskEntityPagingResultAllOfValues

# TODO update the JSON string below
json = "{}"
# create an instance of TaskEntityPagingResultAllOfValues from a JSON string
task_entity_paging_result_all_of_values_instance = TaskEntityPagingResultAllOfValues.from_json(json)
# print the JSON string representation of the object
print TaskEntityPagingResultAllOfValues.to_json()

# convert the object into a dict
task_entity_paging_result_all_of_values_dict = task_entity_paging_result_all_of_values_instance.to_dict()
# create an instance of TaskEntityPagingResultAllOfValues from a dict
task_entity_paging_result_all_of_values_form_dict = task_entity_paging_result_all_of_values.from_dict(task_entity_paging_result_all_of_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


