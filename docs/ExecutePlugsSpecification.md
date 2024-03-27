# ExecutePlugsSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **object** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**stream_data** | **object** |  | [optional] 

## Example

```python
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutePlugsSpecification from a JSON string
execute_plugs_specification_instance = ExecutePlugsSpecification.from_json(json)
# print the JSON string representation of the object
print ExecutePlugsSpecification.to_json()

# convert the object into a dict
execute_plugs_specification_dict = execute_plugs_specification_instance.to_dict()
# create an instance of ExecutePlugsSpecification from a dict
execute_plugs_specification_form_dict = execute_plugs_specification.from_dict(execute_plugs_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


