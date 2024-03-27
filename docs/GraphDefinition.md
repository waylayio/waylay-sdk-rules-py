# GraphDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 
**nodes** | **List[object]** |  | [optional] 
**posterior** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.rules.models.graph_definition import GraphDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of GraphDefinition from a JSON string
graph_definition_instance = GraphDefinition.from_json(json)
# print the JSON string representation of the object
print GraphDefinition.to_json()

# convert the object into a dict
graph_definition_dict = graph_definition_instance.to_dict()
# create an instance of GraphDefinition from a dict
graph_definition_form_dict = graph_definition.from_dict(graph_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


