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
        ATasksBatchOperationSpecification,
        BatchOperationEnqueued,
        ErrorResponse,
        GetBatchOperation200Response,
    )
    from waylay.services.rules.queries.tasks_batch_operations_api import (
        GetQuery,
        StartQuery,
    )


try:
    from waylay.services.rules.models import (
        ATasksBatchOperationSpecification,
        BatchOperationEnqueued,
        ErrorResponse,
        GetBatchOperation200Response,
    )
    from waylay.services.rules.queries.tasks_batch_operations_api import (
        GetQuery,
        StartQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        GetQuery = dict
        GetBatchOperation200Response = Model

        ErrorResponse = Model

        ATasksBatchOperationSpecification = Model

        StartQuery = dict
        BatchOperationEnqueued = Model

        ErrorResponse = Model


T = TypeVar("T")


class TasksBatchOperationsApi(WithApiClient):
    """TasksBatchOperationsApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> GetBatchOperation200Response: ...

    @overload
    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get(
        self,
        batch_id: Annotated[
            StrictStr, Field(description="Unique Batch Operation identifier")
        ],
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> GetBatchOperation200Response | T | Response | Model:
        """Get Tasks Batch Operation Status.

        Get the results of the Tasks Batch Operation.
        :param batch_id: Unique Batch Operation identifier (required)
        :type batch_id: str
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
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

        # path parameters
        path_params: Dict[str, str] = {
            "batchId": str(batch_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": GetBatchOperation200Response if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/rules/v1/batch/{batchId}",
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
    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> BatchOperationEnqueued: ...

    @overload
    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def start(
        self,
        *,
        json: Annotated[
            ATasksBatchOperationSpecification,
            Field(description="Tasks Batch Operation"),
        ],
        query: StartQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> BatchOperationEnqueued | T | Response | Model:
        """Start Batch Operations.

        Start a batch operation.
        :param json: Tasks Batch Operation
        :type json: ATasksBatchOperationSpecification, optional
        :param query: URL Query parameters.
        :type query: StartQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
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

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and validate_request:
            body_adapter = TypeAdapter(
                Annotated[
                    ATasksBatchOperationSpecification,
                    Field(description="Tasks Batch Operation"),
                ]
            )
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(StartQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "202": BatchOperationEnqueued if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/rules/v1/batch",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
