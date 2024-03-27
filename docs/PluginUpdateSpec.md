# PluginUpdateSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the plugin to update | 
**from_version** | [**PluginUpdateSpecFromVersion**](PluginUpdateSpecFromVersion.md) |  | 
**to_version** | **str** |  | 

## Example

```python
from waylay.services.rules.models.plugin_update_spec import PluginUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PluginUpdateSpec from a JSON string
plugin_update_spec_instance = PluginUpdateSpec.from_json(json)
# print the JSON string representation of the object
print PluginUpdateSpec.to_json()

# convert the object into a dict
plugin_update_spec_dict = plugin_update_spec_instance.to_dict()
# create an instance of PluginUpdateSpec from a dict
plugin_update_spec_form_dict = plugin_update_spec.from_dict(plugin_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


