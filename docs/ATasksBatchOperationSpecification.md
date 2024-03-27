# ATasksBatchOperationSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**BatchTaskEntity**](BatchTaskEntity.md) |  | 
**action** | [**BatchUpdatePropertiesAllOfAction**](BatchUpdatePropertiesAllOfAction.md) |  | 
**query** | [**BatchTaskQuery**](BatchTaskQuery.md) |  | 
**action_parameters** | [**PropertyUpdatesSpec**](PropertyUpdatesSpec.md) |  | 

## Example

```python
from waylay.services.rules.models.a_tasks_batch_operation_specification import ATasksBatchOperationSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ATasksBatchOperationSpecification from a JSON string
a_tasks_batch_operation_specification_instance = ATasksBatchOperationSpecification.from_json(json)
# print the JSON string representation of the object
print ATasksBatchOperationSpecification.to_json()

# convert the object into a dict
a_tasks_batch_operation_specification_dict = a_tasks_batch_operation_specification_instance.to_dict()
# create an instance of ATasksBatchOperationSpecification from a dict
a_tasks_batch_operation_specification_form_dict = a_tasks_batch_operation_specification.from_dict(a_tasks_batch_operation_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


