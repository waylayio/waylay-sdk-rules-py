# ResourceDataInjection

data to inject per resource

**Source:** `waylay.services.rules.models.resource_data_injection`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Unique resource identifier | 
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 


## Example

```python
from waylay.services.rules.models.resource_data_injection import ResourceDataInjection

resource_data_injection = ResourceDataInjection(resource=..., timestamp=...)

# Create from JSON
resource_data_injection = ResourceDataInjection.from_json(
    '{ "resource": ..., "timestamp": ... }'
)

# Export to dictionary
resource_data_injection_dict = resource_data_injection.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


