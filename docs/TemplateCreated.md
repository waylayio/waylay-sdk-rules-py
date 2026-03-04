# TemplateCreated


**Source:** `waylay.services.rules.models.template_created`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**uri** | **str** |  | 
**entity** | [**TemplateEntity**](TemplateEntity.md) |  | 


## Example

```python
from waylay.services.rules.models.template_created import TemplateCreated

template_created = TemplateCreated(status_code=..., uri=..., entity=...)

# Create from JSON
template_created = TemplateCreated.from_json(
    '{ "statusCode": ..., "uri": ..., "entity": ... }'
)

# Export to dictionary
template_created_dict = template_created.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


