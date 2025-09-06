from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TimeFilter")


@_attrs_define
class TimeFilter:
    """
    Attributes:
        start_millis (int):
        end_millis (int):
    """

    start_millis: int
    end_millis: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_millis = self.start_millis

        end_millis = self.end_millis

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_millis": start_millis,
                "end_millis": end_millis,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_millis = d.pop("start_millis")

        end_millis = d.pop("end_millis")

        time_filter = cls(
            start_millis=start_millis,
            end_millis=end_millis,
        )

        time_filter.additional_properties = d
        return time_filter

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
