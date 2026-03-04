# LogEntry


**Source:** `waylay.services.rules.models.log_entry`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** |  | 
**level** | [**LogEntryLevel**](LogEntryLevel.md) |  | 
**message** | **str** |  | 


## Example

```python
from waylay.services.rules.models.log_entry import LogEntry

log_entry = LogEntry(time=..., level=..., message=...)

# Create from JSON
log_entry = LogEntry.from_json('{ "time": ..., "level": ..., "message": ... }')

# Export to dictionary
log_entry_dict = log_entry.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


