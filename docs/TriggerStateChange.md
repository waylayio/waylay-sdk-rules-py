# TriggerStateChange

State change specification under which to trigger the next node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_from** | **str** |  | 
**state_to** | **str** |  | 

## Example

```python
from waylay.services.rules.models.trigger_state_change import TriggerStateChange

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerStateChange from a JSON string
trigger_state_change_instance = TriggerStateChange.from_json(json)
# print the JSON string representation of the object
print TriggerStateChange.to_json()

# convert the object into a dict
trigger_state_change_dict = trigger_state_change_instance.to_dict()
# create an instance of TriggerStateChange from a dict
trigger_state_change_form_dict = trigger_state_change.from_dict(trigger_state_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


