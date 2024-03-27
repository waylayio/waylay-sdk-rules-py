# PropertyUpdatesSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **object** | Set of variables to update. Will be merged with the current variables. To delete any of the current variables (and fall back to the default value from the template) set the value to &#x60;null&#x60; | [optional] 
**tags** | **object** | Key-value pairs. Will be merged with the current tags. To delete any of the current tags set the value to &#x60;null&#x60; | [optional] 

## Example

```python
from waylay.services.rules.models.property_updates_spec import PropertyUpdatesSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyUpdatesSpec from a JSON string
property_updates_spec_instance = PropertyUpdatesSpec.from_json(json)
# print the JSON string representation of the object
print PropertyUpdatesSpec.to_json()

# convert the object into a dict
property_updates_spec_dict = property_updates_spec_instance.to_dict()
# create an instance of PropertyUpdatesSpec from a dict
property_updates_spec_form_dict = property_updates_spec.from_dict(property_updates_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


