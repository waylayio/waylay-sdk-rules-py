# BatchTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | [optional] 
**action** | **str** |  | [optional] 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.batch_task import BatchTask

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTask from a JSON string
batch_task_instance = BatchTask.from_json(json)
# print the JSON string representation of the object
print BatchTask.to_json()

# convert the object into a dict
batch_task_dict = batch_task_instance.to_dict()
# create an instance of BatchTask from a dict
batch_task_form_dict = batch_task.from_dict(batch_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


