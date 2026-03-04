# PeriodicTaskSetting


**Source:** `waylay.services.rules.models.periodic_task_setting`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PeriodicTaskSettingType**](PeriodicTaskSettingType.md) |  | 
**frequency** | **int** | polling frequency in milliseconds | 


## Example

```python
from waylay.services.rules.models.periodic_task_setting import PeriodicTaskSetting

periodic_task_setting = PeriodicTaskSetting(type=..., frequency=...)

# Create from JSON
periodic_task_setting = PeriodicTaskSetting.from_json(
    '{ "type": ..., "frequency": ... }'
)

# Export to dictionary
periodic_task_setting_dict = periodic_task_setting.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


