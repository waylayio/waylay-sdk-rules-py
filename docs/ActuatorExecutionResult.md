# ActuatorExecutionResult


**Source:** `waylay.services.rules.models.actuator_execution_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the actuator was successfully executed | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**raw_data** | **object** |  | [optional] 
**log** | **List[object]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.actuator_execution_result import (
    ActuatorExecutionResult,
)

actuator_execution_result = ActuatorExecutionResult(
    result=..., error=..., raw_data=..., log=...
)

# Create from JSON
actuator_execution_result = ActuatorExecutionResult.from_json(
    '{ "result": ..., "error": ..., "rawData": ..., "log": ... }'
)

# Export to dictionary
actuator_execution_result_dict = actuator_execution_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


