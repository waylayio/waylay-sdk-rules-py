# ScheduledTaskSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScheduledTaskSettingAllOfType**](ScheduledTaskSettingAllOfType.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 

## Example

```python
from waylay.services.rules.models.scheduled_task_setting import ScheduledTaskSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskSetting from a JSON string
scheduled_task_setting_instance = ScheduledTaskSetting.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskSetting.to_json()

# convert the object into a dict
scheduled_task_setting_dict = scheduled_task_setting_instance.to_dict()
# create an instance of ScheduledTaskSetting from a dict
scheduled_task_setting_form_dict = scheduled_task_setting.from_dict(scheduled_task_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


