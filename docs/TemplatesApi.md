# waylay.services.rules.TemplatesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TemplatesApi.md#create) | **POST** /rules/v1/templates | Create Template
[**delete**](TemplatesApi.md#delete) | **DELETE** /rules/v1/templates/{name} | Delete Template
[**get_discovery**](TemplatesApi.md#get_discovery) | **GET** /rules/v1/discoveryTemplate | Retrieve Discovery Template
[**get**](TemplatesApi.md#get) | **GET** /rules/v1/templates/{name} | Retrieve Template Details
[**list**](TemplatesApi.md#list) | **GET** /rules/v1/templates | List Templates
[**replace**](TemplatesApi.md#replace) | **PUT** /rules/v1/templates/{name} | Update Template
[**set**](TemplatesApi.md#set) | **PUT** /rules/v1/discoveryTemplate | Set Discovery Template
[**upgrade_plugins**](TemplatesApi.md#upgrade_plugins) | **PATCH** /rules/v1/templates | Upgrade Plugins

# **create**
> create(
> headers
> ) -> CreateTemplate201Response

Create Template

Create a template.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.create_template201_response import CreateTemplate201Response
from waylay.services.rules.models.template_entity import TemplateEntity
try:
    # Create Template
    # calls `POST /rules/v1/templates`
    api_response = await waylay_client.rules.templates.create(
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TemplateEntity() # TemplateEntity | Template Specification
    )
    print("The response of rules.templates.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.create: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/templates
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**TemplateEntity**](TemplateEntity.md) | json request body | Template Specification | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`CreateTemplate201Response`** |  | [CreateTemplate201Response](CreateTemplate201Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template Created |  * Location - URI where the created Template can be fetched <br>  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(
> name: str,
> headers
> ) -> void (empty response body)

Delete Template

Delete a template.

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
    # Delete Template
    # calls `DELETE /rules/v1/templates/{name}`
    await waylay_client.rules.templates.delete(
        'name_example', # name | path param "name"
    )
except ApiError as e:
    print("Exception when calling rules.templates.delete: %s\n" % e)
```

### Endpoint
```
DELETE /rules/v1/templates/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | Unique Template identifier | 
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
**204** | Template Deleted |  -  |
**400** | Template Still In Use |  -  |
**404** | Template Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery**
> get_discovery(
> headers
> ) -> TemplateDetails \| None

Retrieve Discovery Template

Get the discovery template.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.template_details import TemplateDetails
try:
    # Retrieve Discovery Template
    # calls `GET /rules/v1/discoveryTemplate`
    api_response = await waylay_client.rules.templates.get_discovery(
    )
    print("The response of rules.templates.get_discovery:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.get_discovery: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/discoveryTemplate
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TemplateDetails \| None`** |  | [TemplateDetails](TemplateDetails.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Template Details |  -  |
**204** | No Discovery Template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> name: str,
> query: GetQuery,
> headers
> ) -> TemplateDetails

Retrieve Template Details

Retrieve the details of a template.

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
from waylay.services.rules.models.template_details import TemplateDetails
try:
    # Retrieve Template Details
    # calls `GET /rules/v1/templates/{name}`
    api_response = await waylay_client.rules.templates.get(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
        },
    )
    print("The response of rules.templates.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.get: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/templates/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | Unique Template identifier | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['format']** (dict) <br> **query.format** (Query) | [**ListTasksFormatParameter**](.md) | query parameter `"format"` | Format of the graph definition | [optional] [default bn]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TemplateDetails`** |  | [TemplateDetails](TemplateDetails.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template Details |  -  |
**404** | Template Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> List[TemplateEntityMetadata]

List Templates

Query templates.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.template_entity_metadata import TemplateEntityMetadata
try:
    # List Templates
    # calls `GET /rules/v1/templates`
    api_response = await waylay_client.rules.templates.list(
        # query parameters:
        query = {
            'id': 'id_example'
            'plugin': 'mySensor:1.0.3'
            'tags.X': 'tags.myref: 3904859080956'
        },
    )
    print("The response of rules.templates.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.list: %s\n" % e)
```

### Endpoint
```
GET /rules/v1/templates
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['hits']** (dict) <br> **query.hits** (Query) | **int** | query parameter `"hits"` | (Paging) maximal number of items returned | [optional] [default 10]
**query['startIndex']** (dict) <br> **query.start_index** (Query) | **int** | query parameter `"startIndex"` | (Paging) items to skip in the listing | [optional] [default 0]
**query['filter']** (dict) <br> **query.filter** (Query) | **str** | query parameter `"filter"` | fuzzy search on multiple properties | [optional] 
**query['ids']** (dict) <br> **query.ids** (Query) | [**List[str]**](str.md) | query parameter `"ids"` | comma separated string of template names | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | **str** | query parameter `"id"` | filter on template name | [optional] 
**query['plugin']** (dict) <br> **query.plugin** (Query) | **str** | query parameter `"plugin"` | either name of a plugin (e.g. &#x60;mySensor&#x60;), or full version specification of the plug (e.g &#x60;mySensor:1.0.3&#x60;) | [optional] 
**query['tags.X']** (dict) <br> **query.tags_x** (Query) | **str** | query parameter `"tags.X"` |  | [optional] 
**query['tags']** (dict) <br> **query.tags** (Query) | [**List[str]**](str.md) | query parameter `"tags"` | Filter templates that have one of the tag keys in the array | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`List[TemplateEntityMetadata]`** |  | [List[TemplateEntityMetadata]](TemplateEntityMetadata.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  * X-Count - Total number of templates that fulfill the query. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> name: str,
> headers
> ) -> ReplaceTemplate200Response

Update Template

Update a template. Note that this will not update any tasks using the template. You will need to do a batch reload operation on the tasks to accomplish that.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.replace_template200_response import ReplaceTemplate200Response
from waylay.services.rules.models.template_entity import TemplateEntity
try:
    # Update Template
    # calls `PUT /rules/v1/templates/{name}`
    api_response = await waylay_client.rules.templates.replace(
        'name_example', # name | path param "name"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TemplateEntity() # TemplateEntity | Template Specification
    )
    print("The response of rules.templates.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.replace: %s\n" % e)
```

### Endpoint
```
PUT /rules/v1/templates/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | Unique Template identifier | 
**json** | [**TemplateEntity**](TemplateEntity.md) | json request body | Template Specification | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ReplaceTemplate200Response`** |  | [ReplaceTemplate200Response](ReplaceTemplate200Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template Updated |  -  |
**400** | Validation Failed |  -  |
**404** | Template Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set**
> set(
> query: SetQuery,
> headers
> ) -> TemplateDetails \| None

Set Discovery Template

Set the discovery template.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.template_details import TemplateDetails
try:
    # Set Discovery Template
    # calls `PUT /rules/v1/discoveryTemplate`
    api_response = await waylay_client.rules.templates.set(
        # query parameters:
        query = {
            'name': 'discoverResourceType'
        },
    )
    print("The response of rules.templates.set:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.set: %s\n" % e)
```

### Endpoint
```
PUT /rules/v1/discoveryTemplate
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | The template to set as discovery template. If you do not specify this parameter, the current discovery template will be cleared. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TemplateDetails \| None`** |  | [TemplateDetails](TemplateDetails.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discovery Template Set |  -  |
**204** | Discovery Template Cleared |  -  |
**404** | Template Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_plugins**
> upgrade_plugins(
> query: UpgradePluginsQuery,
> headers
> ) -> UpgradePluginsTemplates200Response

Upgrade Plugins

Upgrade plugins on multiple templates.  The plugin upgrades specified in the body will be applied to all template that fullfil the query expresses by the query parameters. At least one of the query parameters must be specified.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.template_modification import TemplateModification
from waylay.services.rules.models.upgrade_plugins_templates200_response import UpgradePluginsTemplates200Response
try:
    # Upgrade Plugins
    # calls `PATCH /rules/v1/templates`
    api_response = await waylay_client.rules.templates.upgrade_plugins(
        # query parameters:
        query = {
            'id': 'id_example'
            'plugin': '{\"plugin\":\"mySensor:1.0.3\"}'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TemplateModification() # TemplateModification | Plugin Update Specifications
    )
    print("The response of rules.templates.upgrade_plugins:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.templates.upgrade_plugins: %s\n" % e)
```

### Endpoint
```
PATCH /rules/v1/templates
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**TemplateModification**](TemplateModification.md) | json request body | Plugin Update Specifications | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ids']** (dict) <br> **query.ids** (Query) | [**List[str]**](str.md) | query parameter `"ids"` | comma separated string of template names | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | **str** | query parameter `"id"` | filter on template name | [optional] 
**query['plugin']** (dict) <br> **query.plugin** (Query) | **str** | query parameter `"plugin"` | either name of a plugin (e.g. &#x60;mySensor&#x60;), or full version specification of the plug (e.g &#x60;mySensor:1.0.3&#x60;) | [optional] 
**query['tags.X']** (dict) <br> **query.tags_x** (Query) | **str** | query parameter `"tags.X"` |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`UpgradePluginsTemplates200Response`** |  | [UpgradePluginsTemplates200Response](UpgradePluginsTemplates200Response.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Updated |  -  |
**400** | Unsuccessful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

