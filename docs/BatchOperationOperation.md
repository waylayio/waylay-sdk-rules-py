# BatchOperationOperation

Summary of the batch operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchOperationOperationAction**](BatchOperationOperationAction.md) |  | 
**description** | **str** | description of the operations | 

## Example

```python
from waylay.services.rules.models.batch_operation_operation import BatchOperationOperation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationOperation from a JSON string
batch_operation_operation_instance = BatchOperationOperation.from_json(json)
# print the JSON string representation of the object
print BatchOperationOperation.to_json()

# convert the object into a dict
batch_operation_operation_dict = batch_operation_operation_instance.to_dict()
# create an instance of BatchOperationOperation from a dict
batch_operation_operation_form_dict = batch_operation_operation.from_dict(batch_operation_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


