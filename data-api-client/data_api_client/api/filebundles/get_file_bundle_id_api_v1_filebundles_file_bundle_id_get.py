from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_bundle import FileBundle
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    file_bundle_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/filebundles/{file_bundle_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[FileBundle, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = FileBundle.from_dict(response.json())

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
) -> Response[Union[FileBundle, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_bundle_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[FileBundle, HTTPValidationError]]:
    """Get File Bundle Id

     Create new batch

    Args:
        file_bundle_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileBundle, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_bundle_id=file_bundle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_bundle_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[FileBundle, HTTPValidationError]]:
    """Get File Bundle Id

     Create new batch

    Args:
        file_bundle_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileBundle, HTTPValidationError]
    """

    return sync_detailed(
        file_bundle_id=file_bundle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_bundle_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[FileBundle, HTTPValidationError]]:
    """Get File Bundle Id

     Create new batch

    Args:
        file_bundle_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FileBundle, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        file_bundle_id=file_bundle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_bundle_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[FileBundle, HTTPValidationError]]:
    """Get File Bundle Id

     Create new batch

    Args:
        file_bundle_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FileBundle, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            file_bundle_id=file_bundle_id,
            client=client,
        )
    ).parsed
