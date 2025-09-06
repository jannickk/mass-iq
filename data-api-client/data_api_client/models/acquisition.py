from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Acquisition")


@_attrs_define
class Acquisition:
    """
    Attributes:
        name (str):
        archive_id (UUID):
        owner_id (UUID):
        mzmlid (Union[None, Unset, str]):
        processed (Union[Unset, bool]):  Default: False.
        id (Union[Unset, UUID]):
    """

    name: str
    archive_id: UUID
    owner_id: UUID
    mzmlid: Union[None, Unset, str] = UNSET
    processed: Union[Unset, bool] = False
    id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        archive_id = str(self.archive_id)

        owner_id = str(self.owner_id)

        mzmlid: Union[None, Unset, str]
        if isinstance(self.mzmlid, Unset):
            mzmlid = UNSET
        else:
            mzmlid = self.mzmlid

        processed = self.processed

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "archive_id": archive_id,
                "owner_id": owner_id,
            }
        )
        if mzmlid is not UNSET:
            field_dict["mzmlid"] = mzmlid
        if processed is not UNSET:
            field_dict["processed"] = processed
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        archive_id = UUID(d.pop("archive_id"))

        owner_id = UUID(d.pop("owner_id"))

        def _parse_mzmlid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mzmlid = _parse_mzmlid(d.pop("mzmlid", UNSET))

        processed = d.pop("processed", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        acquisition = cls(
            name=name,
            archive_id=archive_id,
            owner_id=owner_id,
            mzmlid=mzmlid,
            processed=processed,
            id=id,
        )

        acquisition.additional_properties = d
        return acquisition

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
