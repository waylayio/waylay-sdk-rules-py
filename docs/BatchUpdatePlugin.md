# BatchUpdatePlugin

Upgrade plugins on multiple tasks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**TemplateModificationOperation**](TemplateModificationOperation.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PluginUpdateSpec**](PluginUpdateSpec.md) |  | 

## Example

```python
from waylay.services.rules.models.batch_update_plugin import BatchUpdatePlugin

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdatePlugin from a JSON string
batch_update_plugin_instance = BatchUpdatePlugin.from_json(json)
# print the JSON string representation of the object
print BatchUpdatePlugin.to_json()

# convert the object into a dict
batch_update_plugin_dict = batch_update_plugin_instance.to_dict()
# create an instance of BatchUpdatePlugin from a dict
batch_update_plugin_form_dict = batch_update_plugin.from_dict(batch_update_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


