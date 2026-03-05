# TemplateRunSpecification


**Source:** `waylay.services.rules.models.template_run_specification`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[List[ResourceDataInjection]]** | The full dataset to process. If specified, template will be run as reactive template | [optional] 
**conf** | [**TemplateRunConfiguration**](TemplateRunConfiguration.md) |  | [optional] 
**variables** | **object** | The values for the variables declared in the template | [optional] 
**nodes_raw_data** | **object** | The input data for the template execution. The data is used to inject the actual data into the template execution nodes map. | [optional] 
**resource_meta_data** | **Dict[str, object]** | Metadata for any of the resources used in the template.  The current metadata for all resources used in the template is fetched at the start of the template run. This provided metadata is used to overwrite this current metadata | [optional] 


## Example

```python
from waylay.services.rules.models.template_run_specification import (
    TemplateRunSpecification,
)

template_run_specification = TemplateRunSpecification(
    data=..., conf=..., variables=..., nodes_raw_data=..., resource_meta_data=...
)

# Create from JSON
template_run_specification = TemplateRunSpecification.from_json(
    '{ "data": ..., "conf": ..., "variables": ..., "nodesRawData": ..., "resourceMetaData": ... }'
)

# Export to dictionary
template_run_specification_dict = template_run_specification.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


