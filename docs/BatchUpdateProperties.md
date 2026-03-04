# BatchUpdateProperties

Update variables and/or tags of multiple tasks

**Source:** `waylay.services.rules.models.batch_update_properties`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchUpdatePropertiesAction**](BatchUpdatePropertiesAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PropertyUpdatesSpec**](PropertyUpdatesSpec.md) |  | 


## Example

```python
from waylay.services.rules.models.batch_update_properties import BatchUpdateProperties

batch_update_properties = BatchUpdateProperties(
    entity=..., action=..., query=..., action_parameters=...
)

# Create from JSON
batch_update_properties = BatchUpdateProperties.from_json(
    '{ "entity": ..., "action": ..., "query": ..., "actionParameters": ... }'
)

# Export to dictionary
batch_update_properties_dict = batch_update_properties.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


