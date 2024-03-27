# PatchTaskNodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | State to set. Should be one of the supported states of the sensor | [optional] 
**raw_data** | **object** | rawData to set | [optional] 

## Example

```python
from waylay.services.rules.models.patch_task_node_request import PatchTaskNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTaskNodeRequest from a JSON string
patch_task_node_request_instance = PatchTaskNodeRequest.from_json(json)
# print the JSON string representation of the object
print PatchTaskNodeRequest.to_json()

# convert the object into a dict
patch_task_node_request_dict = patch_task_node_request_instance.to_dict()
# create an instance of PatchTaskNodeRequest from a dict
patch_task_node_request_form_dict = patch_task_node_request.from_dict(patch_task_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


