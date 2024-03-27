# StatesTrigger

A trigger that is conditional on the states of the source.

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

# TODO update the JSON string below
json = "{}"
# create an instance of StatesTrigger from a JSON string
states_trigger_instance = StatesTrigger.from_json(json)
# print the JSON string representation of the object
print StatesTrigger.to_json()

# convert the object into a dict
states_trigger_dict = states_trigger_instance.to_dict()
# create an instance of StatesTrigger from a dict
states_trigger_form_dict = states_trigger.from_dict(states_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


