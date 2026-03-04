# TaskEntityPagingResult


**Source:** `waylay.services.rules.models.task_entity_paging_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 10]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[TaskWithRuntimeInfo]**](TaskWithRuntimeInfo.md) |  | [optional] 


## Example

```python
from waylay.services.rules.models.task_entity_paging_result import (
    TaskEntityPagingResult,
)

task_entity_paging_result = TaskEntityPagingResult(
    skip=..., limit=..., total=..., values=...
)

# Create from JSON
task_entity_paging_result = TaskEntityPagingResult.from_json(
    '{ "skip": ..., "limit": ..., "total": ..., "values": ... }'
)

# Export to dictionary
task_entity_paging_result_dict = task_entity_paging_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


