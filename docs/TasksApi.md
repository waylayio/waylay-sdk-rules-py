# waylay.services.rules.TasksApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TasksApi.md#create) | **POST** /rules/v1/tasks | Create Task
[**delete**](TasksApi.md#delete) | **DELETE** /rules/v1/tasks/{taskId} | Delete Task
[**get_configuration**](TasksApi.md#get_configuration) | **GET** /rules/v1/tasks/{taskId}/conf | Get Task Configuration
[**get**](TasksApi.md#get) | **GET** /rules/v1/tasks/{taskId} | Retrieve Task Details
[**list**](TasksApi.md#list) | **GET** /rules/v1/tasks | Query Multiple Tasks
[**replace**](TasksApi.md#replace) | **PUT** /rules/v1/tasks/{taskId} | Update Task
[**start**](TasksApi.md#start) | **POST** /rules/v1/tasks/{taskId}/command/start | Start Task
[**stop**](TasksApi.md#stop) | **POST** /rules/v1/tasks/{taskId}/command/stop | Stop Task

# **create**
> create(
> query: CreateQuery,
> headers
> ) -> CreateTask201Response

Create Task

Create a new task.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.create_task201_response import CreateTask201Response
from waylay.services.rules.models.task_specification import TaskSpecification
try:
    # Create Task
    # calls `POST /rules/v1/tasks`
    api_response = await waylay_client.rules.tasks.create(
        # query parameters:
        query = {
            'failOnWarning': False
            'returnWarnings': False
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TaskSpecification() # TaskSpecification | Task Specification
    )
    print("The response of rules.tasks.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.create: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/tasks
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**TaskSpecification**](TaskSpecification.md) | json request body | Task Specification | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['failOnWarning']** (dict) <br> **query.fail_on_warning** (Query) | **bool** | query parameter `"failOnWarning"` | If &#x60;true&#x60; and there are task warnings, the response will be a &#x60;400 Validation failed&#x60; | [optional] [default False]
**query['returnWarnings']** (dict) <br> **query.return_warnings** (Query) | **bool** | query parameter `"returnWarnings"` | If &#x60;true&#x60;, result body will contain a list of task warnings that where detected | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`CreateTask201Response`** |  | [CreateTask201Response](CreateTask201Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task Created |  * Location - URI where the created Template can be fetched <br>  |
**400** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> task_id: str,
> headers
> ) -> void (empty response body)

Delete Task

Delete a task.

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
    # Delete Task
    # calls `DELETE /rules/v1/tasks/{taskId}`
    await waylay_client.rules.tasks.delete(
        'task_id_example', # task_id | path param "taskId"
    )
except ApiError as e:
    print("Exception when calling rules.tasks.delete: %s\n" % e)
```

### Endpoint
```
DELETE /rules/v1/tasks/{taskId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | void (empty response body) |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Task Deleted |  -  |
**400** | Error Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> get_configuration(
> task_id: str,
> query: GetConfigurationQuery,
> headers
> ) -> TaskSpecification

Get Task Configuration

Getting the configuration of an existing task.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.list_tasks_format_parameter import ListTasksFormatParameter
from waylay.services.rules.models.task_specification import TaskSpecification
try:
    # Get Task Configuration
    # calls `GET /rules/v1/tasks/{taskId}/conf`
    api_response = await waylay_client.rules.tasks.get_configuration(
        'task_id_example', # task_id | path param "taskId"
        # query parameters:
        query = {
        },
    )
    print("The response of rules.tasks.get_configuration:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.get_configuration: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/tasks/{taskId}/conf
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['format']** (dict) <br> **query.format** (Query) | [**ListTasksFormatParameter**](.md) | query parameter `"format"` | Format of the graph definition | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TaskSpecification`** |  | [TaskSpecification](TaskSpecification.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Configuration |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> task_id: str,
> query: GetQuery,
> headers
> ) -> TaskEntity

Retrieve Task Details

Retrieve the details of a task.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.list_tasks_format_parameter import ListTasksFormatParameter
from waylay.services.rules.models.task_entity import TaskEntity
try:
    # Retrieve Task Details
    # calls `GET /rules/v1/tasks/{taskId}`
    api_response = await waylay_client.rules.tasks.get(
        'task_id_example', # task_id | path param "taskId"
        # query parameters:
        query = {
        },
    )
    print("The response of rules.tasks.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.get: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/tasks/{taskId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['format']** (dict) <br> **query.format** (Query) | [**ListTasksFormatParameter**](.md) | query parameter `"format"` | Format of the graph definition | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TaskEntity`** |  | [TaskEntity](TaskEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Details |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> List[TaskEntity]

Query Multiple Tasks

Query multiple tasks.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.list_tasks_format_parameter import ListTasksFormatParameter
from waylay.services.rules.models.task_entity import TaskEntity
from waylay.services.rules.models.task_scenario_type import TaskScenarioType
from waylay.services.rules.models.task_status import TaskStatus
try:
    # Query Multiple Tasks
    # calls `GET /rules/v1/tasks`
    api_response = await waylay_client.rules.tasks.list(
        # query parameters:
        query = {
            'resource': 'resource_example'
            'resourceType': 'resource_type_example'
            'type': 'scheduled'
            'status': 'running'
            'id': 'id_example'
            'tags.key': 3904859080956
            'finishedBefore': 56
            'createdAfter': 1661990400000
            'createdBefore': 1662768000000
        },
    )
    print("The response of rules.tasks.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.list: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/tasks
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['hits']** (dict) <br> **query.hits** (Query) | **int** | query parameter `"hits"` | (Paging) maximal number of items returned | [optional] [default 10]
**query['startIndex']** (dict) <br> **query.start_index** (Query) | **int** | query parameter `"startIndex"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['format']** (dict) <br> **query.format** (Query) | [**ListTasksFormatParameter**](.md) | query parameter `"format"` | Format of the graph definition | [optional] 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` |  | [optional] 
**query['resource']** (dict) <br> **query.resource** (Query) | **str** | query parameter `"resource"` |  | [optional] 
**query['resourceType']** (dict) <br> **query.resource_type** (Query) | **str** | query parameter `"resourceType"` |  | [optional] 
**query['type']** (dict) <br> **query.type** (Query) | [**TaskScenarioType**](.md) | query parameter `"type"` |  | [optional] 
**query['status']** (dict) <br> **query.status** (Query) | [**TaskStatus**](.md) | query parameter `"status"` |  | [optional] 
**query['ids']** (dict) <br> **query.ids** (Query) | [**List[str]**](str.md) | query parameter `"ids"` |  | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | **str** | query parameter `"id"` |  | [optional] 
**query['plugin']** (dict) <br> **query.plugin** (Query) | **str** | query parameter `"plugin"` |  | [optional] 
**query['template']** (dict) <br> **query.template** (Query) | **str** | query parameter `"template"` |  | [optional] 
**query['filter']** (dict) <br> **query.filter** (Query) | **str** | query parameter `"filter"` | fuzzy search on multiple properties | [optional] 
**query['tags.key']** (dict) <br> **query.tags_key** (Query) | [**ListTasksTagsKeyParameter**](.md) | query parameter `"tags.key"` | Parameter is &#x60;form&#x60; style serialized, with explode: true  See [Query multiple tasks tag examples](/#/api/rules/?id&#x3D;queryTagExamples)  You can add the same tag query parameter multiple times with different values, which will be applied with a logical OR.  You can specify the &#x60;tags.&lt;key&gt;&#x60; query parameter without a value, tasks which have a value for tag &#x60;&lt;key&gt;&#x60; will be returned | [optional] 
**query['finishedBefore']** (dict) <br> **query.finished_before** (Query) | **int** | query parameter `"finishedBefore"` | Tasks stopped before provided time will be returned. | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | **int** | query parameter `"createdAfter"` | Tasks created after provided time will be returned. | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | **int** | query parameter `"createdBefore"` | Tasks created before provided time will be returned | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[TaskEntity]`** |  | [List[TaskEntity]](TaskEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.waylay.paged+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Count - Total number of templates that fulfill the query. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> task_id: str,
> headers
> ) -> TaskEntity

Update Task

Update a task.  Remark that the full specification of the task must be given

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.task_entity import TaskEntity
from waylay.services.rules.models.task_specification import TaskSpecification
try:
    # Update Task
    # calls `PUT /rules/v1/tasks/{taskId}`
    api_response = await waylay_client.rules.tasks.replace(
        'task_id_example', # task_id | path param "taskId"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TaskSpecification() # TaskSpecification | Task Specification
    )
    print("The response of rules.tasks.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.replace: %s\n" % e)
```

### Endpoint
```
PUT /rules/v1/tasks/{taskId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**json** | [**TaskSpecification**](TaskSpecification.md) | json request body | Task Specification | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TaskEntity`** |  | [TaskEntity](TaskEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Updated |  -  |
**400** | Validation Error |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(
> task_id: str,
> headers
> ) -> TaskEntity

Start Task

Start a task.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.task_entity import TaskEntity
try:
    # Start Task
    # calls `POST /rules/v1/tasks/{taskId}/command/start`
    api_response = await waylay_client.rules.tasks.start(
        'task_id_example', # task_id | path param "taskId"
    )
    print("The response of rules.tasks.start:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.start: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/tasks/{taskId}/command/start
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TaskEntity`** |  | [TaskEntity](TaskEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Started |  -  |
**400** | Task Cannot Be Started |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(
> task_id: str,
> headers
> ) -> TaskEntity

Stop Task

Stop a task.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.task_entity import TaskEntity
try:
    # Stop Task
    # calls `POST /rules/v1/tasks/{taskId}/command/stop`
    api_response = await waylay_client.rules.tasks.stop(
        'task_id_example', # task_id | path param "taskId"
    )
    print("The response of rules.tasks.stop:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.tasks.stop: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/tasks/{taskId}/command/stop
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**task_id** | **str** | path parameter `"taskId"` | Unique Task identifier | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TaskEntity`** |  | [TaskEntity](TaskEntity.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task Stopped |  -  |
**400** | Task Cannot Be Stopped |  -  |
**404** | Task Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

