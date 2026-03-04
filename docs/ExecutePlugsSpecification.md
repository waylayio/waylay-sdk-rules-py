# ExecutePlugsSpecification


**Source:** `waylay.services.rules.models.execute_plugs_specification`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **object** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**stream_data** | **object** |  | [optional] 


## Example

```python
from waylay.services.rules.models.execute_plugs_specification import (
    ExecutePlugsSpecification,
)

execute_plugs_specification = ExecutePlugsSpecification(
    properties=..., resource=..., stream_data=...
)

# Create from JSON
execute_plugs_specification = ExecutePlugsSpecification.from_json(
    '{ "properties": ..., "resource": ..., "streamData": ... }'
)

# Export to dictionary
execute_plugs_specification_dict = execute_plugs_specification.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


