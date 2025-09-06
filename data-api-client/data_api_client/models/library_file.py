import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryFile")


@_attrs_define
class LibraryFile:
    """
    Attributes:
        filename (str):
        user_defined_path (str):
        file_absolute_path (str):
        type_ (str):
        filename_extension (str):
        owner_id (UUID):
        added_by_id (UUID):
        create_time (datetime.datetime):
        acl (Union[None, Unset, str]):
        permission (Union[None, Unset, str]):
        processed (Union[Unset, bool]):  Default: False.
        submitted (Union[Unset, bool]):  Default: False.
        file_size (Union[None, Unset, int]):
        uploaded_at (Union[None, Unset, datetime.datetime]): Time of upload finished.
        upload_finished (Union[Unset, bool]):  Default: False.
        upd_by_id (Union[None, UUID, Unset]):
        update_time (Union[None, Unset, datetime.datetime]):
        id (Union[None, Unset, int]):
    """

    filename: str
    user_defined_path: str
    file_absolute_path: str
    type_: str
    filename_extension: str
    owner_id: UUID
    added_by_id: UUID
    create_time: datetime.datetime
    acl: Union[None, Unset, str] = UNSET
    permission: Union[None, Unset, str] = UNSET
    processed: Union[Unset, bool] = False
    submitted: Union[Unset, bool] = False
    file_size: Union[None, Unset, int] = UNSET
    uploaded_at: Union[None, Unset, datetime.datetime] = UNSET
    upload_finished: Union[Unset, bool] = False
    upd_by_id: Union[None, UUID, Unset] = UNSET
    update_time: Union[None, Unset, datetime.datetime] = UNSET
    id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        user_defined_path = self.user_defined_path

        file_absolute_path = self.file_absolute_path

        type_ = self.type_

        filename_extension = self.filename_extension

        owner_id = str(self.owner_id)

        added_by_id = str(self.added_by_id)

        create_time = self.create_time.isoformat()

        acl: Union[None, Unset, str]
        if isinstance(self.acl, Unset):
            acl = UNSET
        else:
            acl = self.acl

        permission: Union[None, Unset, str]
        if isinstance(self.permission, Unset):
            permission = UNSET
        else:
            permission = self.permission

        processed = self.processed

        submitted = self.submitted

        file_size: Union[None, Unset, int]
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        uploaded_at: Union[None, Unset, str]
        if isinstance(self.uploaded_at, Unset):
            uploaded_at = UNSET
        elif isinstance(self.uploaded_at, datetime.datetime):
            uploaded_at = self.uploaded_at.isoformat()
        else:
            uploaded_at = self.uploaded_at

        upload_finished = self.upload_finished

        upd_by_id: Union[None, Unset, str]
        if isinstance(self.upd_by_id, Unset):
            upd_by_id = UNSET
        elif isinstance(self.upd_by_id, UUID):
            upd_by_id = str(self.upd_by_id)
        else:
            upd_by_id = self.upd_by_id

        update_time: Union[None, Unset, str]
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "user_defined_path": user_defined_path,
                "file_absolute_path": file_absolute_path,
                "type": type_,
                "filename_extension": filename_extension,
                "owner_id": owner_id,
                "added_by_id": added_by_id,
                "create_time": create_time,
            }
        )
        if acl is not UNSET:
            field_dict["acl"] = acl
        if permission is not UNSET:
            field_dict["permission"] = permission
        if processed is not UNSET:
            field_dict["processed"] = processed
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if uploaded_at is not UNSET:
            field_dict["uploaded_at"] = uploaded_at
        if upload_finished is not UNSET:
            field_dict["upload_finished"] = upload_finished
        if upd_by_id is not UNSET:
            field_dict["upd_by_id"] = upd_by_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        user_defined_path = d.pop("user_defined_path")

        file_absolute_path = d.pop("file_absolute_path")

        type_ = d.pop("type")

        filename_extension = d.pop("filename_extension")

        owner_id = UUID(d.pop("owner_id"))

        added_by_id = UUID(d.pop("added_by_id"))

        create_time = isoparse(d.pop("create_time"))

        def _parse_acl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acl = _parse_acl(d.pop("acl", UNSET))

        def _parse_permission(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        permission = _parse_permission(d.pop("permission", UNSET))

        processed = d.pop("processed", UNSET)

        submitted = d.pop("submitted", UNSET)

        def _parse_file_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        def _parse_uploaded_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uploaded_at_type_0 = isoparse(data)

                return uploaded_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        uploaded_at = _parse_uploaded_at(d.pop("uploaded_at", UNSET))

        upload_finished = d.pop("upload_finished", UNSET)

        def _parse_upd_by_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upd_by_id_type_0 = UUID(data)

                return upd_by_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        upd_by_id = _parse_upd_by_id(d.pop("upd_by_id", UNSET))

        def _parse_update_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = isoparse(data)

                return update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        library_file = cls(
            filename=filename,
            user_defined_path=user_defined_path,
            file_absolute_path=file_absolute_path,
            type_=type_,
            filename_extension=filename_extension,
            owner_id=owner_id,
            added_by_id=added_by_id,
            create_time=create_time,
            acl=acl,
            permission=permission,
            processed=processed,
            submitted=submitted,
            file_size=file_size,
            uploaded_at=uploaded_at,
            upload_finished=upload_finished,
            upd_by_id=upd_by_id,
            update_time=update_time,
            id=id,
        )

        library_file.additional_properties = d
        return library_file

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
