# waylay.services.rules.TaskNodesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_states**](TaskNodesApi.md#get_states) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId}/states | Get Supported States
[**get**](TaskNodesApi.md#get) | **GET** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Get Current States
[**patch**](TaskNodesApi.md#patch) | **PATCH** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Node State
[**update**](TaskNodesApi.md#update) | **POST** /rules/v1/tasks/{taskId}/nodes/{nodeId} | Set Current State

# **get_states**
> get_states(
> task_id: str,
> node_id: str,
> headers
> ) -> object

Get Supported States

Get the supported states of a node.  #### visibility This definition has visibility status `deprecated`. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
try:
    # Get Supported States
    # calls `GET /rules/v1/tasks/{taskId}/nodes/{nodeId}/states`
    api_response = await waylay_client.rules.task_nodes.get_states(
        'task_id_example', # task_id | path param "taskId"
        'node_id_example', # node_id | path param "nodeId"
    )
    print("The response of rules.task_nodes.get_states:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.task_nodes.get_states: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/tasks/{taskId}/nodes/{nodeId}/states
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**node_id** | **str** | path parameter `"nodeId"` | Unique node label | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`object`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> task_id: str,
> node_id: str,
> headers
> ) -> object

Get Current States

Get current states (posteriors) and raw data of the node.  #### visibility This definition has visibility status `deprecated`. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
try:
    # Get Current States
    # calls `GET /rules/v1/tasks/{taskId}/nodes/{nodeId}`
    api_response = await waylay_client.rules.task_nodes.get(
        'task_id_example', # task_id | path param "taskId"
        'node_id_example', # node_id | path param "nodeId"
    )
    print("The response of rules.task_nodes.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.task_nodes.get: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/tasks/{taskId}/nodes/{nodeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**node_id** | **str** | path parameter `"nodeId"` | Unique node label | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`object`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> patch(
> task_id: str,
> node_id: str,
> headers
> ) -> object

Set Node State

Set the current state and rawData for the node. This can only be done for a running task

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.node_state_specification import NodeStateSpecification
try:
    # Set Node State
    # calls `PATCH /rules/v1/tasks/{taskId}/nodes/{nodeId}`
    api_response = await waylay_client.rules.task_nodes.patch(
        'task_id_example', # task_id | path param "taskId"
        'node_id_example', # node_id | path param "nodeId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.NodeStateSpecification() # NodeStateSpecification | 
    )
    print("The response of rules.task_nodes.patch:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.task_nodes.patch: %s\n" % e)
```

### Endpoint
```
PATCH /rules/v1/tasks/{taskId}/nodes/{nodeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**node_id** | **str** | path parameter `"nodeId"` | Unique node label | 
**json** | [**NodeStateSpecification**](NodeStateSpecification.md) | json request body |  | 
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
**400** | Validation Error |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(
> task_id: str,
> node_id: str,
> headers
> ) -> object

Set Current State

Set the current state of the node.  This call is deprecated. Please use `PATCH /rules/v1/tasks/{taskId}/nodes/{nodeId}`  #### visibility This definition has visibility status `deprecated`. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
try:
    # Set Current State
    # calls `POST /rules/v1/tasks/{taskId}/nodes/{nodeId}`
    api_response = await waylay_client.rules.task_nodes.update(
        'task_id_example', # task_id | path param "taskId"
        'node_id_example', # node_id | path param "nodeId"
    )
    print("The response of rules.task_nodes.update:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.task_nodes.update: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/tasks/{taskId}/nodes/{nodeId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**node_id** | **str** | path parameter `"nodeId"` | Unique node label | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`object`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

