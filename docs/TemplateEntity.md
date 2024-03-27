# TemplateEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** | flag to indicate if the template is the discovery template | [optional] 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 

## Example

```python
from waylay.services.rules.models.template_entity import TemplateEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEntity from a JSON string
template_entity_instance = TemplateEntity.from_json(json)
# print the JSON string representation of the object
print TemplateEntity.to_json()

# convert the object into a dict
template_entity_dict = template_entity_instance.to_dict()
# create an instance of TemplateEntity from a dict
template_entity_form_dict = template_entity.from_dict(template_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


