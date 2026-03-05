# BatchUpdatePlugin

Upgrade plugins on multiple tasks

**Source:** `waylay.services.rules.models.batch_update_plugin`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchUpdatePluginAction**](BatchUpdatePluginAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PluginUpdateSpec**](PluginUpdateSpec.md) |  | 


## Example

```python
from waylay.services.rules.models.batch_update_plugin import BatchUpdatePlugin

batch_update_plugin = BatchUpdatePlugin(
    entity=..., action=..., query=..., action_parameters=...
)

# Create from JSON
batch_update_plugin = BatchUpdatePlugin.from_json(
    '{ "entity": ..., "action": ..., "query": ..., "actionParameters": ... }'
)

# Export to dictionary
batch_update_plugin_dict = batch_update_plugin.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


