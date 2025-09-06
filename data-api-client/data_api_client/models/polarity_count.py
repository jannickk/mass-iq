from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polarity_count_polarity import PolarityCountPolarity

T = TypeVar("T", bound="PolarityCount")


@_attrs_define
class PolarityCount:
    """
    Attributes:
        polarity (PolarityCountPolarity):
        count (int):
    """

    polarity: PolarityCountPolarity
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polarity = self.polarity.value

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polarity": polarity,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        polarity = PolarityCountPolarity(d.pop("polarity"))

        count = d.pop("count")

        polarity_count = cls(
            polarity=polarity,
            count=count,
        )

        polarity_count.additional_properties = d
        return polarity_count

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
