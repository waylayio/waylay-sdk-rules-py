# ErrorWithDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 
**code** | **str** | Optional error code | [optional] 
**details** | [**List[ValidationIssue]**](ValidationIssue.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.error_with_details_response import ErrorWithDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWithDetailsResponse from a JSON string
error_with_details_response_instance = ErrorWithDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ErrorWithDetailsResponse.to_json()

# convert the object into a dict
error_with_details_response_dict = error_with_details_response_instance.to_dict()
# create an instance of ErrorWithDetailsResponse from a dict
error_with_details_response_form_dict = error_with_details_response.from_dict(error_with_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


