# TemplateRunConfiguration

Template run configurations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execute_actuators** | **bool** | Flag to trigger actual execution of actuators | [optional] [default to False]
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** | reset observations before injecting data | [optional] [default to True]
**gates_need_full_observation** | **bool** | Only evaluate gates when all inputs are observed | [optional] [default to False]

## Example

```python
from waylay.services.rules.models.template_run_configuration import TemplateRunConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRunConfiguration from a JSON string
template_run_configuration_instance = TemplateRunConfiguration.from_json(json)
# print the JSON string representation of the object
print TemplateRunConfiguration.to_json()

# convert the object into a dict
template_run_configuration_dict = template_run_configuration_instance.to_dict()
# create an instance of TemplateRunConfiguration from a dict
template_run_configuration_form_dict = template_run_configuration.from_dict(template_run_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


