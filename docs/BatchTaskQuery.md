# BatchTaskQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 
**name** | **str** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**type** | [**TaskScenarioType**](TaskScenarioType.md) |  | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**template** | **str** | Unique template identifier | [optional] 
**plugin** | **str** | either name of a plugin (e.g. &#x60;mySensor&#x60;), or full version specification of the plug (e.g &#x60;mySensor:1.0.3&#x60;) | [optional] 
**user** | **str** | Creation user mail address or &#39;system&#39; for system generated tasks | [optional] 
**finished_before** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 
**created_after** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 
**created_before** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | [optional] 
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 

## Example

```python
from waylay.services.rules.models.batch_task_query import BatchTaskQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTaskQuery from a JSON string
batch_task_query_instance = BatchTaskQuery.from_json(json)
# print the JSON string representation of the object
print BatchTaskQuery.to_json()

# convert the object into a dict
batch_task_query_dict = batch_task_query_instance.to_dict()
# create an instance of BatchTaskQuery from a dict
batch_task_query_form_dict = batch_task_query.from_dict(batch_task_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


