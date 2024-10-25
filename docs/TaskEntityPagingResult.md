# TaskEntityPagingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of items skipped before this page of results. | [default to 0]
**limit** | **int** | Size of one page of results. | [default to 10]
**total** | **int** | Total number of items matching the query of which this is one page of results. | 
**values** | [**List[TaskEntityPagingResultAllOfValues]**](TaskEntityPagingResultAllOfValues.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.task_entity_paging_result import TaskEntityPagingResult

# TODO update the JSON string below
json = "{}"
# create an instance of TaskEntityPagingResult from a JSON string
task_entity_paging_result_instance = TaskEntityPagingResult.from_json(json)
# print the JSON string representation of the object
print TaskEntityPagingResult.to_json()

# convert the object into a dict
task_entity_paging_result_dict = task_entity_paging_result_instance.to_dict()
# create an instance of TaskEntityPagingResult from a dict
task_entity_paging_result_form_dict = task_entity_paging_result.from_dict(task_entity_paging_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


