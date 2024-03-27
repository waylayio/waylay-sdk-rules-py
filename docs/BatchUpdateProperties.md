# BatchUpdateProperties

Update variables and/or tags of multiple tasks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchUpdatePropertiesAllOfAction**](BatchUpdatePropertiesAllOfAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PropertyUpdatesSpec**](PropertyUpdatesSpec.md) |  | 

## Example

```python
from waylay.services.rules.models.batch_update_properties import BatchUpdateProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdateProperties from a JSON string
batch_update_properties_instance = BatchUpdateProperties.from_json(json)
# print the JSON string representation of the object
print BatchUpdateProperties.to_json()

# convert the object into a dict
batch_update_properties_dict = batch_update_properties_instance.to_dict()
# create an instance of BatchUpdateProperties from a dict
batch_update_properties_form_dict = batch_update_properties.from_dict(batch_update_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


