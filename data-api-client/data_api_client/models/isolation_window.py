from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IsolationWindow")


@_attrs_define
class IsolationWindow:
    """
    Attributes:
        isolation_window_lower_end (float):
        isolation_window_upper_end (float):
        isolation_window_target (float):
        experiment (int):
        lower_offset (Union[None, Unset, float]):
        upper_offset (Union[None, Unset, float]):
        width (Union[None, Unset, float]):
    """

    isolation_window_lower_end: float
    isolation_window_upper_end: float
    isolation_window_target: float
    experiment: int
    lower_offset: Union[None, Unset, float] = UNSET
    upper_offset: Union[None, Unset, float] = UNSET
    width: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isolation_window_lower_end = self.isolation_window_lower_end

        isolation_window_upper_end = self.isolation_window_upper_end

        isolation_window_target = self.isolation_window_target

        experiment = self.experiment

        lower_offset: Union[None, Unset, float]
        if isinstance(self.lower_offset, Unset):
            lower_offset = UNSET
        else:
            lower_offset = self.lower_offset

        upper_offset: Union[None, Unset, float]
        if isinstance(self.upper_offset, Unset):
            upper_offset = UNSET
        else:
            upper_offset = self.upper_offset

        width: Union[None, Unset, float]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isolationWindowLowerEnd": isolation_window_lower_end,
                "isolationWindowUpperEnd": isolation_window_upper_end,
                "isolationWindowTarget": isolation_window_target,
                "experiment": experiment,
            }
        )
        if lower_offset is not UNSET:
            field_dict["lowerOffset"] = lower_offset
        if upper_offset is not UNSET:
            field_dict["upperOffset"] = upper_offset
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        isolation_window_lower_end = d.pop("isolationWindowLowerEnd")

        isolation_window_upper_end = d.pop("isolationWindowUpperEnd")

        isolation_window_target = d.pop("isolationWindowTarget")

        experiment = d.pop("experiment")

        def _parse_lower_offset(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lower_offset = _parse_lower_offset(d.pop("lowerOffset", UNSET))

        def _parse_upper_offset(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        upper_offset = _parse_upper_offset(d.pop("upperOffset", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        width = _parse_width(d.pop("width", UNSET))

        isolation_window = cls(
            isolation_window_lower_end=isolation_window_lower_end,
            isolation_window_upper_end=isolation_window_upper_end,
            isolation_window_target=isolation_window_target,
            experiment=experiment,
            lower_offset=lower_offset,
            upper_offset=upper_offset,
            width=width,
        )

        isolation_window.additional_properties = d
        return isolation_window

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
