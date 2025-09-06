from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    library_id: int,
    peptide_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/libraries/{library_id}/peptides/{peptide_id}/transitions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    library_id: int,
    peptide_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError]:
    """Api Get Transitions Of Peptides

    Args:
        library_id (int):
        peptide_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        peptide_id=peptide_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: int,
    peptide_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[HTTPValidationError]:
    """Api Get Transitions Of Peptides

    Args:
        library_id (int):
        peptide_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        library_id=library_id,
        peptide_id=peptide_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    library_id: int,
    peptide_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError]:
    """Api Get Transitions Of Peptides

    Args:
        library_id (int):
        peptide_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        peptide_id=peptide_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: int,
    peptide_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[HTTPValidationError]:
    """Api Get Transitions Of Peptides

    Args:
        library_id (int):
        peptide_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            peptide_id=peptide_id,
            client=client,
        )
    ).parsed
