from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.isolation_window import IsolationWindow


T = TypeVar("T", bound="IsolationWindowCount")


@_attrs_define
class IsolationWindowCount:
    """
    Attributes:
        count (int):
        window (IsolationWindow):
    """

    count: int
    window: "IsolationWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.isolation_window import IsolationWindow

        d = dict(src_dict)
        count = d.pop("count")

        window = IsolationWindow.from_dict(d.pop("window"))

        isolation_window_count = cls(
            count=count,
            window=window,
        )

        isolation_window_count.additional_properties = d
        return isolation_window_count

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
