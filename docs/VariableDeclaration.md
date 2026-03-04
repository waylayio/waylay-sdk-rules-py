# VariableDeclaration

Variable declaration.

**Source:** `waylay.services.rules.models.variable_declaration`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Variable Name | 
**display_name** | **str** | Display name. Will default to the name if not specified | [optional] 
**type** | [**VariableType**](VariableType.md) |  | 
**format** | [**VariableFormat**](VariableFormat.md) |  | [optional] 
**mandatory** | **bool** | flag to indicate if value for variable is mandatory or not | [optional] [default to False]
**description** | **str** | Description of the variable | [optional] 
**default_value** | [**VariableDeclarationDefaultValue**](VariableDeclarationDefaultValue.md) |  | [optional] 
**override_by_stream** | **bool** | Override variable value by streamed data parameter with the same name in reactive tasks if this property set to true | [optional] [default to False]
**override_by_data** | **bool** | Override variable value by last value of task node&#39;s resource timeseries metric with the same name. Task node should be linked to some resource. | [optional] [default to False]


## Example

```python
from waylay.services.rules.models.variable_declaration import VariableDeclaration

variable_declaration = VariableDeclaration(
    name=...,
    display_name=...,
    type=...,
    format=...,
    mandatory=...,
    description=...,
    default_value=...,
    override_by_stream=...,
    override_by_data=...,
)

# Create from JSON
variable_declaration = VariableDeclaration.from_json(
    '{ "name": ..., "displayName": ..., "type": ..., "format": ..., "mandatory": ..., "description": ..., "defaultValue": ..., "overrideByStream": ..., "overrideByData": ... }'
)

# Export to dictionary
variable_declaration_dict = variable_declaration.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


