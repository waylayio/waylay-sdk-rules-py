# ActuatorNode

Representation of an actuator in a Rule Template.

**Source:** `waylay.services.rules.models.actuator_node`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Unique node label | 
**name** | **str** |  | 
**version** | **str** |  | 
**properties** | **object** |  | [optional] 
**sequence** | **int** |  | [optional] 
**position** | **List[int]** |  | [optional] 
**timeout** | **str** |  | [optional] [default to 'PT50S']
**description** | **str** |  | [optional] 


## Example

```python
from waylay.services.rules.models.actuator_node import ActuatorNode

actuator_node = ActuatorNode(
    label=...,
    name=...,
    version=...,
    properties=...,
    sequence=...,
    position=...,
    timeout=...,
    description=...,
)

# Create from JSON
actuator_node = ActuatorNode.from_json(
    '{ "label": ..., "name": ..., "version": ..., "properties": ..., "sequence": ..., "position": ..., "timeout": ..., "description": ... }'
)

# Export to dictionary
actuator_node_dict = actuator_node.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


