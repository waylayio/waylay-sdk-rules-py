# ValidationIssue


**Source:** `waylay.services.rules.models.validation_issue`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indication of \&quot;area\&quot; where validation issue is situated | 
**message** | **str** | Description of the issue | 
**severity** | [**ValidationIssueSeverity**](ValidationIssueSeverity.md) |  | 
**details** | **object** | Object containing identifying information on what gives the issue | [optional] 
**suggestion** | **str** | Suggestion on how to change the object to get the issue fixed | [optional] 


## Example

```python
from waylay.services.rules.models.validation_issue import ValidationIssue

validation_issue = ValidationIssue(
    type=..., message=..., severity=..., details=..., suggestion=...
)

# Create from JSON
validation_issue = ValidationIssue.from_json(
    '{ "type": ..., "message": ..., "severity": ..., "details": ..., "suggestion": ... }'
)

# Export to dictionary
validation_issue_dict = validation_issue.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


