from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_reference import DataReference
    from ..models.ic_selector import ICSelector


T = TypeVar("T", bound="ICRequestSingleAcquisition")


@_attrs_define
class ICRequestSingleAcquisition:
    """
    Attributes:
        ic_selectors (list['ICSelector']):
        data_reference (DataReference):
        schema_version (Union[None, Unset, str]):  Default: 'v2'.
    """

    ic_selectors: list["ICSelector"]
    data_reference: "DataReference"
    schema_version: Union[None, Unset, str] = "v2"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ic_selectors = []
        for ic_selectors_item_data in self.ic_selectors:
            ic_selectors_item = ic_selectors_item_data.to_dict()
            ic_selectors.append(ic_selectors_item)

        data_reference = self.data_reference.to_dict()

        schema_version: Union[None, Unset, str]
        if isinstance(self.schema_version, Unset):
            schema_version = UNSET
        else:
            schema_version = self.schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ic_selectors": ic_selectors,
                "data_reference": data_reference,
            }
        )
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_reference import DataReference
        from ..models.ic_selector import ICSelector

        d = dict(src_dict)
        ic_selectors = []
        _ic_selectors = d.pop("ic_selectors")
        for ic_selectors_item_data in _ic_selectors:
            ic_selectors_item = ICSelector.from_dict(ic_selectors_item_data)

            ic_selectors.append(ic_selectors_item)

        data_reference = DataReference.from_dict(d.pop("data_reference"))

        def _parse_schema_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schema_version = _parse_schema_version(d.pop("schema_version", UNSET))

        ic_request_single_acquisition = cls(
            ic_selectors=ic_selectors,
            data_reference=data_reference,
            schema_version=schema_version,
        )

        ic_request_single_acquisition.additional_properties = d
        return ic_request_single_acquisition

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
