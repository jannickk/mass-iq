from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.isolation_window import IsolationWindow


T = TypeVar("T", bound="TransitionFilter")


@_attrs_define
class TransitionFilter:
    """
    Attributes:
        isolation_windows (list['IsolationWindow']): List of isolation windows, to be obtained from acquisition metadata
        fragment_min_mz (float):
        fragment_max_mz (float):
        allowed_fragment_types (list[str]):
        allowed_fragment_charges (list[int]):
        precursor_min_mz (float):
        precursor_max_mz (float):
        min_transitions (int):
        max_transitions (int):
    """

    isolation_windows: list["IsolationWindow"]
    fragment_min_mz: float
    fragment_max_mz: float
    allowed_fragment_types: list[str]
    allowed_fragment_charges: list[int]
    precursor_min_mz: float
    precursor_max_mz: float
    min_transitions: int
    max_transitions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isolation_windows = []
        for isolation_windows_item_data in self.isolation_windows:
            isolation_windows_item = isolation_windows_item_data.to_dict()
            isolation_windows.append(isolation_windows_item)

        fragment_min_mz = self.fragment_min_mz

        fragment_max_mz = self.fragment_max_mz

        allowed_fragment_types = self.allowed_fragment_types

        allowed_fragment_charges = self.allowed_fragment_charges

        precursor_min_mz = self.precursor_min_mz

        precursor_max_mz = self.precursor_max_mz

        min_transitions = self.min_transitions

        max_transitions = self.max_transitions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isolation_windows": isolation_windows,
                "fragment_min_mz": fragment_min_mz,
                "fragment_max_mz": fragment_max_mz,
                "allowed_fragment_types": allowed_fragment_types,
                "allowed_fragment_charges": allowed_fragment_charges,
                "precursor_min_mz": precursor_min_mz,
                "precursor_max_mz": precursor_max_mz,
                "min_transitions": min_transitions,
                "max_transitions": max_transitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.isolation_window import IsolationWindow

        d = dict(src_dict)
        isolation_windows = []
        _isolation_windows = d.pop("isolation_windows")
        for isolation_windows_item_data in _isolation_windows:
            isolation_windows_item = IsolationWindow.from_dict(isolation_windows_item_data)

            isolation_windows.append(isolation_windows_item)

        fragment_min_mz = d.pop("fragment_min_mz")

        fragment_max_mz = d.pop("fragment_max_mz")

        allowed_fragment_types = cast(list[str], d.pop("allowed_fragment_types"))

        allowed_fragment_charges = cast(list[int], d.pop("allowed_fragment_charges"))

        precursor_min_mz = d.pop("precursor_min_mz")

        precursor_max_mz = d.pop("precursor_max_mz")

        min_transitions = d.pop("min_transitions")

        max_transitions = d.pop("max_transitions")

        transition_filter = cls(
            isolation_windows=isolation_windows,
            fragment_min_mz=fragment_min_mz,
            fragment_max_mz=fragment_max_mz,
            allowed_fragment_types=allowed_fragment_types,
            allowed_fragment_charges=allowed_fragment_charges,
            precursor_min_mz=precursor_min_mz,
            precursor_max_mz=precursor_max_mz,
            min_transitions=min_transitions,
            max_transitions=max_transitions,
        )

        transition_filter.additional_properties = d
        return transition_filter

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
