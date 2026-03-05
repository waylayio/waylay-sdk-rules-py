# TemplateModification


**Source:** `waylay.services.rules.models.template_modification`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**TemplateModificationOperation**](TemplateModificationOperation.md) |  | 
**updates** | [**List[PluginUpdateSpec]**](PluginUpdateSpec.md) |  | 
**reload_tasks** | **bool** | Should all tasks created from the template be reloaded | [optional] [default to False]


## Example

```python
from waylay.services.rules.models.template_modification import TemplateModification

template_modification = TemplateModification(
    operation=..., updates=..., reload_tasks=...
)

# Create from JSON
template_modification = TemplateModification.from_json(
    '{ "operation": ..., "updates": ..., "reloadTasks": ... }'
)

# Export to dictionary
template_modification_dict = template_modification.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


