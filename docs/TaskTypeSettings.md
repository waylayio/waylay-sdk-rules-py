# TaskTypeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**frequency** | **int** | polling frequency in milliseconds | [optional] 

## Example

```python
from waylay.services.rules.models.task_type_settings import TaskTypeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTypeSettings from a JSON string
task_type_settings_instance = TaskTypeSettings.from_json(json)
# print the JSON string representation of the object
print TaskTypeSettings.to_json()

# convert the object into a dict
task_type_settings_dict = task_type_settings_instance.to_dict()
# create an instance of TaskTypeSettings from a dict
task_type_settings_form_dict = task_type_settings.from_dict(task_type_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


