# ExecutionTrigger

A trigger that always executes on successful execution of the source.

**Source:** `waylay.services.rules.models.execution_trigger`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | 
**destination_label** | **str** | Unique node label | 
**invocation_policy** | **int** |  | [optional] 


## Example

```python
from waylay.services.rules.models.execution_trigger import ExecutionTrigger

execution_trigger = ExecutionTrigger(
    source_label=..., destination_label=..., invocation_policy=...
)

# Create from JSON
execution_trigger = ExecutionTrigger.from_json(
    '{ "sourceLabel": ..., "destinationLabel": ..., "invocationPolicy": ... }'
)

# Export to dictionary
execution_trigger_dict = execution_trigger.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


