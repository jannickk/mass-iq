from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.isolation_window import IsolationWindow
    from ..models.mz_filter import MZFilter
    from ..models.mz_target import MzTarget


T = TypeVar("T", bound="ICSelectorFilter")


@_attrs_define
class ICSelectorFilter:
    """ """

    additional_properties: dict[str, Union["IsolationWindow", "MZFilter", "MzTarget"]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.isolation_window import IsolationWindow
        from ..models.mz_filter import MZFilter

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, IsolationWindow):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, MZFilter):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.isolation_window import IsolationWindow
        from ..models.mz_filter import MZFilter
        from ..models.mz_target import MzTarget

        d = dict(src_dict)
        ic_selector_filter = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Union["IsolationWindow", "MZFilter", "MzTarget"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = IsolationWindow.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = MZFilter.from_dict(data)

                    return additional_property_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_2 = MzTarget.from_dict(data)

                return additional_property_type_2

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        ic_selector_filter.additional_properties = additional_properties
        return ic_selector_filter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union["IsolationWindow", "MZFilter", "MzTarget"]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union["IsolationWindow", "MZFilter", "MzTarget"]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
