# BatchTaskSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchUpdatePropertiesAllOfAction**](BatchUpdatePropertiesAllOfAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PropertyUpdatesSpec**](PropertyUpdatesSpec.md) |  | 

## Example

```python
from waylay.services.rules.models.batch_task_spec import BatchTaskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTaskSpec from a JSON string
batch_task_spec_instance = BatchTaskSpec.from_json(json)
# print the JSON string representation of the object
print BatchTaskSpec.to_json()

# convert the object into a dict
batch_task_spec_dict = batch_task_spec_instance.to_dict()
# create an instance of BatchTaskSpec from a dict
batch_task_spec_form_dict = batch_task_spec.from_dict(batch_task_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


