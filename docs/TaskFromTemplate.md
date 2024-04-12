# TaskFromTemplate


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
**template** | **str** | Unique template identifier | 

## Example

```python
from waylay.services.rules.models.task_from_template import TaskFromTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFromTemplate from a JSON string
task_from_template_instance = TaskFromTemplate.from_json(json)
# print the JSON string representation of the object
print TaskFromTemplate.to_json()

# convert the object into a dict
task_from_template_dict = task_from_template_instance.to_dict()
# create an instance of TaskFromTemplate from a dict
task_from_template_form_dict = task_from_template.from_dict(task_from_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


