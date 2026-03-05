# NoteElement

Representation of a note in a Rule Template.

**Source:** `waylay.services.rules.models.note_element`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **List[int]** |  | 
**text** | **str** |  | 


## Example

```python
from waylay.services.rules.models.note_element import NoteElement

note_element = NoteElement(position=..., text=...)

# Create from JSON
note_element = NoteElement.from_json('{ "position": ..., "text": ... }')

# Export to dictionary
note_element_dict = note_element.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


