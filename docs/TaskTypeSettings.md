# TaskTypeSettings


**Source:** `waylay.services.rules.models.task_type_settings`



## Union Type (One Of)

This type allows one of the following:

Type | Description
------------ | -------------
[**ScheduledTaskSetting**](ScheduledTaskSetting.md) | -
[**PeriodicTaskSetting**](PeriodicTaskSetting.md) | -
[**OneTimeTaskSetting**](OneTimeTaskSetting.md) | -
[**ReactiveTaskSetting**](ReactiveTaskSetting.md) | -

## Example

```python
from waylay.services.rules.models.task_type_settings import TaskTypeSettings

# Use any of the accepted types (see table above)
my_task_type_settings: TaskTypeSettings = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


