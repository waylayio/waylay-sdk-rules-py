# GenericTrigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | [optional] 
**destination_label** | **str** | Unique node label | [optional] 
**invocation_policy** | **int** |  | [optional] 

## Example

```python
from waylay.services.rules.models.generic_trigger import GenericTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of GenericTrigger from a JSON string
generic_trigger_instance = GenericTrigger.from_json(json)
# print the JSON string representation of the object
print GenericTrigger.to_json()

# convert the object into a dict
generic_trigger_dict = generic_trigger_instance.to_dict()
# create an instance of GenericTrigger from a dict
generic_trigger_form_dict = generic_trigger.from_dict(generic_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


