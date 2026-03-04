# BatchTaskCommandAction


**Source:** `waylay.services.rules.models.batch_task_command_action`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DELETE** | `'delete'` |
**START** | `'start'` |
**RESTART** | `'restart'` |
**STOP** | `'stop'` |
**RELOAD** | `'reload'` |
**STOPANDDELETE** | `'stopAndDelete'` |

## Example

```python
from waylay.services.rules.models.batch_task_command_action import (
    BatchTaskCommandAction,
)

# Use enum by value
my_batch_task_command_action = BatchTaskCommandAction.DELETE
print(my_batch_task_command_action)  # Output: 'delete'

# Or by string value
my_batch_task_command_action = BatchTaskCommandAction("delete")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


