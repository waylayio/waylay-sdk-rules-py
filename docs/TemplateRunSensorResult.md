# TemplateRunSensorResult


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
from waylay.services.rules.models.template_run_sensor_result import TemplateRunSensorResult

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRunSensorResult from a JSON string
template_run_sensor_result_instance = TemplateRunSensorResult.from_json(json)
# print the JSON string representation of the object
print TemplateRunSensorResult.to_json()

# convert the object into a dict
template_run_sensor_result_dict = template_run_sensor_result_instance.to_dict()
# create an instance of TemplateRunSensorResult from a dict
template_run_sensor_result_form_dict = template_run_sensor_result.from_dict(template_run_sensor_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


