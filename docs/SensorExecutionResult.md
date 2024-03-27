# SensorExecutionResult


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

# TODO update the JSON string below
json = "{}"
# create an instance of SensorExecutionResult from a JSON string
sensor_execution_result_instance = SensorExecutionResult.from_json(json)
# print the JSON string representation of the object
print SensorExecutionResult.to_json()

# convert the object into a dict
sensor_execution_result_dict = sensor_execution_result_instance.to_dict()
# create an instance of SensorExecutionResult from a dict
sensor_execution_result_form_dict = sensor_execution_result.from_dict(sensor_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


