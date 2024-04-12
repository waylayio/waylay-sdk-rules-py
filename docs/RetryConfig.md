# RetryConfig

Configuration for retrying a template node. The node execution will be retried `maxRetries` times. The delay between retries will be exponentially increased starting from `minBackoff` to `maxBackoff`. If the node execution fails after `maxRetries` retries, the node state will be set to `errorState` if it that property is provided. Otherwise node execution will fail. Error state should be one of the possible states defined by the sensor node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_retries** | **int** |  | 
**min_backoff** | **str** |  | 
**max_backoff** | **str** |  | 
**error_state** | **str** | Optional sensor state which will be used to set the state of the node when the maxRetries is reached. | [optional] 

## Example

```python
from waylay.services.rules.models.retry_config import RetryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RetryConfig from a JSON string
retry_config_instance = RetryConfig.from_json(json)
# print the JSON string representation of the object
print RetryConfig.to_json()

# convert the object into a dict
retry_config_dict = retry_config_instance.to_dict()
# create an instance of RetryConfig from a dict
retry_config_form_dict = retry_config.from_dict(retry_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


