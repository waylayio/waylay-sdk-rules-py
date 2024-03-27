# TransformerExecutionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | flag indicating if the actuator was Successfully Executed | [optional] 
**error** | **str** | error message in case of failure | [optional] 
**data** | **object** |  | [optional] 
**log** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.rules.models.transformer_execution_result import TransformerExecutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransformerExecutionResult from a JSON string
transformer_execution_result_instance = TransformerExecutionResult.from_json(json)
# print the JSON string representation of the object
print TransformerExecutionResult.to_json()

# convert the object into a dict
transformer_execution_result_dict = transformer_execution_result_instance.to_dict()
# create an instance of TransformerExecutionResult from a dict
transformer_execution_result_form_dict = transformer_execution_result.from_dict(transformer_execution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


