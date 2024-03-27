# StateChangeTrigger

A trigger that executes on state change.

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

# TODO update the JSON string below
json = "{}"
# create an instance of StateChangeTrigger from a JSON string
state_change_trigger_instance = StateChangeTrigger.from_json(json)
# print the JSON string representation of the object
print StateChangeTrigger.to_json()

# convert the object into a dict
state_change_trigger_dict = state_change_trigger_instance.to_dict()
# create an instance of StateChangeTrigger from a dict
state_change_trigger_form_dict = state_change_trigger.from_dict(state_change_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


