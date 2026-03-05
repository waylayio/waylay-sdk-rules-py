# RRuleSchedule


**Source:** `waylay.services.rules.models.r_rule_schedule`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rrule** | **str** | RRule expression as defined in [RFC5545 3.8.5.3](https://www.rfc-editor.org/rfc/rfc5545#section-3.8.5.3) | 


## Example

```python
from waylay.services.rules.models.r_rule_schedule import RRuleSchedule

r_rule_schedule = RRuleSchedule(rrule=...)

# Create from JSON
r_rule_schedule = RRuleSchedule.from_json('{ "rrule": ... }')

# Export to dictionary
r_rule_schedule_dict = r_rule_schedule.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


