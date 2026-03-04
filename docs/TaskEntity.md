# TaskEntity


**Source:** `waylay.services.rules.models.task_entity`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique task identifier | 
**name** | **str** |  | 
**status** | [**TaskStatus**](TaskStatus.md) |  | 
**user** | **str** | Creation user mail address or &#39;system&#39; for system generated tasks | 
**create_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970, not counting leap seconds. | 
**template** | **str** | Unique template identifier | [optional] 
**network** | **object** | The graph, either from the template or from the task definition. Depending on the &#x60;format&#x60; query parameter either BN or simplified format | 
**resource_ids** | **List[str]** | List of resources that are used in the task | [optional] 


## Example

```python
from waylay.services.rules.models.task_entity import TaskEntity

task_entity = TaskEntity(
    id=...,
    name=...,
    status=...,
    user=...,
    create_time=...,
    template=...,
    network=...,
    resource_ids=...,
)

# Create from JSON
task_entity = TaskEntity.from_json(
    '{ "ID": ..., "name": ..., "status": ..., "user": ..., "createTime": ..., "template": ..., "network": ..., "resourceIds": ... }'
)

# Export to dictionary
task_entity_dict = task_entity.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


