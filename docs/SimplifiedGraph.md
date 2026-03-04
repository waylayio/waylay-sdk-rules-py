# SimplifiedGraph

Graph in simplified format

**Source:** `waylay.services.rules.models.simplified_graph`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[TriggerType]**](TriggerType.md) | List of conditions under which actuators/sensors get executed. | [optional] 


## Example

```python
from waylay.services.rules.models.simplified_graph import SimplifiedGraph

simplified_graph = SimplifiedGraph(
    sensors=..., actuators=..., relations=..., triggers=...
)

# Create from JSON
simplified_graph = SimplifiedGraph.from_json(
    '{ "sensors": ..., "actuators": ..., "relations": ..., "triggers": ... }'
)

# Export to dictionary
simplified_graph_dict = simplified_graph.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


