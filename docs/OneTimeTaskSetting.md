# OneTimeTaskSetting


**Source:** `waylay.services.rules.models.one_time_task_setting`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**OneTimeTaskSettingType**](OneTimeTaskSettingType.md) |  | 


## Example

```python
from waylay.services.rules.models.one_time_task_setting import OneTimeTaskSetting

one_time_task_setting = OneTimeTaskSetting(type=...)

# Create from JSON
one_time_task_setting = OneTimeTaskSetting.from_json('{ "type": ... }')

# Export to dictionary
one_time_task_setting_dict = one_time_task_setting.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


