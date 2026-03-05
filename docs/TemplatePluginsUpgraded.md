# TemplatePluginsUpgraded


**Source:** `waylay.services.rules.models.template_plugins_upgraded`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **List[str]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.template_plugins_upgraded import (
    TemplatePluginsUpgraded,
)

template_plugins_upgraded = TemplatePluginsUpgraded(successful=...)

# Create from JSON
template_plugins_upgraded = TemplatePluginsUpgraded.from_json('{ "successful": ... }')

# Export to dictionary
template_plugins_upgraded_dict = template_plugins_upgraded.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


