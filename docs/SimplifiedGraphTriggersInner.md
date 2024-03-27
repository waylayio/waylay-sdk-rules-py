# SimplifiedGraphTriggersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | 
**destination_label** | **str** | Unique node label | 
**invocation_policy** | **int** |  | [optional] 
**state_change_trigger** | [**TriggerStateChange**](TriggerStateChange.md) |  | 
**states_trigger** | **List[str]** | array of states of source node under which to fire | 

## Example

```python
from waylay.services.rules.models.simplified_graph_triggers_inner import SimplifiedGraphTriggersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedGraphTriggersInner from a JSON string
simplified_graph_triggers_inner_instance = SimplifiedGraphTriggersInner.from_json(json)
# print the JSON string representation of the object
print SimplifiedGraphTriggersInner.to_json()

# convert the object into a dict
simplified_graph_triggers_inner_dict = simplified_graph_triggers_inner_instance.to_dict()
# create an instance of SimplifiedGraphTriggersInner from a dict
simplified_graph_triggers_inner_form_dict = simplified_graph_triggers_inner.from_dict(simplified_graph_triggers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


