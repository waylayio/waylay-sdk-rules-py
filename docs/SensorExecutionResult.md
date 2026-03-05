# SensorExecutionResult


**Source:** `waylay.services.rules.models.sensor_execution_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the sensor was successfully executed | [optional] 
**state** | **str** | observedState field returned by the sensor execution | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**raw_data** | **object** | the rawData returned by the sensor execution | [optional] 
**log** | **List[object]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.sensor_execution_result import SensorExecutionResult

sensor_execution_result = SensorExecutionResult(
    result=..., state=..., error=..., raw_data=..., log=...
)

# Create from JSON
sensor_execution_result = SensorExecutionResult.from_json(
    '{ "result": ..., "state": ..., "error": ..., "rawData": ..., "log": ... }'
)

# Export to dictionary
sensor_execution_result_dict = sensor_execution_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


