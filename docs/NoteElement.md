# NoteElement

Representation of a note in a Rule Template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **List[int]** |  | 
**text** | **str** |  | 

## Example

```python
from waylay.services.rules.models.note_element import NoteElement

# TODO update the JSON string below
json = "{}"
# create an instance of NoteElement from a JSON string
note_element_instance = NoteElement.from_json(json)
# print the JSON string representation of the object
print NoteElement.to_json()

# convert the object into a dict
note_element_dict = note_element_instance.to_dict()
# create an instance of NoteElement from a dict
note_element_form_dict = note_element.from_dict(note_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


