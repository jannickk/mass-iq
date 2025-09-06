from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleBatchCreate")


@_attrs_define
class SampleBatchCreate:
    """
    Attributes:
        name (str):
        owner (str):
        owner_id (UUID):
        description (Union[None, Unset, str]):
        frozen (Union[None, Unset, bool]):  Default: False.
        update_time (Union[None, Unset, str]):
        added_by_id (Union[None, Unset, str]):
        updated_by_id (Union[None, Unset, str]):
    """

    name: str
    owner: str
    owner_id: UUID
    description: Union[None, Unset, str] = UNSET
    frozen: Union[None, Unset, bool] = False
    update_time: Union[None, Unset, str] = UNSET
    added_by_id: Union[None, Unset, str] = UNSET
    updated_by_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner = self.owner

        owner_id = str(self.owner_id)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        frozen: Union[None, Unset, bool]
        if isinstance(self.frozen, Unset):
            frozen = UNSET
        else:
            frozen = self.frozen

        update_time: Union[None, Unset, str]
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        else:
            update_time = self.update_time

        added_by_id: Union[None, Unset, str]
        if isinstance(self.added_by_id, Unset):
            added_by_id = UNSET
        else:
            added_by_id = self.added_by_id

        updated_by_id: Union[None, Unset, str]
        if isinstance(self.updated_by_id, Unset):
            updated_by_id = UNSET
        else:
            updated_by_id = self.updated_by_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "owner": owner,
                "owner_id": owner_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if frozen is not UNSET:
            field_dict["frozen"] = frozen
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if updated_by_id is not UNSET:
            field_dict["updated_by_id"] = updated_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        owner = d.pop("owner")

        owner_id = UUID(d.pop("owner_id"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_frozen(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        frozen = _parse_frozen(d.pop("frozen", UNSET))

        def _parse_update_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_added_by_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        added_by_id = _parse_added_by_id(d.pop("added_by_id", UNSET))

        def _parse_updated_by_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_id = _parse_updated_by_id(d.pop("updated_by_id", UNSET))

        sample_batch_create = cls(
            name=name,
            owner=owner,
            owner_id=owner_id,
            description=description,
            frozen=frozen,
            update_time=update_time,
            added_by_id=added_by_id,
            updated_by_id=updated_by_id,
        )

        sample_batch_create.additional_properties = d
        return sample_batch_create

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
