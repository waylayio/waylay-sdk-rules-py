# TaskWithRule


**Source:** `waylay.services.rules.models.task_with_rule`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[TriggerType]**](TriggerType.md) | List of conditions under which actuators/sensors get executed. | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) |  | [optional] 
**task** | [**TaskCreationSettings**](TaskCreationSettings.md) |  | 


## Example

```python
from waylay.services.rules.models.task_with_rule import TaskWithRule

task_with_rule = TaskWithRule(
    sensors=..., actuators=..., relations=..., triggers=..., notes=..., task=...
)

# Create from JSON
task_with_rule = TaskWithRule.from_json(
    '{ "sensors": ..., "actuators": ..., "relations": ..., "triggers": ..., "notes": ..., "task": ... }'
)

# Export to dictionary
task_with_rule_dict = task_with_rule.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


