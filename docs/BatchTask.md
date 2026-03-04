# BatchTask


**Source:** `waylay.services.rules.models.batch_task`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | [optional] 
**action** | **str** |  | [optional] 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | [optional] 


## Example

```python
from waylay.services.rules.models.batch_task import BatchTask

batch_task = BatchTask(entity=..., action=..., query=...)

# Create from JSON
batch_task = BatchTask.from_json('{ "entity": ..., "action": ..., "query": ... }')

# Export to dictionary
batch_task_dict = batch_task.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


