# waylay.services.rules.PushDataApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**push**](PushDataApi.md#push) | **POST** /rules/v1/data | Push Streaming Data

# **push**
> push(
> headers
> ) -> object

Push Streaming Data

Push (real-time) streaming data.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.stream_data import StreamData
try:
    # Push Streaming Data
    # calls `POST /rules/v1/data`
    api_response = await waylay_client.rules.push_data.push(
    )
    print("The response of rules.push_data.push:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.push_data.push: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/data
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`object`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

