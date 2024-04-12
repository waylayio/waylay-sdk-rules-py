# PeriodicTaskSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PeriodicTaskSettingType**](PeriodicTaskSettingType.md) |  | 
**frequency** | **int** | polling frequency in milliseconds | 

## Example

```python
from waylay.services.rules.models.periodic_task_setting import PeriodicTaskSetting

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodicTaskSetting from a JSON string
periodic_task_setting_instance = PeriodicTaskSetting.from_json(json)
# print the JSON string representation of the object
print PeriodicTaskSetting.to_json()

# convert the object into a dict
periodic_task_setting_dict = periodic_task_setting_instance.to_dict()
# create an instance of PeriodicTaskSetting from a dict
periodic_task_setting_form_dict = periodic_task_setting.from_dict(periodic_task_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


