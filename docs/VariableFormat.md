# VariableFormat

Format for a variable definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**values** | [**List[PossibleValuesEnumDeclarationInner]**](PossibleValuesEnumDeclarationInner.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.variable_format import VariableFormat

# TODO update the JSON string below
json = "{}"
# create an instance of VariableFormat from a JSON string
variable_format_instance = VariableFormat.from_json(json)
# print the JSON string representation of the object
print VariableFormat.to_json()

# convert the object into a dict
variable_format_dict = variable_format_instance.to_dict()
# create an instance of VariableFormat from a dict
variable_format_form_dict = variable_format.from_dict(variable_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


