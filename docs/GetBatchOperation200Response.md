# GetBatchOperation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user** | **str** | User id of the user who started the operation | 
**operation** | [**BatchOperationOperation**](BatchOperationOperation.md) |  | 
**queue_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**finished_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**results** | [**OperationResultObjectResults**](OperationResultObjectResults.md) |  | 

## Example

```python
from waylay.services.rules.models.get_batch_operation200_response import GetBatchOperation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBatchOperation200Response from a JSON string
get_batch_operation200_response_instance = GetBatchOperation200Response.from_json(json)
# print the JSON string representation of the object
print GetBatchOperation200Response.to_json()

# convert the object into a dict
get_batch_operation200_response_dict = get_batch_operation200_response_instance.to_dict()
# create an instance of GetBatchOperation200Response from a dict
get_batch_operation200_response_form_dict = get_batch_operation200_response.from_dict(get_batch_operation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


