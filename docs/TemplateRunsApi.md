# waylay.services.rules.TemplateRunsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_graph**](TemplateRunsApi.md#run_graph) | **POST** /rules/v1/templates/run | Run Graph Or Bayesian Network
[**run**](TemplateRunsApi.md#run) | **POST** /rules/v1/templates/{name}/run | Run Template

# **run_graph**
> run_graph(
> query: RunGraphQuery,
> headers
> ) -> AsyncIterator[TemplateRunInvocation]

Run Graph Or Bayesian Network

Run a graph or Bayesian Network. If `data` is specified, template will be run as reactive template. If `data` is not specified, template will be run as a one-time template (1 tick)

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.run_template_log_level_parameter import RunTemplateLogLevelParameter
from waylay.services.rules.models.template_run_invocation import TemplateRunInvocation
from waylay.services.rules.models.template_run_with_graph_specification import TemplateRunWithGraphSpecification
try:
    # Run Graph Or Bayesian Network
    # calls `POST /rules/v1/templates/run`
    api_response = await waylay_client.rules.template_runs.run_graph(
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TemplateRunWithGraphSpecification() # TemplateRunWithGraphSpecification | Specification to run template through graph/BN.
    )
    print("The response of rules.template_runs.run_graph:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.template_runs.run_graph: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/templates/run
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**json** | [**TemplateRunWithGraphSpecification**](TemplateRunWithGraphSpecification.md) | json request body | Specification to run template through graph/BN. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['logLevel']** (dict) <br> **query.log_level** (Query) | [**RunTemplateLogLevelParameter**](.md) | query parameter `"logLevel"` | sets the log level for filtering out logs to requested log level or higher from the template run output. Value &#x60;NONE&#x60; will disable all logs. If not specified all logs will be returned. | [optional] [default DEBUG]
**query['targetNode']** (dict) <br> **query.target_node** (Query) | [**List[str]**](str.md) | query parameter `"targetNode"` | The sensors and actuators part of response will contain only elements related to the asked node of the graph. The returned logs also will be filtered and contain only logs related to the asked node(s). | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AsyncIterator[TemplateRunInvocation]`** |  | [TemplateRunInvocation](TemplateRunInvocation.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Of Invocation Results |  -  |
**400** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run**
> run(
> name: str,
> query: RunQuery,
> headers
> ) -> AsyncIterator[TemplateRunInvocation]

Run Template

Run a template. If `data` is specified, template will be run as reactive template. If `data` is not specified, template will be run as a one-time template (1 tick)

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.run_template_log_level_parameter import RunTemplateLogLevelParameter
from waylay.services.rules.models.template_run_invocation import TemplateRunInvocation
from waylay.services.rules.models.template_run_specification import TemplateRunSpecification
try:
    # Run Template
    # calls `POST /rules/v1/templates/{name}/run`
    api_response = await waylay_client.rules.template_runs.run(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.rules.TemplateRunSpecification() # TemplateRunSpecification | Specification to run template
    )
    print("The response of rules.template_runs.run:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.template_runs.run: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/templates/{name}/run
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | Unique Template identifier | 
**json** | [**TemplateRunSpecification**](TemplateRunSpecification.md) | json request body | Specification to run template | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['logLevel']** (dict) <br> **query.log_level** (Query) | [**RunTemplateLogLevelParameter**](.md) | query parameter `"logLevel"` | sets the log level for filtering out logs to requested log level or higher from the template run output. Value &#x60;NONE&#x60; will disable all logs. If not specified all logs will be returned. | [optional] [default DEBUG]
**query['targetNode']** (dict) <br> **query.target_node** (Query) | [**List[str]**](str.md) | query parameter `"targetNode"` | The sensors and actuators part of response will contain only elements related to the asked node of the graph. The returned logs also will be filtered and contain only logs related to the asked node(s). | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AsyncIterator[TemplateRunInvocation]`** |  | [TemplateRunInvocation](TemplateRunInvocation.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-ndjson, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream Of Invocation Results |  -  |
**400** | Validation Failed |  -  |
**404** | Template Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

