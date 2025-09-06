from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DBSequence")


@_attrs_define
class DBSequence:
    """
    Attributes:
        id (str): An unambiguous unique identifier within the scope of use.
        name (Union[None, str]): the name according to the XML document
        library_id (int): Reference to the library id which is an integer.
        searchdatabase_ref (str): Reference to the source database of this sequence.
        accession (str): The unique accession number of this sequence.
        seq (Union[None, Unset, str]): The actual sequence of amino acids or nucleic acids.
        description (Union[None, Unset, str]):
        db_id (Union[Unset, UUID]):
    """

    id: str
    name: Union[None, str]
    library_id: int
    searchdatabase_ref: str
    accession: str
    seq: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    db_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, str]
        name = self.name

        library_id = self.library_id

        searchdatabase_ref = self.searchdatabase_ref

        accession = self.accession

        seq: Union[None, Unset, str]
        if isinstance(self.seq, Unset):
            seq = UNSET
        else:
            seq = self.seq

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        db_id: Union[Unset, str] = UNSET
        if not isinstance(self.db_id, Unset):
            db_id = str(self.db_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "library_id": library_id,
                "searchdatabase_ref": searchdatabase_ref,
                "accession": accession,
            }
        )
        if seq is not UNSET:
            field_dict["seq"] = seq
        if description is not UNSET:
            field_dict["description"] = description
        if db_id is not UNSET:
            field_dict["db_id"] = db_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        name = _parse_name(d.pop("name"))

        library_id = d.pop("library_id")

        searchdatabase_ref = d.pop("searchdatabase_ref")

        accession = d.pop("accession")

        def _parse_seq(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        seq = _parse_seq(d.pop("seq", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _db_id = d.pop("db_id", UNSET)
        db_id: Union[Unset, UUID]
        if isinstance(_db_id, Unset):
            db_id = UNSET
        else:
            db_id = UUID(_db_id)

        db_sequence = cls(
            id=id,
            name=name,
            library_id=library_id,
            searchdatabase_ref=searchdatabase_ref,
            accession=accession,
            seq=seq,
            description=description,
            db_id=db_id,
        )

        db_sequence.additional_properties = d
        return db_sequence

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
