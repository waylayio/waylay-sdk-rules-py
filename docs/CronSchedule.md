# CronSchedule


**Source:** `waylay.services.rules.models.cron_schedule`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **str** | cron expression as defined in [Cron format](https://www.quartz-scheduler.org/documentation/quartz-1.8.6/tutorials/TutorialLesson06) | 


## Example

```python
from waylay.services.rules.models.cron_schedule import CronSchedule

cron_schedule = CronSchedule(cron=...)

# Create from JSON
cron_schedule = CronSchedule.from_json('{ "cron": ... }')

# Export to dictionary
cron_schedule_dict = cron_schedule.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


