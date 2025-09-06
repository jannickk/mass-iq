from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeptideEvidence")


@_attrs_define
class PeptideEvidence:
    """
    Attributes:
        id (str): An unambiguous unique identifier within the scope of use.
        name (Union[None, str]): the name according to the XML document
        library_id (int): Reference to the library id which is an integer.
        db_sequence_ref (str): Reference to DBSequence according to XML document
        db_sequence_ref_db (UUID):
        peptide_ref (str): Reference to the identified peptide according to XML document
        peptide_ref_db (UUID):
        translationtable_ref (Union[None, Unset, str]): Reference to translation table
        frame (Union[None, Unset, int]): Translation frame (custom allowed_frames enum could be added)
        isdecoy (Union[None, Unset, bool]): Is a decoy sequence Default: False.
        peptide_start (Union[None, Unset, int]): Start position in protein
        peptide_end (Union[None, Unset, int]): End position in protein
        pre (Union[None, Unset, str]): Previous flanking residue
        post (Union[None, Unset, str]): Post flanking residue
        db_id (Union[Unset, UUID]):
    """

    id: str
    name: Union[None, str]
    library_id: int
    db_sequence_ref: str
    db_sequence_ref_db: UUID
    peptide_ref: str
    peptide_ref_db: UUID
    translationtable_ref: Union[None, Unset, str] = UNSET
    frame: Union[None, Unset, int] = UNSET
    isdecoy: Union[None, Unset, bool] = False
    peptide_start: Union[None, Unset, int] = UNSET
    peptide_end: Union[None, Unset, int] = UNSET
    pre: Union[None, Unset, str] = UNSET
    post: Union[None, Unset, str] = UNSET
    db_id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, str]
        name = self.name

        library_id = self.library_id

        db_sequence_ref = self.db_sequence_ref

        db_sequence_ref_db = str(self.db_sequence_ref_db)

        peptide_ref = self.peptide_ref

        peptide_ref_db = str(self.peptide_ref_db)

        translationtable_ref: Union[None, Unset, str]
        if isinstance(self.translationtable_ref, Unset):
            translationtable_ref = UNSET
        else:
            translationtable_ref = self.translationtable_ref

        frame: Union[None, Unset, int]
        if isinstance(self.frame, Unset):
            frame = UNSET
        else:
            frame = self.frame

        isdecoy: Union[None, Unset, bool]
        if isinstance(self.isdecoy, Unset):
            isdecoy = UNSET
        else:
            isdecoy = self.isdecoy

        peptide_start: Union[None, Unset, int]
        if isinstance(self.peptide_start, Unset):
            peptide_start = UNSET
        else:
            peptide_start = self.peptide_start

        peptide_end: Union[None, Unset, int]
        if isinstance(self.peptide_end, Unset):
            peptide_end = UNSET
        else:
            peptide_end = self.peptide_end

        pre: Union[None, Unset, str]
        if isinstance(self.pre, Unset):
            pre = UNSET
        else:
            pre = self.pre

        post: Union[None, Unset, str]
        if isinstance(self.post, Unset):
            post = UNSET
        else:
            post = self.post

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
                "db_sequence_ref": db_sequence_ref,
                "db_sequence_ref_db": db_sequence_ref_db,
                "peptide_ref": peptide_ref,
                "peptide_ref_db": peptide_ref_db,
            }
        )
        if translationtable_ref is not UNSET:
            field_dict["translationtable_ref"] = translationtable_ref
        if frame is not UNSET:
            field_dict["frame"] = frame
        if isdecoy is not UNSET:
            field_dict["isdecoy"] = isdecoy
        if peptide_start is not UNSET:
            field_dict["peptide_start"] = peptide_start
        if peptide_end is not UNSET:
            field_dict["peptide_end"] = peptide_end
        if pre is not UNSET:
            field_dict["pre"] = pre
        if post is not UNSET:
            field_dict["post"] = post
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

        db_sequence_ref = d.pop("db_sequence_ref")

        db_sequence_ref_db = UUID(d.pop("db_sequence_ref_db"))

        peptide_ref = d.pop("peptide_ref")

        peptide_ref_db = UUID(d.pop("peptide_ref_db"))

        def _parse_translationtable_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        translationtable_ref = _parse_translationtable_ref(d.pop("translationtable_ref", UNSET))

        def _parse_frame(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        frame = _parse_frame(d.pop("frame", UNSET))

        def _parse_isdecoy(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        isdecoy = _parse_isdecoy(d.pop("isdecoy", UNSET))

        def _parse_peptide_start(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        peptide_start = _parse_peptide_start(d.pop("peptide_start", UNSET))

        def _parse_peptide_end(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        peptide_end = _parse_peptide_end(d.pop("peptide_end", UNSET))

        def _parse_pre(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pre = _parse_pre(d.pop("pre", UNSET))

        def _parse_post(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post = _parse_post(d.pop("post", UNSET))

        _db_id = d.pop("db_id", UNSET)
        db_id: Union[Unset, UUID]
        if isinstance(_db_id, Unset):
            db_id = UNSET
        else:
            db_id = UUID(_db_id)

        peptide_evidence = cls(
            id=id,
            name=name,
            library_id=library_id,
            db_sequence_ref=db_sequence_ref,
            db_sequence_ref_db=db_sequence_ref_db,
            peptide_ref=peptide_ref,
            peptide_ref_db=peptide_ref_db,
            translationtable_ref=translationtable_ref,
            frame=frame,
            isdecoy=isdecoy,
            peptide_start=peptide_start,
            peptide_end=peptide_end,
            pre=pre,
            post=post,
            db_id=db_id,
        )

        peptide_evidence.additional_properties = d
        return peptide_evidence

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
