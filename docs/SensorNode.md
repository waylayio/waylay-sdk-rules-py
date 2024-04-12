# SensorNode

Representation of a sensor in a Rule Template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Unique node label | 
**name** | **str** |  | 
**version** | **str** |  | 
**properties** | **object** |  | [optional] 
**resource** | **str** | Unique resource identifier | [optional] 
**sequence** | **int** |  | [optional] [default to 1]
**position** | **List[int]** |  | [optional] 
**data_trigger** | **bool** |  | [optional] [default to True]
**tick_trigger** | **bool** |  | [optional] [default to True]
**eviction_time** | **int** |  | [optional] 
**polling_period** | **int** |  | [optional] 
**schedule** | **str** | Either a valid cron or RRule expression to set the sensor&#39;s own tick | [optional] 
**timeout** | **str** |  | [optional] [default to 'PT50S']
**timeout_state** | **str** |  | [optional] 
**loop_def** | **str** | A loop definition is a string that defines items over which node will be iterated multiple times. The string is an JSON array of JSON objects.During template execution the sensor node with such a defined loop definition will be invoked for every JSON Object in the JSON array. Parameter is optional. Node will be executed only once if loop definition is not defined. | [optional] 
**retry_config** | [**RetryConfig**](RetryConfig.md) |  | [optional] 

## Example

```python
from waylay.services.rules.models.sensor_node import SensorNode

# TODO update the JSON string below
json = "{}"
# create an instance of SensorNode from a JSON string
sensor_node_instance = SensorNode.from_json(json)
# print the JSON string representation of the object
print SensorNode.to_json()

# convert the object into a dict
sensor_node_dict = sensor_node_instance.to_dict()
# create an instance of SensorNode from a dict
sensor_node_form_dict = sensor_node.from_dict(sensor_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


