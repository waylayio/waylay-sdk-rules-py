# PluginUpdateSpec


**Source:** `waylay.services.rules.models.plugin_update_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the plugin to update | 
**from_version** | [**PluginUpdateSpecFromVersion**](PluginUpdateSpecFromVersion.md) |  | 
**to_version** | **str** | Plugin version to upgrade to | 


## Example

```python
from waylay.services.rules.models.plugin_update_spec import PluginUpdateSpec

plugin_update_spec = PluginUpdateSpec(name=..., from_version=..., to_version=...)

# Create from JSON
plugin_update_spec = PluginUpdateSpec.from_json(
    '{ "name": ..., "fromVersion": ..., "toVersion": ... }'
)

# Export to dictionary
plugin_update_spec_dict = plugin_update_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


