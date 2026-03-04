# RelationNode

Representation of a gate in a Rule Template.

**Source:** `waylay.services.rules.models.relation_node`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Unique node label | 
**type** | [**GateType**](GateType.md) |  | 
**parent_labels** | **List[str]** |  | 
**combinations** | **List[List[str]]** |  | 
**position** | **List[int]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.relation_node import RelationNode

relation_node = RelationNode(
    label=..., type=..., parent_labels=..., combinations=..., position=...
)

# Create from JSON
relation_node = RelationNode.from_json(
    '{ "label": ..., "type": ..., "parentLabels": ..., "combinations": ..., "position": ... }'
)

# Export to dictionary
relation_node_dict = relation_node.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


