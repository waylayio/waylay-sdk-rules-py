# TemplateRunSensorResult


**Source:** `waylay.services.rules.models.template_run_sensor_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the sensor was successfully executed | [optional] 
**state** | **str** | observedState field returned by the sensor execution | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**raw_data** | **object** | the rawData returned by the sensor execution | [optional] 
**log** | **List[object]** |  | [optional] 
**executed** | **bool** | flag indicating if the sensor was executed | 


## Example

```python
from waylay.services.rules.models.template_run_sensor_result import (
    TemplateRunSensorResult,
)

template_run_sensor_result = TemplateRunSensorResult(
    result=..., state=..., error=..., raw_data=..., log=..., executed=...
)

# Create from JSON
template_run_sensor_result = TemplateRunSensorResult.from_json(
    '{ "result": ..., "state": ..., "error": ..., "rawData": ..., "log": ..., "executed": ... }'
)

# Export to dictionary
template_run_sensor_result_dict = template_run_sensor_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


