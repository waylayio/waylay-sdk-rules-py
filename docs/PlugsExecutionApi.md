# waylay.services.rules.PlugsExecutionApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_actuator**](PlugsExecutionApi.md#execute_actuator) | **POST** /rules/v1/actions/{name} | Execute Latest Actuator Version
[**execute_actuator_version**](PlugsExecutionApi.md#execute_actuator_version) | **POST** /rules/v1/actions/{name}/versions/{version} | Execute Specified Actuator Version
[**execute_sensor**](PlugsExecutionApi.md#execute_sensor) | **POST** /rules/v1/sensors/{name} | Execute Latest Sensor Version
[**execute_sensor_version**](PlugsExecutionApi.md#execute_sensor_version) | **POST** /rules/v1/sensors/{name}/versions/{version} | Execute Specified Sensor Version
[**execute_transformer**](PlugsExecutionApi.md#execute_transformer) | **POST** /rules/v1/transformers/{name} | Execute Latest Transformer Version
[**execute_transformer_version**](PlugsExecutionApi.md#execute_transformer_version) | **POST** /rules/v1/transformers/{name}/versions/{version} | Execute Specified Transformer Version

# **execute_actuator**
> execute_actuator(
> name: str,
> headers
> ) -> ActuatorExecutionResult

Execute Latest Actuator Version

Execute latest version of an actuator.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.actuator_execution_result import ActuatorExecutionResult
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
try:
    # Execute Latest Actuator Version
    # calls `POST /rules/v1/actions/{name}`
    api_response = await waylay_client.rules.plugs_execution.execute_actuator(
        'name_example', # name | path param "name"
    )
    print("The response of rules.plugs_execution.execute_actuator:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_actuator: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/actions/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ActuatorExecutionResult`** |  | [ActuatorExecutionResult](ActuatorExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Actuator Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_actuator_version**
> execute_actuator_version(
> name: str,
> version: str,
> headers
> ) -> ActuatorExecutionResult

Execute Specified Actuator Version

Execute specified version of an actuator.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.actuator_execution_result import ActuatorExecutionResult
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
try:
    # Execute Specified Actuator Version
    # calls `POST /rules/v1/actions/{name}/versions/{version}`
    api_response = await waylay_client.rules.plugs_execution.execute_actuator_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of rules.plugs_execution.execute_actuator_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_actuator_version: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/actions/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**version** | **str** | path parameter `"version"` | Version number of plugin | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`ActuatorExecutionResult`** |  | [ActuatorExecutionResult](ActuatorExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Actuator Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_sensor**
> execute_sensor(
> name: str,
> headers
> ) -> SensorExecutionResult

Execute Latest Sensor Version

Execute latest version of a sensor.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
from waylay.services.rules.models.sensor_execution_result import SensorExecutionResult
try:
    # Execute Latest Sensor Version
    # calls `POST /rules/v1/sensors/{name}`
    api_response = await waylay_client.rules.plugs_execution.execute_sensor(
        'name_example', # name | path param "name"
    )
    print("The response of rules.plugs_execution.execute_sensor:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_sensor: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/sensors/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SensorExecutionResult`** |  | [SensorExecutionResult](SensorExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Sensor Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_sensor_version**
> execute_sensor_version(
> name: str,
> version: str,
> headers
> ) -> SensorExecutionResult

Execute Specified Sensor Version

Execute the specified version of a sensor.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
from waylay.services.rules.models.sensor_execution_result import SensorExecutionResult
try:
    # Execute Specified Sensor Version
    # calls `POST /rules/v1/sensors/{name}/versions/{version}`
    api_response = await waylay_client.rules.plugs_execution.execute_sensor_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of rules.plugs_execution.execute_sensor_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_sensor_version: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/sensors/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**version** | **str** | path parameter `"version"` | Version number of plugin | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`SensorExecutionResult`** |  | [SensorExecutionResult](SensorExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Sensor Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_transformer**
> execute_transformer(
> name: str,
> headers
> ) -> TransformerExecutionResult

Execute Latest Transformer Version

Execute the latest transformer version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
from waylay.services.rules.models.transformer_execution_result import TransformerExecutionResult
try:
    # Execute Latest Transformer Version
    # calls `POST /rules/v1/transformers/{name}`
    api_response = await waylay_client.rules.plugs_execution.execute_transformer(
        'name_example', # name | path param "name"
    )
    print("The response of rules.plugs_execution.execute_transformer:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_transformer: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/transformers/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TransformerExecutionResult`** |  | [TransformerExecutionResult](TransformerExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Transformer Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_transformer_version**
> execute_transformer_version(
> name: str,
> version: str,
> headers
> ) -> TransformerExecutionResult

Execute Specified Transformer Version

Execute specified version of a transformer.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-rules-types` is installed
from waylay.services.rules.models.execute_plugs_specification import ExecutePlugsSpecification
from waylay.services.rules.models.transformer_execution_result import TransformerExecutionResult
try:
    # Execute Specified Transformer Version
    # calls `POST /rules/v1/transformers/{name}/versions/{version}`
    api_response = await waylay_client.rules.plugs_execution.execute_transformer_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of rules.plugs_execution.execute_transformer_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling rules.plugs_execution.execute_transformer_version: %s\n" % e)
```

### Endpoint
```
POST /rules/v1/transformers/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` |  | 
**version** | **str** | path parameter `"version"` | Version number of plugin | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`TransformerExecutionResult`** |  | [TransformerExecutionResult](TransformerExecutionResult.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Executed |  -  |
**400** | Unsuccessfully Executed |  -  |
**404** | Transformer Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

