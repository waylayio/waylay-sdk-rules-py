# ReactiveTaskSetting


**Source:** `waylay.services.rules.models.reactive_task_setting`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 


## Example

```python
from waylay.services.rules.models.reactive_task_setting import ReactiveTaskSetting

reactive_task_setting = ReactiveTaskSetting(type=...)

# Create from JSON
reactive_task_setting = ReactiveTaskSetting.from_json('{ "type": ... }')

# Export to dictionary
reactive_task_setting_dict = reactive_task_setting.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


