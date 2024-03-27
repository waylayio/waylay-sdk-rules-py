# TemplateRunInvocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | Unique task identifier | 
**invocation_id** | **str** | Unique invocation identifier | 
**sensors** | [**Dict[str, TemplateRunSensorResult]**](TemplateRunSensorResult.md) | The execution result for each of the sensors of the template | 
**actuators** | [**Dict[str, TemplateRunActuatorResult]**](TemplateRunActuatorResult.md) | The execution result for each of the actuators of the template | 
**log** | [**List[LogsInner]**](LogsInner.md) |  | 

## Example

```python
from waylay.services.rules.models.template_run_invocation import TemplateRunInvocation

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRunInvocation from a JSON string
template_run_invocation_instance = TemplateRunInvocation.from_json(json)
# print the JSON string representation of the object
print TemplateRunInvocation.to_json()

# convert the object into a dict
template_run_invocation_dict = template_run_invocation_instance.to_dict()
# create an instance of TemplateRunInvocation from a dict
template_run_invocation_form_dict = template_run_invocation.from_dict(template_run_invocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


