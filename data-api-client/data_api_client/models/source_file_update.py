from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceFileUpdate")


@_attrs_define
class SourceFileUpdate:
    """
    Attributes:
        owner_id (Union[None, UUID, Unset]):
        filebundle_id (Union[None, UUID, Unset]):
        upload_finished (Union[None, Unset, bool]):
        file_size (Union[None, Unset, int]):
    """

    owner_id: Union[None, UUID, Unset] = UNSET
    filebundle_id: Union[None, UUID, Unset] = UNSET
    upload_finished: Union[None, Unset, bool] = UNSET
    file_size: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id: Union[None, Unset, str]
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, UUID):
            owner_id = str(self.owner_id)
        else:
            owner_id = self.owner_id

        filebundle_id: Union[None, Unset, str]
        if isinstance(self.filebundle_id, Unset):
            filebundle_id = UNSET
        elif isinstance(self.filebundle_id, UUID):
            filebundle_id = str(self.filebundle_id)
        else:
            filebundle_id = self.filebundle_id

        upload_finished: Union[None, Unset, bool]
        if isinstance(self.upload_finished, Unset):
            upload_finished = UNSET
        else:
            upload_finished = self.upload_finished

        file_size: Union[None, Unset, int]
        if isinstance(self.file_size, Unset):
            file_size = UNSET
        else:
            file_size = self.file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if filebundle_id is not UNSET:
            field_dict["filebundle_id"] = filebundle_id
        if upload_finished is not UNSET:
            field_dict["upload_finished"] = upload_finished
        if file_size is not UNSET:
            field_dict["file_size"] = file_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_owner_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_id_type_0 = UUID(data)

                return owner_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

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

        def _parse_upload_finished(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        upload_finished = _parse_upload_finished(d.pop("upload_finished", UNSET))

        def _parse_file_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        file_size = _parse_file_size(d.pop("file_size", UNSET))

        source_file_update = cls(
            owner_id=owner_id,
            filebundle_id=filebundle_id,
            upload_finished=upload_finished,
            file_size=file_size,
        )

        source_file_update.additional_properties = d
        return source_file_update

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
