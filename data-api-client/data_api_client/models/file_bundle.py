from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileBundle")


@_attrs_define
class FileBundle:
    """
    Attributes:
        filename (str):
        owner (str):
        owner_id (UUID):
        user_defined_path (str):
        type_ (Union[None, Unset, str]):
        processed (Union[Unset, bool]):  Default: False.
        submitted (Union[Unset, bool]):  Default: False.
        upload_finished (Union[Unset, bool]):  Default: False.
        filebundle_id (Union[Unset, UUID]):
    """

    filename: str
    owner: str
    owner_id: UUID
    user_defined_path: str
    type_: Union[None, Unset, str] = UNSET
    processed: Union[Unset, bool] = False
    submitted: Union[Unset, bool] = False
    upload_finished: Union[Unset, bool] = False
    filebundle_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filename = self.filename

        owner = self.owner

        owner_id = str(self.owner_id)

        user_defined_path = self.user_defined_path

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        processed = self.processed

        submitted = self.submitted

        upload_finished = self.upload_finished

        filebundle_id: Union[Unset, str] = UNSET
        if not isinstance(self.filebundle_id, Unset):
            filebundle_id = str(self.filebundle_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filename": filename,
                "owner": owner,
                "owner_id": owner_id,
                "user_defined_path": user_defined_path,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if processed is not UNSET:
            field_dict["processed"] = processed
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if upload_finished is not UNSET:
            field_dict["upload_finished"] = upload_finished
        if filebundle_id is not UNSET:
            field_dict["filebundle_id"] = filebundle_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filename = d.pop("filename")

        owner = d.pop("owner")

        owner_id = UUID(d.pop("owner_id"))

        user_defined_path = d.pop("user_defined_path")

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        processed = d.pop("processed", UNSET)

        submitted = d.pop("submitted", UNSET)

        upload_finished = d.pop("upload_finished", UNSET)

        _filebundle_id = d.pop("filebundle_id", UNSET)
        filebundle_id: Union[Unset, UUID]
        if isinstance(_filebundle_id, Unset):
            filebundle_id = UNSET
        else:
            filebundle_id = UUID(_filebundle_id)

        file_bundle = cls(
            filename=filename,
            owner=owner,
            owner_id=owner_id,
            user_defined_path=user_defined_path,
            type_=type_,
            processed=processed,
            submitted=submitted,
            upload_finished=upload_finished,
            filebundle_id=filebundle_id,
        )

        file_bundle.additional_properties = d
        return file_bundle

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
