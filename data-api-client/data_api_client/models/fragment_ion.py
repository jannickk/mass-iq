from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FragmentIon")


@_attrs_define
class FragmentIon:
    """
    Attributes:
        db_sequence_ref (str): The db sequence reference according to the XML document
        db_sequence_ref_db (UUID):
        elutionfr_time (float):
        library_id (int): Reference to the library id which is an integer.
        peptide_evidence_ref (str): The peptide evidence reference according to the XML document
        peptide_evidence_ref_db (UUID):
        peptide_ref (str): The peptide reference according to the XML document
        peptide_ref_db (UUID):
        rank (int):
        spectrum_title (str): The spectrum identification result reference according to the XML document
        precursor_calculated_mz (float):
        precursor_experimental_mz (float):
        precursor_charge (int):
        fragment_ion_charge (int):
        fragment_ion_mz (float):
        fragment_ion_type (str):
        index (int):
        intensity (float):
        scan_start_time (float):
        db_id (Union[Unset, UUID]):
    """

    db_sequence_ref: str
    db_sequence_ref_db: UUID
    elutionfr_time: float
    library_id: int
    peptide_evidence_ref: str
    peptide_evidence_ref_db: UUID
    peptide_ref: str
    peptide_ref_db: UUID
    rank: int
    spectrum_title: str
    precursor_calculated_mz: float
    precursor_experimental_mz: float
    precursor_charge: int
    fragment_ion_charge: int
    fragment_ion_mz: float
    fragment_ion_type: str
    index: int
    intensity: float
    scan_start_time: float
    db_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        db_sequence_ref = self.db_sequence_ref

        db_sequence_ref_db = str(self.db_sequence_ref_db)

        elutionfr_time = self.elutionfr_time

        library_id = self.library_id

        peptide_evidence_ref = self.peptide_evidence_ref

        peptide_evidence_ref_db = str(self.peptide_evidence_ref_db)

        peptide_ref = self.peptide_ref

        peptide_ref_db = str(self.peptide_ref_db)

        rank = self.rank

        spectrum_title = self.spectrum_title

        precursor_calculated_mz = self.precursor_calculated_mz

        precursor_experimental_mz = self.precursor_experimental_mz

        precursor_charge = self.precursor_charge

        fragment_ion_charge = self.fragment_ion_charge

        fragment_ion_mz = self.fragment_ion_mz

        fragment_ion_type = self.fragment_ion_type

        index = self.index

        intensity = self.intensity

        scan_start_time = self.scan_start_time

        db_id: Union[Unset, str] = UNSET
        if not isinstance(self.db_id, Unset):
            db_id = str(self.db_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "db_sequence_ref": db_sequence_ref,
                "db_sequence_ref_db": db_sequence_ref_db,
                "elutionfr_time": elutionfr_time,
                "library_id": library_id,
                "peptide_evidence_ref": peptide_evidence_ref,
                "peptide_evidence_ref_db": peptide_evidence_ref_db,
                "peptide_ref": peptide_ref,
                "peptide_ref_db": peptide_ref_db,
                "rank": rank,
                "spectrum_title": spectrum_title,
                "precursor_calculated_mz": precursor_calculated_mz,
                "precursor_experimental_mz": precursor_experimental_mz,
                "precursor_charge": precursor_charge,
                "fragment_ion_charge": fragment_ion_charge,
                "fragment_ion_mz": fragment_ion_mz,
                "fragment_ion_type": fragment_ion_type,
                "index": index,
                "intensity": intensity,
                "scan_start_time": scan_start_time,
            }
        )
        if db_id is not UNSET:
            field_dict["db_id"] = db_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        db_sequence_ref = d.pop("db_sequence_ref")

        db_sequence_ref_db = UUID(d.pop("db_sequence_ref_db"))

        elutionfr_time = d.pop("elutionfr_time")

        library_id = d.pop("library_id")

        peptide_evidence_ref = d.pop("peptide_evidence_ref")

        peptide_evidence_ref_db = UUID(d.pop("peptide_evidence_ref_db"))

        peptide_ref = d.pop("peptide_ref")

        peptide_ref_db = UUID(d.pop("peptide_ref_db"))

        rank = d.pop("rank")

        spectrum_title = d.pop("spectrum_title")

        precursor_calculated_mz = d.pop("precursor_calculated_mz")

        precursor_experimental_mz = d.pop("precursor_experimental_mz")

        precursor_charge = d.pop("precursor_charge")

        fragment_ion_charge = d.pop("fragment_ion_charge")

        fragment_ion_mz = d.pop("fragment_ion_mz")

        fragment_ion_type = d.pop("fragment_ion_type")

        index = d.pop("index")

        intensity = d.pop("intensity")

        scan_start_time = d.pop("scan_start_time")

        _db_id = d.pop("db_id", UNSET)
        db_id: Union[Unset, UUID]
        if isinstance(_db_id, Unset):
            db_id = UNSET
        else:
            db_id = UUID(_db_id)

        fragment_ion = cls(
            db_sequence_ref=db_sequence_ref,
            db_sequence_ref_db=db_sequence_ref_db,
            elutionfr_time=elutionfr_time,
            library_id=library_id,
            peptide_evidence_ref=peptide_evidence_ref,
            peptide_evidence_ref_db=peptide_evidence_ref_db,
            peptide_ref=peptide_ref,
            peptide_ref_db=peptide_ref_db,
            rank=rank,
            spectrum_title=spectrum_title,
            precursor_calculated_mz=precursor_calculated_mz,
            precursor_experimental_mz=precursor_experimental_mz,
            precursor_charge=precursor_charge,
            fragment_ion_charge=fragment_ion_charge,
            fragment_ion_mz=fragment_ion_mz,
            fragment_ion_type=fragment_ion_type,
            index=index,
            intensity=intensity,
            scan_start_time=scan_start_time,
            db_id=db_id,
        )

        fragment_ion.additional_properties = d
        return fragment_ion

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
