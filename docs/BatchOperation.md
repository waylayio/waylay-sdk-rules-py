# BatchOperation


**Source:** `waylay.services.rules.models.batch_operation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationSummary**](BatchOperationSummary.md) |  | 
**queue_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 


## Example

```python
from waylay.services.rules.models.batch_operation import BatchOperation

batch_operation = BatchOperation(id=..., user=..., operation=..., queue_time=...)

# Create from JSON
batch_operation = BatchOperation.from_json(
    '{ "id": ..., "user": ..., "operation": ..., "queueTime": ... }'
)

# Export to dictionary
batch_operation_dict = batch_operation.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


