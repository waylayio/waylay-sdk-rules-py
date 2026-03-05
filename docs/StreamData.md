# StreamData


**Source:** `waylay.services.rules.models.stream_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Unique resource identifier | 
**data** | [**StreamDataPayload**](StreamDataPayload.md) |  | 


## Example

```python
from waylay.services.rules.models.stream_data import StreamData

stream_data = StreamData(resource=..., data=...)

# Create from JSON
stream_data = StreamData.from_json('{ "resource": ..., "data": ... }')

# Export to dictionary
stream_data_dict = stream_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


