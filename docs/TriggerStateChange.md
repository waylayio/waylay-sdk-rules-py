# TriggerStateChange

State change specification under which to trigger the next node.

**Source:** `waylay.services.rules.models.trigger_state_change`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_from** | **str** |  | 
**state_to** | **str** |  | 


## Example

```python
from waylay.services.rules.models.trigger_state_change import TriggerStateChange

trigger_state_change = TriggerStateChange(state_from=..., state_to=...)

# Create from JSON
trigger_state_change = TriggerStateChange.from_json(
    '{ "stateFrom": ..., "stateTo": ... }'
)

# Export to dictionary
trigger_state_change_dict = trigger_state_change.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


