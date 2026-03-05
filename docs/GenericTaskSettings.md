# GenericTaskSettings


**Source:** `waylay.services.rules.models.generic_task_settings`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]
**gates_need_full_observation** | **bool** |  | [optional] [default to False]
**protected** | **bool** |  | [optional] [default to False]
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**variables** | **object** | set of variables which will be used when starting a task and will automatically be injected in the template before starting a task. | [optional] 


## Example

```python
from waylay.services.rules.models.generic_task_settings import GenericTaskSettings

generic_task_settings = GenericTaskSettings(
    name=...,
    resource=...,
    reset_observations=...,
    parallel=...,
    gates_need_full_observation=...,
    protected=...,
    tags=...,
    variables=...,
)

# Create from JSON
generic_task_settings = GenericTaskSettings.from_json(
    '{ "name": ..., "resource": ..., "resetObservations": ..., "parallel": ..., "gatesNeedFullObservation": ..., "protected": ..., "tags": ..., "variables": ... }'
)

# Export to dictionary
generic_task_settings_dict = generic_task_settings.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


