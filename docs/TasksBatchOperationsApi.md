# waylay.services.rules.TasksBatchOperationsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](TasksBatchOperationsApi.md#get) | **GET** /rules/v1/batch/{batchId} | Get Tasks Batch Operation Status
[**start**](TasksBatchOperationsApi.md#start) | **POST** /rules/v1/batch | Start Batch Operations

# **get**
> get(
> batch_id: str,
> headers
> ) -> GetBatchOperation200Response

Get Tasks Batch Operation Status

Get the results of the Tasks Batch Operation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.get_batch_operation200_response import GetBatchOperation200Response
try:
    # Get Tasks Batch Operation Status
    # calls `GET /rules/v1/batch/{batchId}`
    api_response = await waylay_client.rules.tasks_batch_operations.get(
        'batch_id_example', # batch_id | path param "batchId"
    )
    print("The response of rules.tasks_batch_operations.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks_batch_operations.get: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/batch/{batchId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**batch_id** | **str** | path parameter `"batchId"` | Unique Batch Operation identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`GetBatchOperation200Response`** |  | [GetBatchOperation200Response](GetBatchOperation200Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Batch Operation |  -  |
**404** | Batch Operation Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(
> headers
> ) -> BatchOperationEnqueued

Start Batch Operations

Start a batch operation.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.a_tasks_batch_operation_specification import ATasksBatchOperationSpecification
from waylay.services.rules.models.batch_operation_enqueued import BatchOperationEnqueued
try:
    # Start Batch Operations
    # calls `POST /rules/v1/batch`
    api_response = await waylay_client.rules.tasks_batch_operations.start(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = {"entity":"task","action":"delete","query":{"type":"onetime","status":"stopped","finishedBefore":1648738809733}} # ATasksBatchOperationSpecification | Tasks Batch Operation
    )
    print("The response of rules.tasks_batch_operations.start:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks_batch_operations.start: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/batch
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**ATasksBatchOperationSpecification**](ATasksBatchOperationSpecification.md) | json request body | Tasks Batch Operation | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`BatchOperationEnqueued`** |  | [BatchOperationEnqueued](BatchOperationEnqueued.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Batch Operation Started |  * Location - URI where the batch operation status can be followed <br>  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

