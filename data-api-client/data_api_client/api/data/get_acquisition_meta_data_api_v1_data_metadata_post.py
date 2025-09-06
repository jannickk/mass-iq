from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acquisition_meta_data import AcquisitionMetaData
from ...models.data_reference import DataReference
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DataReference,
    q: Union[None, Unset, str] = "v2",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_q: Union[None, Unset, str]
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/data/metadata",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AcquisitionMetaData, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = AcquisitionMetaData.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AcquisitionMetaData, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataReference,
    q: Union[None, Unset, str] = "v2",
) -> Response[Union[AcquisitionMetaData, HTTPValidationError]]:
    """Get Acquisition Meta Data

    Args:
        q (Union[None, Unset, str]):  Default: 'v2'.
        body (DataReference):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcquisitionMetaData, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataReference,
    q: Union[None, Unset, str] = "v2",
) -> Optional[Union[AcquisitionMetaData, HTTPValidationError]]:
    """Get Acquisition Meta Data

    Args:
        q (Union[None, Unset, str]):  Default: 'v2'.
        body (DataReference):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcquisitionMetaData, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataReference,
    q: Union[None, Unset, str] = "v2",
) -> Response[Union[AcquisitionMetaData, HTTPValidationError]]:
    """Get Acquisition Meta Data

    Args:
        q (Union[None, Unset, str]):  Default: 'v2'.
        body (DataReference):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcquisitionMetaData, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DataReference,
    q: Union[None, Unset, str] = "v2",
) -> Optional[Union[AcquisitionMetaData, HTTPValidationError]]:
    """Get Acquisition Meta Data

    Args:
        q (Union[None, Unset, str]):  Default: 'v2'.
        body (DataReference):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcquisitionMetaData, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            q=q,
        )
    ).parsed
