from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_reference import DataReference
    from ..models.mz_target import MzTarget


T = TypeVar("T", bound="IsolationWindowRequest")


@_attrs_define
class IsolationWindowRequest:
    """
    Attributes:
        mz_target (MzTarget):
        data_reference (DataReference):
        schema_version (Union[None, Unset, str]):  Default: 'v2'.
    """

    mz_target: "MzTarget"
    data_reference: "DataReference"
    schema_version: Union[None, Unset, str] = "v2"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mz_target = self.mz_target.to_dict()

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
                "mz_target": mz_target,
                "data_reference": data_reference,
            }
        )
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_reference import DataReference
        from ..models.mz_target import MzTarget

        d = dict(src_dict)
        mz_target = MzTarget.from_dict(d.pop("mz_target"))

        data_reference = DataReference.from_dict(d.pop("data_reference"))

        def _parse_schema_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schema_version = _parse_schema_version(d.pop("schema_version", UNSET))

        isolation_window_request = cls(
            mz_target=mz_target,
            data_reference=data_reference,
            schema_version=schema_version,
        )

        isolation_window_request.additional_properties = d
        return isolation_window_request

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
