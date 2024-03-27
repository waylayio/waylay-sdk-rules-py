# ActuatorNode

Representation of an actuator in a Rule Template.

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

## Example

```python
from waylay.services.rules.models.actuator_node import ActuatorNode

# TODO update the JSON string below
json = "{}"
# create an instance of ActuatorNode from a JSON string
actuator_node_instance = ActuatorNode.from_json(json)
# print the JSON string representation of the object
print ActuatorNode.to_json()

# convert the object into a dict
actuator_node_dict = actuator_node_instance.to_dict()
# create an instance of ActuatorNode from a dict
actuator_node_form_dict = actuator_node.from_dict(actuator_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


