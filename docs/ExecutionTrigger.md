# ExecutionTrigger

A trigger that always executes on successful execution of the source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | 
**destination_label** | **str** | Unique node label | 
**invocation_policy** | **int** |  | [optional] 

## Example

```python
from waylay.services.rules.models.execution_trigger import ExecutionTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionTrigger from a JSON string
execution_trigger_instance = ExecutionTrigger.from_json(json)
# print the JSON string representation of the object
print ExecutionTrigger.to_json()

# convert the object into a dict
execution_trigger_dict = execution_trigger_instance.to_dict()
# create an instance of ExecutionTrigger from a dict
execution_trigger_form_dict = execution_trigger.from_dict(execution_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


