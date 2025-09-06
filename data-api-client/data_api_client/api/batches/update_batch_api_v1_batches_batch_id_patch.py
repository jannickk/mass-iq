from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sample_batch import SampleBatch
from ...models.sample_batch_update import SampleBatchUpdate
from ...types import Response


def _get_kwargs(
    batch_id: UUID,
    *,
    body: SampleBatchUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/batches/{batch_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SampleBatch]]:
    if response.status_code == 200:
        response_200 = SampleBatch.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, SampleBatch]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SampleBatchUpdate,
) -> Response[Union[HTTPValidationError, SampleBatch]]:
    """Update Batch

     Retrieve Batches

    Args:
        batch_id (UUID):
        body (SampleBatchUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SampleBatch]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SampleBatchUpdate,
) -> Optional[Union[HTTPValidationError, SampleBatch]]:
    """Update Batch

     Retrieve Batches

    Args:
        batch_id (UUID):
        body (SampleBatchUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SampleBatch]
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    batch_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SampleBatchUpdate,
) -> Response[Union[HTTPValidationError, SampleBatch]]:
    """Update Batch

     Retrieve Batches

    Args:
        batch_id (UUID):
        body (SampleBatchUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SampleBatch]]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SampleBatchUpdate,
) -> Optional[Union[HTTPValidationError, SampleBatch]]:
    """Update Batch

     Retrieve Batches

    Args:
        batch_id (UUID):
        body (SampleBatchUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SampleBatch]
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            body=body,
        )
    ).parsed
