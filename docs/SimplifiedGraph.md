# SimplifiedGraph

Graph in simplified format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 

## Example

```python
from waylay.services.rules.models.simplified_graph import SimplifiedGraph

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedGraph from a JSON string
simplified_graph_instance = SimplifiedGraph.from_json(json)
# print the JSON string representation of the object
print SimplifiedGraph.to_json()

# convert the object into a dict
simplified_graph_dict = simplified_graph_instance.to_dict()
# create an instance of SimplifiedGraph from a dict
simplified_graph_form_dict = simplified_graph.from_dict(simplified_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


