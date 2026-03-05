# TaskHealth

Health of the task

**Source:** `waylay.services.rules.models.task_health`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors_count** | **int** | Number of errors during last 64 task invocations | 
**errors_rate** | **float** | Error rate during last 64 task invocations. 0.0 means no errors, 1.0 means all errors | 


## Example

```python
from waylay.services.rules.models.task_health import TaskHealth

task_health = TaskHealth(errors_count=..., errors_rate=...)

# Create from JSON
task_health = TaskHealth.from_json('{ "errorsCount": ..., "errorsRate": ... }')

# Export to dictionary
task_health_dict = task_health.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


