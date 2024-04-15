# coding: utf-8
"""Waylay rules engine api.

This code was generated from the OpenAPI documentation of 'Waylay rules engine'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Literal,
    TypeVar,
    overload,
)

from pydantic import (
    Field,
    StrictBool,
    StrictStr,
    TypeAdapter,
)
from typing_extensions import (
    Annotated,  # >=3.9,
)
from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.rules.models import (
        ActuatorExecutionResult,
        ErrorResponse,
        ExecutePlugsSpecification,
        SensorExecutionResult,
        TransformerExecutionResult,
    )
    from waylay.services.rules.queries.plugs_execution_api import (
        ExecuteActuatorQuery,
        ExecuteActuatorVersionQuery,
        ExecuteSensorQuery,
        ExecuteSensorVersionQuery,
        ExecuteTransformerQuery,
        ExecuteTransformerVersionQuery,
    )


try:
    from waylay.services.rules.models import (
        ActuatorExecutionResult,
        ErrorResponse,
        ExecutePlugsSpecification,
        SensorExecutionResult,
        TransformerExecutionResult,
    )
    from waylay.services.rules.queries.plugs_execution_api import (
        ExecuteActuatorQuery,
        ExecuteActuatorVersionQuery,
        ExecuteSensorQuery,
        ExecuteSensorVersionQuery,
        ExecuteTransformerQuery,
        ExecuteTransformerVersionQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        ExecutePlugsSpecification = Model

        ExecuteActuatorQuery = dict
        ActuatorExecutionResult = Model

        ActuatorExecutionResult = Model

        ErrorResponse = Model

        ExecutePlugsSpecification = Model

        ExecuteActuatorVersionQuery = dict
        ActuatorExecutionResult = Model

        ActuatorExecutionResult = Model

        ErrorResponse = Model

        ExecutePlugsSpecification = Model

        ExecuteSensorQuery = dict
        SensorExecutionResult = Model

        SensorExecutionResult = Model

        ErrorResponse = Model

        ExecutePlugsSpecification = Model

        ExecuteSensorVersionQuery = dict
        SensorExecutionResult = Model

        SensorExecutionResult = Model

        ErrorResponse = Model

        ExecutePlugsSpecification = Model

        ExecuteTransformerQuery = dict
        TransformerExecutionResult = Model

        TransformerExecutionResult = Model

        ErrorResponse = Model

        ExecutePlugsSpecification = Model

        ExecuteTransformerVersionQuery = dict
        TransformerExecutionResult = Model

        TransformerExecutionResult = Model

        ErrorResponse = Model


T = TypeVar("T")


class PlugsExecutionApi(WithApiClient):
    """PlugsExecutionApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ActuatorExecutionResult: ...

    @overload
    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_actuator(
        self,
        name: StrictStr,
        *,
        query: ExecuteActuatorQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ActuatorExecutionResult | T | Response | Model:
        """Execute Latest Actuator Version.

        Execute latest version of an actuator.
        :param name: (required)
        :type name: str
        :param query: URL Query parameters.
        :type query: ExecuteActuatorQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteActuatorQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": ActuatorExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ActuatorExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/actions/{name}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ActuatorExecutionResult: ...

    @overload
    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_actuator_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteActuatorVersionQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> ActuatorExecutionResult | T | Response | Model:
        """Execute Specified Actuator Version.

        Execute specified version of an actuator.
        :param name: (required)
        :type name: str
        :param version: Version number of plugin (required)
        :type version: str
        :param query: URL Query parameters.
        :type query: ExecuteActuatorVersionQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
            "version": str(version),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteActuatorVersionQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": ActuatorExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ActuatorExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/actions/{name}/versions/{version}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> SensorExecutionResult: ...

    @overload
    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_sensor(
        self,
        name: StrictStr,
        *,
        query: ExecuteSensorQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> SensorExecutionResult | T | Response | Model:
        """Execute Latest Sensor Version.

        Execute latest version of a sensor.
        :param name: (required)
        :type name: str
        :param query: URL Query parameters.
        :type query: ExecuteSensorQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteSensorQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": SensorExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": SensorExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/sensors/{name}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> SensorExecutionResult: ...

    @overload
    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_sensor_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteSensorVersionQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> SensorExecutionResult | T | Response | Model:
        """Execute Specified Sensor Version.

        Execute the specified version of a sensor.
        :param name: (required)
        :type name: str
        :param version: Version number of plugin (required)
        :type version: str
        :param query: URL Query parameters.
        :type query: ExecuteSensorVersionQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
            "version": str(version),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteSensorVersionQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": SensorExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": SensorExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/sensors/{name}/versions/{version}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TransformerExecutionResult: ...

    @overload
    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_transformer(
        self,
        name: StrictStr,
        *,
        query: ExecuteTransformerQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TransformerExecutionResult | T | Response | Model:
        """Execute Latest Transformer Version.

        Execute the latest transformer version.
        :param name: (required)
        :type name: str
        :param query: URL Query parameters.
        :type query: ExecuteTransformerQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteTransformerQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": TransformerExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": TransformerExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/transformers/{name}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TransformerExecutionResult: ...

    @overload
    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def execute_transformer_version(
        self,
        name: StrictStr,
        version: Annotated[
            str, Field(strict=True, description="Version number of plugin")
        ],
        *,
        query: ExecuteTransformerVersionQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TransformerExecutionResult | T | Response | Model:
        """Execute Specified Transformer Version.

        Execute specified version of a transformer.
        :param name: (required)
        :type name: str
        :param version: Version number of plugin (required)
        :type version: str
        :param query: URL Query parameters.
        :type query: ExecuteTransformerVersionQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "name": str(name),
            "version": str(version),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ExecuteTransformerVersionQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": TransformerExecutionResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": TransformerExecutionResult,
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/transformers/{name}/versions/{version}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )