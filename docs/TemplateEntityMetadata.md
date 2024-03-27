# TemplateEntityMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** | flag to indicate if the template is the discovery template | 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 
**user** | **str** | Creation user mail address | 
**create_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**last_update_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 

## Example

```python
from waylay.services.rules.models.template_entity_metadata import TemplateEntityMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEntityMetadata from a JSON string
template_entity_metadata_instance = TemplateEntityMetadata.from_json(json)
# print the JSON string representation of the object
print TemplateEntityMetadata.to_json()

# convert the object into a dict
template_entity_metadata_dict = template_entity_metadata_instance.to_dict()
# create an instance of TemplateEntityMetadata from a dict
template_entity_metadata_form_dict = template_entity_metadata.from_dict(template_entity_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


