# TaskRuntimeInformationAllOfHealth

Health of the task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors_count** | **int** | Number of errors during last 64 task invocations | 
**errors_rate** | **float** | Error rate during last 64 task invocations. 0.0 means no errors, 1.0 means all errors | 

## Example

```python
from waylay.services.rules.models.task_runtime_information_all_of_health import TaskRuntimeInformationAllOfHealth

# TODO update the JSON string below
json = "{}"
# create an instance of TaskRuntimeInformationAllOfHealth from a JSON string
task_runtime_information_all_of_health_instance = TaskRuntimeInformationAllOfHealth.from_json(json)
# print the JSON string representation of the object
print TaskRuntimeInformationAllOfHealth.to_json()

# convert the object into a dict
task_runtime_information_all_of_health_dict = task_runtime_information_all_of_health_instance.to_dict()
# create an instance of TaskRuntimeInformationAllOfHealth from a dict
task_runtime_information_all_of_health_form_dict = task_runtime_information_all_of_health.from_dict(task_runtime_information_all_of_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


