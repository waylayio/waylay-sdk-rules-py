# ReactiveTaskSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 

## Example

```python
from waylay.services.rules.models.reactive_task_setting import ReactiveTaskSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ReactiveTaskSetting from a JSON string
reactive_task_setting_instance = ReactiveTaskSetting.from_json(json)
# print the JSON string representation of the object
print ReactiveTaskSetting.to_json()

# convert the object into a dict
reactive_task_setting_dict = reactive_task_setting_instance.to_dict()
# create an instance of ReactiveTaskSetting from a dict
reactive_task_setting_form_dict = reactive_task_setting.from_dict(reactive_task_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


