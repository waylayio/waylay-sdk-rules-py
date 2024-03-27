# StreamData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Unique resource identifier | 
**data** | [**StreamDataData**](StreamDataData.md) |  | 

## Example

```python
from waylay.services.rules.models.stream_data import StreamData

# TODO update the JSON string below
json = "{}"
# create an instance of StreamData from a JSON string
stream_data_instance = StreamData.from_json(json)
# print the JSON string representation of the object
print StreamData.to_json()

# convert the object into a dict
stream_data_dict = stream_data_instance.to_dict()
# create an instance of StreamData from a dict
stream_data_form_dict = stream_data.from_dict(stream_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


