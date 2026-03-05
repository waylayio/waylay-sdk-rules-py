# BayesianGraph

Graph in BN format

**Source:** `waylay.services.rules.models.bayesian_graph`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **List[object]** |  | [optional] 
**posterior** | **List[object]** |  | [optional] 


## Example

```python
from waylay.services.rules.models.bayesian_graph import BayesianGraph

bayesian_graph = BayesianGraph(nodes=..., posterior=...)

# Create from JSON
bayesian_graph = BayesianGraph.from_json('{ "nodes": ..., "posterior": ... }')

# Export to dictionary
bayesian_graph_dict = bayesian_graph.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


