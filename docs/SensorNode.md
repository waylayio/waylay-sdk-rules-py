# SensorNode

Representation of a sensor in a Rule Template.

**Source:** `waylay.services.rules.models.sensor_node`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Unique node label | 
**name** | **str** |  | 
**version** | **str** |  | 
**icon_url** | **str** | URL to an icon representing the sensor | [optional] 
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
**pause_execution** | **bool** |  | [optional] [default to False]
**pause_execution_timeout** | **str** |  | [optional] [default to 'PT1H']
**description** | **str** |  | [optional] 


## Example

```python
from waylay.services.rules.models.sensor_node import SensorNode

sensor_node = SensorNode(
    label=...,
    name=...,
    version=...,
    icon_url=...,
    properties=...,
    resource=...,
    sequence=...,
    position=...,
    data_trigger=...,
    tick_trigger=...,
    eviction_time=...,
    polling_period=...,
    schedule=...,
    timeout=...,
    timeout_state=...,
    loop_def=...,
    retry_config=...,
    pause_execution=...,
    pause_execution_timeout=...,
    description=...,
)

# Create from JSON
sensor_node = SensorNode.from_json(
    '{ "label": ..., "name": ..., "version": ..., "iconURL": ..., "properties": ..., "resource": ..., "sequence": ..., "position": ..., "dataTrigger": ..., "tickTrigger": ..., "evictionTime": ..., "pollingPeriod": ..., "schedule": ..., "timeout": ..., "timeoutState": ..., "loopDef": ..., "retryConfig": ..., "pauseExecution": ..., "pauseExecutionTimeout": ..., "description": ... }'
)

# Export to dictionary
sensor_node_dict = sensor_node.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


