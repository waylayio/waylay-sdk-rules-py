# TemplateRunConfiguration

Template run configurations

**Source:** `waylay.services.rules.models.template_run_configuration`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execute_actuators** | **bool** | Flag to trigger actual execution of actuators | [optional] [default to False]
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** | reset observations before injecting data | [optional] [default to True]
**gates_need_full_observation** | **bool** | Only evaluate gates when all inputs are observed | [optional] [default to False]


## Example

```python
from waylay.services.rules.models.template_run_configuration import (
    TemplateRunConfiguration,
)

template_run_configuration = TemplateRunConfiguration(
    execute_actuators=...,
    resource=...,
    reset_observations=...,
    gates_need_full_observation=...,
)

# Create from JSON
template_run_configuration = TemplateRunConfiguration.from_json(
    '{ "executeActuators": ..., "resource": ..., "resetObservations": ..., "gatesNeedFullObservation": ... }'
)

# Export to dictionary
template_run_configuration_dict = template_run_configuration.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


