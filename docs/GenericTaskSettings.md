# GenericTaskSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]
**gates_need_full_observation** | **bool** |  | [optional] [default to False]
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**variables** | **object** | set of variables which will be used when starting a task and will automatically be injected in the template before starting a task. | [optional] 

## Example

```python
from waylay.services.rules.models.generic_task_settings import GenericTaskSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GenericTaskSettings from a JSON string
generic_task_settings_instance = GenericTaskSettings.from_json(json)
# print the JSON string representation of the object
print GenericTaskSettings.to_json()

# convert the object into a dict
generic_task_settings_dict = generic_task_settings_instance.to_dict()
# create an instance of GenericTaskSettings from a dict
generic_task_settings_form_dict = generic_task_settings.from_dict(generic_task_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


