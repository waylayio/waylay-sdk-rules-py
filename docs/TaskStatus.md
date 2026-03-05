# TaskStatus

Status of a task

**Source:** `waylay.services.rules.models.task_status`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**RUNNING** | `'running'` |
**PENDING** | `'pending'` |
**STOPPED** | `'stopped'` |
**FAILED** | `'failed'` |

## Example

```python
from waylay.services.rules.models.task_status import TaskStatus

# Use enum by value
my_task_status = TaskStatus.RUNNING
print(my_task_status)  # Output: 'running'

# Or by string value
my_task_status = TaskStatus("running")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


