# TransformerExecutionResult


**Source:** `waylay.services.rules.models.transformer_execution_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the actuator was Successfully Executed | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**data** | **object** |  | [optional] 
**log** | **List[object]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.transformer_execution_result import (
    TransformerExecutionResult,
)

transformer_execution_result = TransformerExecutionResult(
    result=..., error=..., data=..., log=...
)

# Create from JSON
transformer_execution_result = TransformerExecutionResult.from_json(
    '{ "result": ..., "error": ..., "data": ..., "log": ... }'
)

# Export to dictionary
transformer_execution_result_dict = transformer_execution_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


