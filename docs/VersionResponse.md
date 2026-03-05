# VersionResponse


**Source:** `waylay.services.rules.models.version_response`




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

version_response = VersionResponse(
    version=..., name=..., start_time=..., uptime=..., status=...
)

# Create from JSON
version_response = VersionResponse.from_json(
    '{ "version": ..., "name": ..., "startTime": ..., "uptime": ..., "status": ... }'
)

# Export to dictionary
version_response_dict = version_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


