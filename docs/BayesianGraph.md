# BayesianGraph

Graph in BN format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[object]** |  | [optional] 
**posterior** | **List[object]** |  | [optional] 

## Example

```python
from waylay.services.rules.models.bayesian_graph import BayesianGraph

# TODO update the JSON string below
json = "{}"
# create an instance of BayesianGraph from a JSON string
bayesian_graph_instance = BayesianGraph.from_json(json)
# print the JSON string representation of the object
print BayesianGraph.to_json()

# convert the object into a dict
bayesian_graph_dict = bayesian_graph_instance.to_dict()
# create an instance of BayesianGraph from a dict
bayesian_graph_form_dict = bayesian_graph.from_dict(bayesian_graph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


