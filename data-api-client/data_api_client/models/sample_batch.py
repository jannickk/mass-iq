import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SampleBatch")


@_attrs_define
class SampleBatch:
    """
    Attributes:
        name (str):
        owner (str):
        owner_id (UUID):
        description (Union[None, Unset, str]):
        frozen (Union[Unset, bool]):  Default: False.
        update_time (Union[None, Unset, str]):
        added_by_id (Union[None, Unset, str]):
        updated_by_id (Union[None, Unset, str]):
        id (Union[Unset, UUID]):
        create_time (Union[Unset, datetime.datetime]):
    """

    name: str
    owner: str
    owner_id: UUID
    description: Union[None, Unset, str] = UNSET
    frozen: Union[Unset, bool] = False
    update_time: Union[None, Unset, str] = UNSET
    added_by_id: Union[None, Unset, str] = UNSET
    updated_by_id: Union[None, Unset, str] = UNSET
    id: Union[Unset, UUID] = UNSET
    create_time: Union[Unset, datetime.datetime] = UNSET
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

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        create_time: Union[Unset, str] = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

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
        if id is not UNSET:
            field_dict["id"] = id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

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

        frozen = d.pop("frozen", UNSET)

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

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _create_time = d.pop("create_time", UNSET)
        create_time: Union[Unset, datetime.datetime]
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = isoparse(_create_time)

        sample_batch = cls(
            name=name,
            owner=owner,
            owner_id=owner_id,
            description=description,
            frozen=frozen,
            update_time=update_time,
            added_by_id=added_by_id,
            updated_by_id=updated_by_id,
            id=id,
            create_time=create_time,
        )

        sample_batch.additional_properties = d
        return sample_batch

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
