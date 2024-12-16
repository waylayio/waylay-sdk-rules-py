# TemplateEntityCommonAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** | flag to indicate if the template is the discovery template | [optional] 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**description** | **str** | Description of the template | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 

## Example

```python
from waylay.services.rules.models.template_entity_common_attributes import TemplateEntityCommonAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEntityCommonAttributes from a JSON string
template_entity_common_attributes_instance = TemplateEntityCommonAttributes.from_json(json)
# print the JSON string representation of the object
print TemplateEntityCommonAttributes.to_json()

# convert the object into a dict
template_entity_common_attributes_dict = template_entity_common_attributes_instance.to_dict()
# create an instance of TemplateEntityCommonAttributes from a dict
template_entity_common_attributes_form_dict = template_entity_common_attributes.from_dict(template_entity_common_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


