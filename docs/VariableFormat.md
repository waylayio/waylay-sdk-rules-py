# VariableFormat

Format for a variable definition.

**Source:** `waylay.services.rules.models.variable_format`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**values** | [**List[VariableFormatValue]**](VariableFormatValue.md) |  | [optional] 


## Example

```python
from waylay.services.rules.models.variable_format import VariableFormat

variable_format = VariableFormat(type=..., values=...)

# Create from JSON
variable_format = VariableFormat.from_json('{ "type": ..., "values": ... }')

# Export to dictionary
variable_format_dict = variable_format.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


