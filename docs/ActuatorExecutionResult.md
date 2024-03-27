# ActuatorExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the actuator was successfully executed | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**raw_data** | **object** |  | [optional] 
**log** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.rules.models.actuator_execution_result import ActuatorExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of ActuatorExecutionResult from a JSON string
actuator_execution_result_instance = ActuatorExecutionResult.from_json(json)
# print the JSON string representation of the object
print ActuatorExecutionResult.to_json()

# convert the object into a dict
actuator_execution_result_dict = actuator_execution_result_instance.to_dict()
# create an instance of ActuatorExecutionResult from a dict
actuator_execution_result_form_dict = actuator_execution_result.from_dict(actuator_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


