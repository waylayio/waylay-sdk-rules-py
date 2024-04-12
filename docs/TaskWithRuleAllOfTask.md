# TaskWithRuleAllOfTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]
**gates_need_full_observation** | **bool** |  | [optional] [default to False]
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**variables** | **object** | set of variables which will be used when starting a task and will automatically be injected in the template before starting a task. | [optional] 
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**frequency** | **int** | polling frequency in milliseconds | 
**start** | **bool** |  | [optional] [default to True]

## Example

```python
from waylay.services.rules.models.task_with_rule_all_of_task import TaskWithRuleAllOfTask

# TODO update the JSON string below
json = "{}"
# create an instance of TaskWithRuleAllOfTask from a JSON string
task_with_rule_all_of_task_instance = TaskWithRuleAllOfTask.from_json(json)
# print the JSON string representation of the object
print TaskWithRuleAllOfTask.to_json()

# convert the object into a dict
task_with_rule_all_of_task_dict = task_with_rule_all_of_task_instance.to_dict()
# create an instance of TaskWithRuleAllOfTask from a dict
task_with_rule_all_of_task_form_dict = task_with_rule_all_of_task.from_dict(task_with_rule_all_of_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


