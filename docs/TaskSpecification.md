# TaskSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**resource** | **str** | Unique resource identifier | [optional] 
**reset_observations** | **bool** |  | [optional] [default to True]
**parallel** | **bool** |  | [optional] [default to True]
**gates_need_full_observation** | **bool** |  | [optional] [default to False]
**tags** | **object** | Key-value pairs on which you can set at task creation and later filter tasks | [optional] 
**variables** | **object** | set of variables which will be used when starting a task and will automatically be injected in the template before starting a task. | [optional] 
**type** | [**ReactiveTaskSettingType**](ReactiveTaskSettingType.md) |  | 
**time_zone** | **str** | Optional identifier of the time zone in which the schedule expression is to be interpreted | [optional] 
**frequency** | **int** | polling frequency in milliseconds | [optional] 
**start** | **bool** |  | [optional] [default to True]
**template** | **str** | Unique template identifier | 
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) |  | [optional] 
**task** | [**TaskWithRuleAllOfTask**](TaskWithRuleAllOfTask.md) |  | 

## Example

```python
from waylay.services.rules.models.task_specification import TaskSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSpecification from a JSON string
task_specification_instance = TaskSpecification.from_json(json)
# print the JSON string representation of the object
print TaskSpecification.to_json()

# convert the object into a dict
task_specification_dict = task_specification_instance.to_dict()
# create an instance of TaskSpecification from a dict
task_specification_form_dict = task_specification.from_dict(task_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


