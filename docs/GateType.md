# GateType

Supported gate types.

**Source:** `waylay.services.rules.models.gate_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**AND** | `'AND'` |
**OR** | `'OR'` |
**GENERAL** | `'GENERAL'` |
**NAND** | `'NAND'` |

## Example

```python
from waylay.services.rules.models.gate_type import GateType

# Use enum by value
my_gate_type = GateType.AND
print(my_gate_type)  # Output: 'AND'

# Or by string value
my_gate_type = GateType("AND")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


