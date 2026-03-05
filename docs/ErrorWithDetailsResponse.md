# ErrorWithDetailsResponse


**Source:** `waylay.services.rules.models.error_with_details_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | 
**error** | **str** |  | 
**code** | **str** | Optional error code | [optional] 
**details** | [**List[ValidationIssue]**](ValidationIssue.md) |  | [optional] 


## Example

```python
from waylay.services.rules.models.error_with_details_response import (
    ErrorWithDetailsResponse,
)

error_with_details_response = ErrorWithDetailsResponse(
    status_code=..., error=..., code=..., details=...
)

# Create from JSON
error_with_details_response = ErrorWithDetailsResponse.from_json(
    '{ "statusCode": ..., "error": ..., "code": ..., "details": ... }'
)

# Export to dictionary
error_with_details_response_dict = error_with_details_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


