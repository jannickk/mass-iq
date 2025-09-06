from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveUpdate")


@_attrs_define
class ArchiveUpdate:
    """
    Attributes:
        archive_absolute_path (str): Absolute path of the archive.
        archive_owner (str): Owner of the archive.
        owner_id (Union[None, str]):
        filename (str): Name of the file.
        filename_extension (str): File extension.
        type_ (str): Type of the file.
        batch_id (Union[None, str]):
        file_size (int): Size of the file in bytes.
        archive_upload_time (Union[None, Unset, int]): Time of upload in Unix timestamp format.
        archive_permission (Union[None, Unset, str]): Permissions of the archive.
        archive_acl (Union[None, Unset, str]): Access control list of the archive.
        processed (Union[Unset, bool]): Indicates if the file has been processed. Default: False.
        submitted (Union[Unset, bool]): Indicates if the file has been submitted to the pipeline Default: False.
        user_defined_path (Union[None, Unset, str]): User-defined path for the file.
        upload_finished (Union[Unset, bool]): Indicates if the upload is finished. Default: False.
    """

    archive_absolute_path: str
    archive_owner: str
    owner_id: Union[None, str]
    filename: str
    filename_extension: str
    type_: str
    batch_id: Union[None, str]
    file_size: int
    archive_upload_time: Union[None, Unset, int] = UNSET
    archive_permission: Union[None, Unset, str] = UNSET
    archive_acl: Union[None, Unset, str] = UNSET
    processed: Union[Unset, bool] = False
    submitted: Union[Unset, bool] = False
    user_defined_path: Union[None, Unset, str] = UNSET
    upload_finished: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_absolute_path = self.archive_absolute_path

        archive_owner = self.archive_owner

        owner_id: Union[None, str]
        owner_id = self.owner_id

        filename = self.filename

        filename_extension = self.filename_extension

        type_ = self.type_

        batch_id: Union[None, str]
        batch_id = self.batch_id

        file_size = self.file_size

        archive_upload_time: Union[None, Unset, int]
        if isinstance(self.archive_upload_time, Unset):
            archive_upload_time = UNSET
        else:
            archive_upload_time = self.archive_upload_time

        archive_permission: Union[None, Unset, str]
        if isinstance(self.archive_permission, Unset):
            archive_permission = UNSET
        else:
            archive_permission = self.archive_permission

        archive_acl: Union[None, Unset, str]
        if isinstance(self.archive_acl, Unset):
            archive_acl = UNSET
        else:
            archive_acl = self.archive_acl

        processed = self.processed

        submitted = self.submitted

        user_defined_path: Union[None, Unset, str]
        if isinstance(self.user_defined_path, Unset):
            user_defined_path = UNSET
        else:
            user_defined_path = self.user_defined_path

        upload_finished = self.upload_finished

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archive_absolute_path": archive_absolute_path,
                "archive_owner": archive_owner,
                "owner_id": owner_id,
                "filename": filename,
                "filename_extension": filename_extension,
                "type": type_,
                "batch_id": batch_id,
                "file_size": file_size,
            }
        )
        if archive_upload_time is not UNSET:
            field_dict["archive_upload_time"] = archive_upload_time
        if archive_permission is not UNSET:
            field_dict["archive_permission"] = archive_permission
        if archive_acl is not UNSET:
            field_dict["archive_acl"] = archive_acl
        if processed is not UNSET:
            field_dict["processed"] = processed
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if user_defined_path is not UNSET:
            field_dict["user_defined_path"] = user_defined_path
        if upload_finished is not UNSET:
            field_dict["upload_finished"] = upload_finished

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archive_absolute_path = d.pop("archive_absolute_path")

        archive_owner = d.pop("archive_owner")

        def _parse_owner_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        owner_id = _parse_owner_id(d.pop("owner_id"))

        filename = d.pop("filename")

        filename_extension = d.pop("filename_extension")

        type_ = d.pop("type")

        def _parse_batch_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        batch_id = _parse_batch_id(d.pop("batch_id"))

        file_size = d.pop("file_size")

        def _parse_archive_upload_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        archive_upload_time = _parse_archive_upload_time(d.pop("archive_upload_time", UNSET))

        def _parse_archive_permission(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archive_permission = _parse_archive_permission(d.pop("archive_permission", UNSET))

        def _parse_archive_acl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archive_acl = _parse_archive_acl(d.pop("archive_acl", UNSET))

        processed = d.pop("processed", UNSET)

        submitted = d.pop("submitted", UNSET)

        def _parse_user_defined_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_defined_path = _parse_user_defined_path(d.pop("user_defined_path", UNSET))

        upload_finished = d.pop("upload_finished", UNSET)

        archive_update = cls(
            archive_absolute_path=archive_absolute_path,
            archive_owner=archive_owner,
            owner_id=owner_id,
            filename=filename,
            filename_extension=filename_extension,
            type_=type_,
            batch_id=batch_id,
            file_size=file_size,
            archive_upload_time=archive_upload_time,
            archive_permission=archive_permission,
            archive_acl=archive_acl,
            processed=processed,
            submitted=submitted,
            user_defined_path=user_defined_path,
            upload_finished=upload_finished,
        )

        archive_update.additional_properties = d
        return archive_update

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
