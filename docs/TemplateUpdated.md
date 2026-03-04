# TemplateUpdated


**Source:** `waylay.services.rules.models.template_updated`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** | flag to indicate if the template is the discovery template | 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**description** | **str** | Description of the template | [optional] 
**icon_url** | **str** | URL to an icon representing the template | [optional] 
**protected** | **bool** | Flag to indicate if the template is protected. Can be set only by user with protected permission. Modification or deletion of template is not allowed to user without protected permission. | [optional] [default to False]
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 
**user** | **str** | Creation user mail address | 
**create_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**last_update_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[TriggerType]**](TriggerType.md) | List of conditions under which actuators/sensors get executed. | [optional] 


## Example

```python
from waylay.services.rules.models.template_updated import TemplateUpdated

template_updated = TemplateUpdated(
    name=...,
    discovery_template=...,
    tags=...,
    variables=...,
    task_defaults=...,
    description=...,
    icon_url=...,
    protected=...,
    notes=...,
    user=...,
    create_time=...,
    last_update_time=...,
    sensors=...,
    actuators=...,
    relations=...,
    triggers=...,
)

# Create from JSON
template_updated = TemplateUpdated.from_json(
    '{ "name": ..., "discoveryTemplate": ..., "tags": ..., "variables": ..., "taskDefaults": ..., "description": ..., "iconURL": ..., "protected": ..., "notes": ..., "user": ..., "createTime": ..., "lastUpdateTime": ..., "sensors": ..., "actuators": ..., "relations": ..., "triggers": ... }'
)

# Export to dictionary
template_updated_dict = template_updated.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


