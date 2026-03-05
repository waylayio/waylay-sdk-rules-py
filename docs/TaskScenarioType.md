# TaskScenarioType

Triggering deployment scenario for a task.

**Source:** `waylay.services.rules.models.task_scenario_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**SCHEDULED** | `'scheduled'` |
**PERIODIC** | `'periodic'` |
**ONETIME** | `'onetime'` |
**REACTIVE** | `'reactive'` |

## Example

```python
from waylay.services.rules.models.task_scenario_type import TaskScenarioType

# Use enum by value
my_task_scenario_type = TaskScenarioType.SCHEDULED
print(my_task_scenario_type)  # Output: 'scheduled'

# Or by string value
my_task_scenario_type = TaskScenarioType("scheduled")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


