# TemplateRunActuatorResult


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
from waylay.services.rules.models.template_run_actuator_result import TemplateRunActuatorResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRunActuatorResult from a JSON string
template_run_actuator_result_instance = TemplateRunActuatorResult.from_json(json)
# print the JSON string representation of the object
print TemplateRunActuatorResult.to_json()

# convert the object into a dict
template_run_actuator_result_dict = template_run_actuator_result_instance.to_dict()
# create an instance of TemplateRunActuatorResult from a dict
template_run_actuator_result_form_dict = template_run_actuator_result.from_dict(template_run_actuator_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


