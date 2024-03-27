# PagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 10]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 

## Example

```python
from waylay.services.rules.models.paging_result import PagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagingResult from a JSON string
paging_result_instance = PagingResult.from_json(json)
# print the JSON string representation of the object
print PagingResult.to_json()

# convert the object into a dict
paging_result_dict = paging_result_instance.to_dict()
# create an instance of PagingResult from a dict
paging_result_form_dict = paging_result.from_dict(paging_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


