from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acquisition import Acquisition
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    acquisition_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/acquisitions/{acquisition_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Acquisition, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Acquisition.from_dict(response.json())

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
) -> Response[Union[Acquisition, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    acquisition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Acquisition, HTTPValidationError]]:
    """Get Acquisition By Id

     Create new batch

    Args:
        acquisition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acquisition, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        acquisition_id=acquisition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    acquisition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Acquisition, HTTPValidationError]]:
    """Get Acquisition By Id

     Create new batch

    Args:
        acquisition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acquisition, HTTPValidationError]
    """

    return sync_detailed(
        acquisition_id=acquisition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    acquisition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Acquisition, HTTPValidationError]]:
    """Get Acquisition By Id

     Create new batch

    Args:
        acquisition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acquisition, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        acquisition_id=acquisition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    acquisition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Acquisition, HTTPValidationError]]:
    """Get Acquisition By Id

     Create new batch

    Args:
        acquisition_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acquisition, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            acquisition_id=acquisition_id,
            client=client,
        )
    ).parsed
