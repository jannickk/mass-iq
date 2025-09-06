from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.peptide_rank import PeptideRank
from ...types import UNSET, Response, Unset


def _get_kwargs(
    library_id: int,
    db_sequence_id: UUID,
    *,
    top_n: Union[None, Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_top_n: Union[None, Unset, int]
    if isinstance(top_n, Unset):
        json_top_n = UNSET
    else:
        json_top_n = top_n
    params["top_n"] = json_top_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/libraries/{library_id}/dbsequences/{db_sequence_id}/peptides/ranked-by-intensity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["PeptideRank"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PeptideRank.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, list["PeptideRank"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    library_id: int,
    db_sequence_id: UUID,
    *,
    client: AuthenticatedClient,
    top_n: Union[None, Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, list["PeptideRank"]]]:
    """Api Get Peptides Of Db Sequence

    Args:
        library_id (int):
        db_sequence_id (UUID):
        top_n (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['PeptideRank']]]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        db_sequence_id=db_sequence_id,
        top_n=top_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    library_id: int,
    db_sequence_id: UUID,
    *,
    client: AuthenticatedClient,
    top_n: Union[None, Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, list["PeptideRank"]]]:
    """Api Get Peptides Of Db Sequence

    Args:
        library_id (int):
        db_sequence_id (UUID):
        top_n (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['PeptideRank']]
    """

    return sync_detailed(
        library_id=library_id,
        db_sequence_id=db_sequence_id,
        client=client,
        top_n=top_n,
    ).parsed


async def asyncio_detailed(
    library_id: int,
    db_sequence_id: UUID,
    *,
    client: AuthenticatedClient,
    top_n: Union[None, Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, list["PeptideRank"]]]:
    """Api Get Peptides Of Db Sequence

    Args:
        library_id (int):
        db_sequence_id (UUID):
        top_n (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['PeptideRank']]]
    """

    kwargs = _get_kwargs(
        library_id=library_id,
        db_sequence_id=db_sequence_id,
        top_n=top_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    library_id: int,
    db_sequence_id: UUID,
    *,
    client: AuthenticatedClient,
    top_n: Union[None, Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, list["PeptideRank"]]]:
    """Api Get Peptides Of Db Sequence

    Args:
        library_id (int):
        db_sequence_id (UUID):
        top_n (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['PeptideRank']]
    """

    return (
        await asyncio_detailed(
            library_id=library_id,
            db_sequence_id=db_sequence_id,
            client=client,
            top_n=top_n,
        )
    ).parsed
