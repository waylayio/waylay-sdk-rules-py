# OneTimeTaskSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OneTimeTaskSettingType**](OneTimeTaskSettingType.md) |  | 

## Example

```python
from waylay.services.rules.models.one_time_task_setting import OneTimeTaskSetting

# TODO update the JSON string below
json = "{}"
# create an instance of OneTimeTaskSetting from a JSON string
one_time_task_setting_instance = OneTimeTaskSetting.from_json(json)
# print the JSON string representation of the object
print OneTimeTaskSetting.to_json()

# convert the object into a dict
one_time_task_setting_dict = one_time_task_setting_instance.to_dict()
# create an instance of OneTimeTaskSetting from a dict
one_time_task_setting_form_dict = one_time_task_setting.from_dict(one_time_task_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


