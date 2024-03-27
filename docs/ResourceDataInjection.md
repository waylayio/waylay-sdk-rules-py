# ResourceDataInjection

data to inject per resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Unique resource identifier | 
**timestamp** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 

## Example

```python
from waylay.services.rules.models.resource_data_injection import ResourceDataInjection

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDataInjection from a JSON string
resource_data_injection_instance = ResourceDataInjection.from_json(json)
# print the JSON string representation of the object
print ResourceDataInjection.to_json()

# convert the object into a dict
resource_data_injection_dict = resource_data_injection_instance.to_dict()
# create an instance of ResourceDataInjection from a dict
resource_data_injection_form_dict = resource_data_injection.from_dict(resource_data_injection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


