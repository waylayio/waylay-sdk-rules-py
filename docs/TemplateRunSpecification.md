# TemplateRunSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[List[ResourceDataInjection]]** | The full dataset to process. If specified, template will be run as reactive template | [optional] 
**conf** | [**TemplateRunConfiguration**](TemplateRunConfiguration.md) |  | [optional] 
**variables** | **object** | The values for the variables declared in the template | [optional] 
**resource_meta_data** | **Dict[str, object]** | Metadata for any of the resources used in the template.  The current metadata for all resources used in the template is fetched at the start of the template run. This provided metadata is used to overwrite this current metadata | [optional] 

## Example

```python
from waylay.services.rules.models.template_run_specification import TemplateRunSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateRunSpecification from a JSON string
template_run_specification_instance = TemplateRunSpecification.from_json(json)
# print the JSON string representation of the object
print TemplateRunSpecification.to_json()

# convert the object into a dict
template_run_specification_dict = template_run_specification_instance.to_dict()
# create an instance of TemplateRunSpecification from a dict
template_run_specification_form_dict = template_run_specification.from_dict(template_run_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


