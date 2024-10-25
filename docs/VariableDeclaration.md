# VariableDeclaration

Variable declaration.

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

## Example

```python
from waylay.services.rules.models.variable_declaration import VariableDeclaration

# TODO update the JSON string below
json = "{}"
# create an instance of VariableDeclaration from a JSON string
variable_declaration_instance = VariableDeclaration.from_json(json)
# print the JSON string representation of the object
print VariableDeclaration.to_json()

# convert the object into a dict
variable_declaration_dict = variable_declaration_instance.to_dict()
# create an instance of VariableDeclaration from a dict
variable_declaration_form_dict = variable_declaration.from_dict(variable_declaration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


