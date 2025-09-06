from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Transition")


@_attrs_define
class Transition:
    """
    Attributes:
        transition_name (str):
        q1 (float):
        q3 (float):
        transition_number (int):
    """

    transition_name: str
    q1: float
    q3: float
    transition_number: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transition_name = self.transition_name

        q1 = self.q1

        q3 = self.q3

        transition_number = self.transition_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transitionName": transition_name,
                "Q1": q1,
                "Q3": q3,
                "transitionNumber": transition_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transition_name = d.pop("transitionName")

        q1 = d.pop("Q1")

        q3 = d.pop("Q3")

        transition_number = d.pop("transitionNumber")

        transition = cls(
            transition_name=transition_name,
            q1=q1,
            q3=q3,
            transition_number=transition_number,
        )

        transition.additional_properties = d
        return transition

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
