# ValidationIssueSeverity

Severity of the issue. ERROR means that object cannot be created if the issue is not fixed. WARNING means that the object can be created, but that errors might be encountered at runtime

**Source:** `waylay.services.rules.models.validation_issue_severity`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ERROR** | `'ERROR'` |
**WARNING** | `'WARNING'` |

## Example

```python
from waylay.services.rules.models.validation_issue_severity import (
    ValidationIssueSeverity,
)

# Use enum by value
my_validation_issue_severity = ValidationIssueSeverity.ERROR
print(my_validation_issue_severity)  # Output: 'ERROR'

# Or by string value
my_validation_issue_severity = ValidationIssueSeverity("ERROR")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


