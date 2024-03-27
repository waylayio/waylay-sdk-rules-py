# VersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**name** | **str** |  | 
**start_time** | **datetime** |  | [optional] 
**uptime** | **int** |  | [optional] 
**status** | [**VersionResponseStatus**](VersionResponseStatus.md) |  | 

## Example

```python
from waylay.services.rules.models.version_response import VersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionResponse from a JSON string
version_response_instance = VersionResponse.from_json(json)
# print the JSON string representation of the object
print VersionResponse.to_json()

# convert the object into a dict
version_response_dict = version_response_instance.to_dict()
# create an instance of VersionResponse from a dict
version_response_form_dict = version_response.from_dict(version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


