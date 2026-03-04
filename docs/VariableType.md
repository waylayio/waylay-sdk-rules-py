# VariableType

Value type for a template variable.

**Source:** `waylay.services.rules.models.variable_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**STRING** | `'string'` |
**BOOLEAN** | `'boolean'` |
**INTEGER** | `'integer'` |
**DOUBLE** | `'double'` |
**LONG** | `'long'` |
**FLOAT** | `'float'` |
**OBJECT** | `'object'` |

## Example

```python
from waylay.services.rules.models.variable_type import VariableType

# Use enum by value
my_variable_type = VariableType.STRING
print(my_variable_type)  # Output: 'string'

# Or by string value
my_variable_type = VariableType("string")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


