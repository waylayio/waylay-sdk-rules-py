# RelationNode

Representation of a gate in a Rule Template.

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

# TODO update the JSON string below
json = "{}"
# create an instance of RelationNode from a JSON string
relation_node_instance = RelationNode.from_json(json)
# print the JSON string representation of the object
print RelationNode.to_json()

# convert the object into a dict
relation_node_dict = relation_node_instance.to_dict()
# create an instance of RelationNode from a dict
relation_node_form_dict = relation_node.from_dict(relation_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


