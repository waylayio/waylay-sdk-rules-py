# GenericTrigger


**Source:** `waylay.services.rules.models.generic_trigger`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_label** | **str** | Unique node label | [optional] 
**destination_label** | **str** | Unique node label | [optional] 
**invocation_policy** | **int** |  | [optional] 


## Example

```python
from waylay.services.rules.models.generic_trigger import GenericTrigger

generic_trigger = GenericTrigger(
    source_label=..., destination_label=..., invocation_policy=...
)

# Create from JSON
generic_trigger = GenericTrigger.from_json(
    '{ "sourceLabel": ..., "destinationLabel": ..., "invocationPolicy": ... }'
)

# Export to dictionary
generic_trigger_dict = generic_trigger.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


