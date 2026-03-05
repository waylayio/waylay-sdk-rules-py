# StateChangeTrigger

A trigger that executes on state change.

**Source:** `waylay.services.rules.models.state_change_trigger`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | 
**destination_label** | **str** | Unique node label | 
**invocation_policy** | **int** |  | [optional] 
**state_change_trigger** | [**TriggerStateChange**](TriggerStateChange.md) |  | 


## Example

```python
from waylay.services.rules.models.state_change_trigger import StateChangeTrigger

state_change_trigger = StateChangeTrigger(
    source_label=...,
    destination_label=...,
    invocation_policy=...,
    state_change_trigger=...,
)

# Create from JSON
state_change_trigger = StateChangeTrigger.from_json(
    '{ "sourceLabel": ..., "destinationLabel": ..., "invocationPolicy": ..., "stateChangeTrigger": ... }'
)

# Export to dictionary
state_change_trigger_dict = state_change_trigger.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


