from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_array import DataArray
    from ..models.ic_descriptor import ICDescriptor


T = TypeVar("T", bound="IC")


@_attrs_define
class IC:
    """
    Attributes:
        data_array (DataArray):
        name (str):
        ic_descriptor (Union['ICDescriptor', None, Unset]):
    """

    data_array: "DataArray"
    name: str
    ic_descriptor: Union["ICDescriptor", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ic_descriptor import ICDescriptor

        data_array = self.data_array.to_dict()

        name = self.name

        ic_descriptor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.ic_descriptor, Unset):
            ic_descriptor = UNSET
        elif isinstance(self.ic_descriptor, ICDescriptor):
            ic_descriptor = self.ic_descriptor.to_dict()
        else:
            ic_descriptor = self.ic_descriptor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dataArray": data_array,
                "name": name,
            }
        )
        if ic_descriptor is not UNSET:
            field_dict["ic_descriptor"] = ic_descriptor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_array import DataArray
        from ..models.ic_descriptor import ICDescriptor

        d = dict(src_dict)
        data_array = DataArray.from_dict(d.pop("dataArray"))

        name = d.pop("name")

        def _parse_ic_descriptor(data: object) -> Union["ICDescriptor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ic_descriptor_type_0 = ICDescriptor.from_dict(data)

                return ic_descriptor_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ICDescriptor", None, Unset], data)

        ic_descriptor = _parse_ic_descriptor(d.pop("ic_descriptor", UNSET))

        ic = cls(
            data_array=data_array,
            name=name,
            ic_descriptor=ic_descriptor,
        )

        ic.additional_properties = d
        return ic

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
