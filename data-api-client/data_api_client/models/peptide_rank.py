from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PeptideRank")


@_attrs_define
class PeptideRank:
    """
    Attributes:
        rank (int):
        peptide_evidence_ref (str):
        db_sequence_ref (str):
        peptide_intensity (float):
        db_id (UUID):
    """

    rank: int
    peptide_evidence_ref: str
    db_sequence_ref: str
    peptide_intensity: float
    db_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        peptide_evidence_ref = self.peptide_evidence_ref

        db_sequence_ref = self.db_sequence_ref

        peptide_intensity = self.peptide_intensity

        db_id = str(self.db_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
                "peptide_evidence_ref": peptide_evidence_ref,
                "db_sequence_ref": db_sequence_ref,
                "peptide_intensity": peptide_intensity,
                "db_id": db_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank")

        peptide_evidence_ref = d.pop("peptide_evidence_ref")

        db_sequence_ref = d.pop("db_sequence_ref")

        peptide_intensity = d.pop("peptide_intensity")

        db_id = UUID(d.pop("db_id"))

        peptide_rank = cls(
            rank=rank,
            peptide_evidence_ref=peptide_evidence_ref,
            db_sequence_ref=db_sequence_ref,
            peptide_intensity=peptide_intensity,
            db_id=db_id,
        )

        peptide_rank.additional_properties = d
        return peptide_rank

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
