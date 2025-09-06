from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceFileCreate")


@_attrs_define
class SourceFileCreate:
    """
    Attributes:
        file_absolute_path (str): Absolute path of the archive.
        owner (str): Owner of the archive.
        owner_id (UUID): Unique identifier for the owner.
        filename (str): Name of the file.
        user_defined_path (str): User-defined path for the file.
        filename_extension (str): File extension.
        type_ (str): Type of the file.
        file_upload_time (Union[None, Unset, int]): Time of upload in Unix timestamp format.
        file_permission (Union[None, Unset, str]): Permissions of the archive.
        file_acl (Union[None, Unset, str]): Access control list of the archive.
        file_size (Union[None, Unset, int]): Size of the file
        filebundle_id (Union[None, UUID, Unset]): Size of the file in bytes.
        upload_finished (Union[Unset, bool]): Indicates if the upload is finished. Default: False.
    """

    file_absolute_path: str
    owner: str
    owner_id: UUID
    filename: str
    user_defined_path: str
    filename_extension: str
    type_: str
    file_upload_time: Union[None, Unset, int] = UNSET
    file_permission: Union[None, Unset, str] = UNSET
    file_acl: Union[None, Unset, str] = UNSET
    file_size: Union[None, Unset, int] = UNSET
    filebundle_id: Union[None, UUID, Unset] = UNSET
    upload_finished: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_absolute_path = self.file_absolute_path

        owner = self.owner

        owner_id = str(self.owner_id)

        filename = self.filename

        user_defined_path = self.user_defined_path

        filename_extension = self.filename_extension

        type_ = self.type_

        file_upload_time: Union[None, Unset, int]
        if isinstance(self.file_upload_time, Unset):
            file_upload_time = UNSET
        else:
            file_upload_time = self.file_upload_time

        file_permission: Union[None, Unset, str]
        if isinstance(self.file_permission, Unset):
            file_permission = UNSET
        else:
            file_permission = self.file_permission

        file_acl: Union[None, Unset, str]
        if isinstance(self.file_acl, Unset):
            file_acl = UNSET
        else:
            file_acl = self.file_acl

        file_size: Union[None, Unset, int]
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        filebundle_id: Union[None, Unset, str]
        if isinstance(self.filebundle_id, Unset):
            filebundle_id = UNSET
        elif isinstance(self.filebundle_id, UUID):
            filebundle_id = str(self.filebundle_id)
        else:
            filebundle_id = self.filebundle_id

        upload_finished = self.upload_finished

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_absolute_path": file_absolute_path,
                "owner": owner,
                "owner_id": owner_id,
                "filename": filename,
                "user_defined_path": user_defined_path,
                "filename_extension": filename_extension,
                "type": type_,
            }
        )
        if file_upload_time is not UNSET:
            field_dict["file_upload_time"] = file_upload_time
        if file_permission is not UNSET:
            field_dict["file_permission"] = file_permission
        if file_acl is not UNSET:
            field_dict["file_acl"] = file_acl
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if filebundle_id is not UNSET:
            field_dict["filebundle_id"] = filebundle_id
        if upload_finished is not UNSET:
            field_dict["upload_finished"] = upload_finished

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_absolute_path = d.pop("file_absolute_path")

        owner = d.pop("owner")

        owner_id = UUID(d.pop("owner_id"))

        filename = d.pop("filename")

        user_defined_path = d.pop("user_defined_path")

        filename_extension = d.pop("filename_extension")

        type_ = d.pop("type")

        def _parse_file_upload_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        file_upload_time = _parse_file_upload_time(d.pop("file_upload_time", UNSET))

        def _parse_file_permission(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_permission = _parse_file_permission(d.pop("file_permission", UNSET))

        def _parse_file_acl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_acl = _parse_file_acl(d.pop("file_acl", UNSET))

        def _parse_file_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_filebundle_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filebundle_id_type_0 = UUID(data)

                return filebundle_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        filebundle_id = _parse_filebundle_id(d.pop("filebundle_id", UNSET))

        upload_finished = d.pop("upload_finished", UNSET)

        source_file_create = cls(
            file_absolute_path=file_absolute_path,
            owner=owner,
            owner_id=owner_id,
            filename=filename,
            user_defined_path=user_defined_path,
            filename_extension=filename_extension,
            type_=type_,
            file_upload_time=file_upload_time,
            file_permission=file_permission,
            file_acl=file_acl,
            file_size=file_size,
            filebundle_id=filebundle_id,
            upload_finished=upload_finished,
        )

        source_file_create.additional_properties = d
        return source_file_create

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
