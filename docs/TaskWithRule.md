# TaskWithRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) |  | [optional] 
**task** | [**TaskWithRuleAllOfTask**](TaskWithRuleAllOfTask.md) |  | 

## Example

```python
from waylay.services.rules.models.task_with_rule import TaskWithRule

# TODO update the JSON string below
json = "{}"
# create an instance of TaskWithRule from a JSON string
task_with_rule_instance = TaskWithRule.from_json(json)
# print the JSON string representation of the object
print TaskWithRule.to_json()

# convert the object into a dict
task_with_rule_dict = task_with_rule_instance.to_dict()
# create an instance of TaskWithRule from a dict
task_with_rule_form_dict = task_with_rule.from_dict(task_with_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


