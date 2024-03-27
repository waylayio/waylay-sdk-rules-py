# BatchIdQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from waylay.services.rules.models.batch_id_query import BatchIdQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchIdQuery from a JSON string
batch_id_query_instance = BatchIdQuery.from_json(json)
# print the JSON string representation of the object
print BatchIdQuery.to_json()

# convert the object into a dict
batch_id_query_dict = batch_id_query_instance.to_dict()
# create an instance of BatchIdQuery from a dict
batch_id_query_form_dict = batch_id_query.from_dict(batch_id_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


