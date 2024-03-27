# NodeStateSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State to set. Should be one of the supported states of the sensor | [optional] 
**raw_data** | **object** | rawData to set | [optional] 

## Example

```python
from waylay.services.rules.models.node_state_specification import NodeStateSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStateSpecification from a JSON string
node_state_specification_instance = NodeStateSpecification.from_json(json)
# print the JSON string representation of the object
print NodeStateSpecification.to_json()

# convert the object into a dict
node_state_specification_dict = node_state_specification_instance.to_dict()
# create an instance of NodeStateSpecification from a dict
node_state_specification_form_dict = node_state_specification.from_dict(node_state_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


