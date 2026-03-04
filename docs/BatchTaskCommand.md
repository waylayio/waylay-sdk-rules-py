# BatchTaskCommand

Execute command on multiple task

**Source:** `waylay.services.rules.models.batch_task_command`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchTaskCommandAction**](BatchTaskCommandAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 


## Example

```python
from waylay.services.rules.models.batch_task_command import BatchTaskCommand

batch_task_command = BatchTaskCommand(entity=..., action=..., query=...)

# Create from JSON
batch_task_command = BatchTaskCommand.from_json(
    '{ "entity": ..., "action": ..., "query": ... }'
)

# Export to dictionary
batch_task_command_dict = batch_task_command.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


