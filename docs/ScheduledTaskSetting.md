# ScheduledTaskSetting


**Source:** `waylay.services.rules.models.scheduled_task_setting`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScheduledTaskSettingScheduled**](ScheduledTaskSettingScheduled.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**rrule** | **str** | RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3) | 
**cron** | **str** | cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06) | 


## Example

```python
from waylay.services.rules.models.scheduled_task_setting import ScheduledTaskSetting

scheduled_task_setting = ScheduledTaskSetting(
    type=..., time_zone=..., rrule=..., cron=...
)

# Create from JSON
scheduled_task_setting = ScheduledTaskSetting.from_json(
    '{ "type": ..., "timeZone": ..., "rrule": ..., "cron": ... }'
)

# Export to dictionary
scheduled_task_setting_dict = scheduled_task_setting.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


