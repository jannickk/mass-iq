from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="BodyChunkedUploadAsyncApiV1UploadFilesChunkedSourcefilesPost")


@_attrs_define
class BodyChunkedUploadAsyncApiV1UploadFilesChunkedSourcefilesPost:
    """
    Attributes:
        file (File):
        file_name (str):
        upload_id (str):
        chunk_index (int):
        total_chunks (int):
    """

    file: File
    file_name: str
    upload_id: str
    chunk_index: int
    total_chunks: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        file_name = self.file_name

        upload_id = self.upload_id

        chunk_index = self.chunk_index

        total_chunks = self.total_chunks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "file_name": file_name,
                "upload_id": upload_id,
                "chunk_index": chunk_index,
                "total_chunks": total_chunks,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        files.append(("file_name", (None, str(self.file_name).encode(), "text/plain")))

        files.append(("upload_id", (None, str(self.upload_id).encode(), "text/plain")))

        files.append(("chunk_index", (None, str(self.chunk_index).encode(), "text/plain")))

        files.append(("total_chunks", (None, str(self.total_chunks).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        file_name = d.pop("file_name")

        upload_id = d.pop("upload_id")

        chunk_index = d.pop("chunk_index")

        total_chunks = d.pop("total_chunks")

        body_chunked_upload_async_api_v1_upload_files_chunked_sourcefiles_post = cls(
            file=file,
            file_name=file_name,
            upload_id=upload_id,
            chunk_index=chunk_index,
            total_chunks=total_chunks,
        )

        body_chunked_upload_async_api_v1_upload_files_chunked_sourcefiles_post.additional_properties = d
        return body_chunked_upload_async_api_v1_upload_files_chunked_sourcefiles_post

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
