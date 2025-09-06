from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ms_level_count_mslevel import MsLevelCountMslevel

T = TypeVar("T", bound="MsLevelCount")


@_attrs_define
class MsLevelCount:
    """
    Attributes:
        mslevel (MsLevelCountMslevel):
        count (int):
    """

    mslevel: MsLevelCountMslevel
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mslevel = self.mslevel.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mslevel": mslevel,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mslevel = MsLevelCountMslevel(d.pop("mslevel"))

        count = d.pop("count")

        ms_level_count = cls(
            mslevel=mslevel,
            count=count,
        )

        ms_level_count.additional_properties = d
        return ms_level_count

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
