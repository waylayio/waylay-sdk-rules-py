# ValidationIssue


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

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationIssue from a JSON string
validation_issue_instance = ValidationIssue.from_json(json)
# print the JSON string representation of the object
print ValidationIssue.to_json()

# convert the object into a dict
validation_issue_dict = validation_issue_instance.to_dict()
# create an instance of ValidationIssue from a dict
validation_issue_form_dict = validation_issue.from_dict(validation_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


