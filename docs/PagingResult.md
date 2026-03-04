# PagingResult


**Source:** `waylay.services.rules.models.paging_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 10]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 


## Example

```python
from waylay.services.rules.models.paging_result import PagingResult

paging_result = PagingResult(skip=..., limit=..., total=...)

# Create from JSON
paging_result = PagingResult.from_json('{ "skip": ..., "limit": ..., "total": ... }')

# Export to dictionary
paging_result_dict = paging_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


