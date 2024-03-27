# GetDiscoveryTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique template identifier | 
**discovery_template** | **bool** |  | 
**tags** | **object** | Key-value pairs on which you can filter to finding templates back | [optional] 
**variables** | [**List[VariableDeclaration]**](VariableDeclaration.md) | Variable declarations | [optional] 
**task_defaults** | [**TaskDefaultsElement**](TaskDefaultsElement.md) |  | [optional] 
**notes** | [**List[NoteElement]**](NoteElement.md) | List of notes as explanation for users | [optional] 
**user** | **str** | Creation user mail address | 
**create_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | 
**last_update_time** | **int** | Timestamp expressed as milliseconds since 00:00:00 UTC on 1 January 1970,  not counting leap seconds. | 
**sensors** | [**List[SensorNode]**](SensorNode.md) | List of sensors with required properties | [optional] 
**actuators** | [**List[ActuatorNode]**](ActuatorNode.md) | List of actuators with required properties | [optional] 
**relations** | [**List[RelationNode]**](RelationNode.md) | List of relations (gates) between sensors | [optional] 
**triggers** | [**List[SimplifiedGraphTriggersInner]**](SimplifiedGraphTriggersInner.md) | List of conditions under which actuators/sensors get executed. | [optional] 
**nodes** | **List[object]** |  | [optional] 
**posterior** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.rules.models.get_discovery_template200_response import GetDiscoveryTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscoveryTemplate200Response from a JSON string
get_discovery_template200_response_instance = GetDiscoveryTemplate200Response.from_json(json)
# print the JSON string representation of the object
print GetDiscoveryTemplate200Response.to_json()

# convert the object into a dict
get_discovery_template200_response_dict = get_discovery_template200_response_instance.to_dict()
# create an instance of GetDiscoveryTemplate200Response from a dict
get_discovery_template200_response_form_dict = get_discovery_template200_response.from_dict(get_discovery_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


