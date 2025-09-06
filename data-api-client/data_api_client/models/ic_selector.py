from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ic_selector_filter import ICSelectorFilter
    from ..models.time_filter import TimeFilter


T = TypeVar("T", bound="ICSelector")


@_attrs_define
class ICSelector:
    """
    Attributes:
        name (str):
        filter_ (ICSelectorFilter):
        time_filter (Union['TimeFilter', None, Unset]):
    """

    name: str
    filter_: "ICSelectorFilter"
    time_filter: Union["TimeFilter", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.time_filter import TimeFilter

        name = self.name

        filter_ = self.filter_.to_dict()

        time_filter: Union[None, Unset, dict[str, Any]]
        if isinstance(self.time_filter, Unset):
            time_filter = UNSET
        elif isinstance(self.time_filter, TimeFilter):
            time_filter = self.time_filter.to_dict()
        else:
            time_filter = self.time_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filter": filter_,
            }
        )
        if time_filter is not UNSET:
            field_dict["timeFilter"] = time_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ic_selector_filter import ICSelectorFilter
        from ..models.time_filter import TimeFilter

        d = dict(src_dict)
        name = d.pop("name")

        filter_ = ICSelectorFilter.from_dict(d.pop("filter"))

        def _parse_time_filter(data: object) -> Union["TimeFilter", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_filter_type_0 = TimeFilter.from_dict(data)

                return time_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TimeFilter", None, Unset], data)

        time_filter = _parse_time_filter(d.pop("timeFilter", UNSET))

        ic_selector = cls(
            name=name,
            filter_=filter_,
            time_filter=time_filter,
        )

        ic_selector.additional_properties = d
        return ic_selector

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
