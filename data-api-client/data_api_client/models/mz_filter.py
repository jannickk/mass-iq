from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mass_interval import MassInterval


T = TypeVar("T", bound="MZFilter")


@_attrs_define
class MZFilter:
    """
    Attributes:
        value (MassInterval):
        type_ (Union[Unset, str]):  Default: 'mz-interval'.
    """

    value: "MassInterval"
    type_: Union[Unset, str] = "mz-interval"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mass_interval import MassInterval

        d = dict(src_dict)
        value = MassInterval.from_dict(d.pop("value"))

        type_ = d.pop("type", UNSET)

        mz_filter = cls(
            value=value,
            type_=type_,
        )

        mz_filter.additional_properties = d
        return mz_filter

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
