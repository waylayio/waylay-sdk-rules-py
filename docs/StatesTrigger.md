# StatesTrigger

A trigger that is conditional on the states of the source.

**Source:** `waylay.services.rules.models.states_trigger`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | 
**destination_label** | **str** | Unique node label | 
**invocation_policy** | **int** |  | [optional] 
**states_trigger** | **List[str]** | array of states of source node under which to fire | 


## Example

```python
from waylay.services.rules.models.states_trigger import StatesTrigger

states_trigger = StatesTrigger(
    source_label=..., destination_label=..., invocation_policy=..., states_trigger=...
)

# Create from JSON
states_trigger = StatesTrigger.from_json(
    '{ "sourceLabel": ..., "destinationLabel": ..., "invocationPolicy": ..., "statesTrigger": ... }'
)

# Export to dictionary
states_trigger_dict = states_trigger.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


