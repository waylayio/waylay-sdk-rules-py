# OperationResultObject

Finished Batch Operation results

**Source:** `waylay.services.rules.models.operation_result_object`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**results** | [**BatchOperationResults**](BatchOperationResults.md) |  | 


## Example

```python
from waylay.services.rules.models.operation_result_object import OperationResultObject

operation_result_object = OperationResultObject(finished_time=..., results=...)

# Create from JSON
operation_result_object = OperationResultObject.from_json(
    '{ "finishedTime": ..., "results": ... }'
)

# Export to dictionary
operation_result_object_dict = operation_result_object.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


