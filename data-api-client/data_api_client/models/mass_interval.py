from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MassInterval")


@_attrs_define
class MassInterval:
    """
    Attributes:
        start_mz (float):
        end_mz (float):
    """

    start_mz: float
    end_mz: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_mz = self.start_mz

        end_mz = self.end_mz

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startMz": start_mz,
                "endMz": end_mz,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_mz = d.pop("startMz")

        end_mz = d.pop("endMz")

        mass_interval = cls(
            start_mz=start_mz,
            end_mz=end_mz,
        )

        mass_interval.additional_properties = d
        return mass_interval

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
