# TaskCreated


**Source:** `waylay.services.rules.models.task_created`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique task identifier | 
**warnings** | [**List[ValidationIssue]**](ValidationIssue.md) | List of task warning issues. Will only be there if query parameter &#x60;returnWarnings&#x60; was set to &#x60;true&#x60; | [optional] 


## Example

```python
from waylay.services.rules.models.task_created import TaskCreated

task_created = TaskCreated(id=..., warnings=...)

# Create from JSON
task_created = TaskCreated.from_json('{ "ID": ..., "warnings": ... }')

# Export to dictionary
task_created_dict = task_created.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


