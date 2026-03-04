# TemplateRunActuatorResult


**Source:** `waylay.services.rules.models.template_run_actuator_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the actuator was successfully executed | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**raw_data** | **object** |  | [optional] 
**log** | **List[object]** |  | [optional] 
**executed** | **bool** | flag indicating if the actuator was executed | 


## Example

```python
from waylay.services.rules.models.template_run_actuator_result import (
    TemplateRunActuatorResult,
)

template_run_actuator_result = TemplateRunActuatorResult(
    result=..., error=..., raw_data=..., log=..., executed=...
)

# Create from JSON
template_run_actuator_result = TemplateRunActuatorResult.from_json(
    '{ "result": ..., "error": ..., "rawData": ..., "log": ..., "executed": ... }'
)

# Export to dictionary
template_run_actuator_result_dict = template_run_actuator_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


