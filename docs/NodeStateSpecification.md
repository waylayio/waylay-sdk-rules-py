# NodeStateSpecification


**Source:** `waylay.services.rules.models.node_state_specification`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State to set. Should be one of the supported states of the sensor | [optional] 
**raw_data** | **object** | rawData to set | [optional] 


## Example

```python
from waylay.services.rules.models.node_state_specification import NodeStateSpecification

node_state_specification = NodeStateSpecification(state=..., raw_data=...)

# Create from JSON
node_state_specification = NodeStateSpecification.from_json(
    '{ "state": ..., "rawData": ... }'
)

# Export to dictionary
node_state_specification_dict = node_state_specification.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


