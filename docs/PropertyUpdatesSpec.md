# PropertyUpdatesSpec


**Source:** `waylay.services.rules.models.property_updates_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **object** | Set of variables to update. Will be merged with the current variables. To delete any of the current variables (and fall back to the default value from the template) set the value to &#x60;null&#x60; | [optional] 
**tags** | **object** | Key-value pairs. Will be merged with the current tags. To delete any of the current tags set the value to &#x60;null&#x60; | [optional] 
**gates_need_full_observation** | **bool** | Only evaluate gates when all inputs are observed | [optional] [default to False]
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]


## Example

```python
from waylay.services.rules.models.property_updates_spec import PropertyUpdatesSpec

property_updates_spec = PropertyUpdatesSpec(
    variables=...,
    tags=...,
    gates_need_full_observation=...,
    reset_observations=...,
    parallel=...,
)

# Create from JSON
property_updates_spec = PropertyUpdatesSpec.from_json(
    '{ "variables": ..., "tags": ..., "gatesNeedFullObservation": ..., "resetObservations": ..., "parallel": ... }'
)

# Export to dictionary
property_updates_spec_dict = property_updates_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


