# BatchTaskCommand

Execute command on multiple task

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchTaskCommandAllOfAction**](BatchTaskCommandAllOfAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 

## Example

```python
from waylay.services.rules.models.batch_task_command import BatchTaskCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTaskCommand from a JSON string
batch_task_command_instance = BatchTaskCommand.from_json(json)
# print the JSON string representation of the object
print BatchTaskCommand.to_json()

# convert the object into a dict
batch_task_command_dict = batch_task_command_instance.to_dict()
# create an instance of BatchTaskCommand from a dict
batch_task_command_form_dict = batch_task_command.from_dict(batch_task_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


