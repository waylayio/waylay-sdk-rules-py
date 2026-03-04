# TemplateEntityCommonAttributes


**Source:** `waylay.services.rules.models.template_entity_common_attributes`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** | flag to indicate if the template is the discovery template | [optional] 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**description** | **str** | Description of the template | [optional] 
**icon_url** | **str** | URL to an icon representing the template | [optional] 
**protected** | **bool** | Flag to indicate if the template is protected. Can be set only by user with protected permission. Modification or deletion of template is not allowed to user without protected permission. | [optional] [default to False]
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 


## Example

```python
from waylay.services.rules.models.template_entity_common_attributes import (
    TemplateEntityCommonAttributes,
)

template_entity_common_attributes = TemplateEntityCommonAttributes(
    name=...,
    discovery_template=...,
    tags=...,
    variables=...,
    task_defaults=...,
    description=...,
    icon_url=...,
    protected=...,
    notes=...,
)

# Create from JSON
template_entity_common_attributes = TemplateEntityCommonAttributes.from_json(
    '{ "name": ..., "discoveryTemplate": ..., "tags": ..., "variables": ..., "taskDefaults": ..., "description": ..., "iconURL": ..., "protected": ..., "notes": ... }'
)

# Export to dictionary
template_entity_common_attributes_dict = template_entity_common_attributes.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


