# BatchOperationAction


**Source:** `waylay.services.rules.models.batch_operation_action`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UPDATEPLUGINS** | `'updatePlugins'` |
**DELETE** | `'delete'` |
**START** | `'start'` |
**RESTART** | `'restart'` |
**STOP** | `'stop'` |
**RELOAD** | `'reload'` |
**UPDATEPROPERTIES** | `'updateProperties'` |

## Example

```python
from waylay.services.rules.models.batch_operation_action import BatchOperationAction

# Use enum by value
my_batch_operation_action = BatchOperationAction.UPDATEPLUGINS
print(my_batch_operation_action)  # Output: 'updatePlugins'

# Or by string value
my_batch_operation_action = BatchOperationAction("updatePlugins")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


