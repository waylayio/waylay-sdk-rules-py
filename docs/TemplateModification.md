# TemplateModification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**TemplateModificationOperation**](TemplateModificationOperation.md) |  | 
**updates** | [**List[PluginUpdateSpec]**](PluginUpdateSpec.md) |  | 
**reload_tasks** | **bool** | Should all tasks created from the template be reloaded | [optional] [default to False]

## Example

```python
from waylay.services.rules.models.template_modification import TemplateModification

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateModification from a JSON string
template_modification_instance = TemplateModification.from_json(json)
# print the JSON string representation of the object
print TemplateModification.to_json()

# convert the object into a dict
template_modification_dict = template_modification_instance.to_dict()
# create an instance of TemplateModification from a dict
template_modification_form_dict = template_modification.from_dict(template_modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


