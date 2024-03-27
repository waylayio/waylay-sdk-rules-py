# BatchOperationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationOperation**](BatchOperationOperation.md) |  | 
**queue_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**finished_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**results** | [**OperationResultObjectResults**](OperationResultObjectResults.md) |  | 

## Example

```python
from waylay.services.rules.models.batch_operation_result import BatchOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchOperationResult from a JSON string
batch_operation_result_instance = BatchOperationResult.from_json(json)
# print the JSON string representation of the object
print BatchOperationResult.to_json()

# convert the object into a dict
batch_operation_result_dict = batch_operation_result_instance.to_dict()
# create an instance of BatchOperationResult from a dict
batch_operation_result_form_dict = batch_operation_result.from_dict(batch_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


