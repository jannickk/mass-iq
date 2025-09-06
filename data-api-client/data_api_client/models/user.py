import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        email (str):
        logon_name (str):
        is_active (Union[Unset, bool]):  Default: True.
        is_superuser (Union[Unset, bool]):  Default: False.
        full_name (Union[None, Unset, str]):
        create_time (Union[None, Unset, datetime.datetime]):
        update_time (Union[None, Unset, datetime.datetime]):
        added_by_id (Union[None, UUID, Unset]):
        upd_by_id (Union[None, UUID, Unset]):
        descr (Union[None, Unset, str]):
        status (Union[Unset, int]):  Default: 0.
        other_attributes (Union[None, Unset, str]):
        sync_source (Union[None, Unset, str]):
        api_access (Union[None, Unset, bool]):  Default: True.
        app_object_id (Union[None, Unset, str]):
        app_client_id (Union[None, Unset, str]):
        object_id (Union[None, Unset, str]):
        subject (Union[None, Unset, str]):
        vault_entity_id (Union[None, Unset, str]):
        id (Union[Unset, UUID]):
    """

    email: str
    logon_name: str
    is_active: Union[Unset, bool] = True
    is_superuser: Union[Unset, bool] = False
    full_name: Union[None, Unset, str] = UNSET
    create_time: Union[None, Unset, datetime.datetime] = UNSET
    update_time: Union[None, Unset, datetime.datetime] = UNSET
    added_by_id: Union[None, UUID, Unset] = UNSET
    upd_by_id: Union[None, UUID, Unset] = UNSET
    descr: Union[None, Unset, str] = UNSET
    status: Union[Unset, int] = 0
    other_attributes: Union[None, Unset, str] = UNSET
    sync_source: Union[None, Unset, str] = UNSET
    api_access: Union[None, Unset, bool] = True
    app_object_id: Union[None, Unset, str] = UNSET
    app_client_id: Union[None, Unset, str] = UNSET
    object_id: Union[None, Unset, str] = UNSET
    subject: Union[None, Unset, str] = UNSET
    vault_entity_id: Union[None, Unset, str] = UNSET
    id: Union[Unset, UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        logon_name = self.logon_name

        is_active = self.is_active

        is_superuser = self.is_superuser

        full_name: Union[None, Unset, str]
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        create_time: Union[None, Unset, str]
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        update_time: Union[None, Unset, str]
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        added_by_id: Union[None, Unset, str]
        if isinstance(self.added_by_id, Unset):
            added_by_id = UNSET
        elif isinstance(self.added_by_id, UUID):
            added_by_id = str(self.added_by_id)
        else:
            added_by_id = self.added_by_id

        upd_by_id: Union[None, Unset, str]
        if isinstance(self.upd_by_id, Unset):
            upd_by_id = UNSET
        elif isinstance(self.upd_by_id, UUID):
            upd_by_id = str(self.upd_by_id)
        else:
            upd_by_id = self.upd_by_id

        descr: Union[None, Unset, str]
        if isinstance(self.descr, Unset):
            descr = UNSET
        else:
            descr = self.descr

        status = self.status

        other_attributes: Union[None, Unset, str]
        if isinstance(self.other_attributes, Unset):
            other_attributes = UNSET
        else:
            other_attributes = self.other_attributes

        sync_source: Union[None, Unset, str]
        if isinstance(self.sync_source, Unset):
            sync_source = UNSET
        else:
            sync_source = self.sync_source

        api_access: Union[None, Unset, bool]
        if isinstance(self.api_access, Unset):
            api_access = UNSET
        else:
            api_access = self.api_access

        app_object_id: Union[None, Unset, str]
        if isinstance(self.app_object_id, Unset):
            app_object_id = UNSET
        else:
            app_object_id = self.app_object_id

        app_client_id: Union[None, Unset, str]
        if isinstance(self.app_client_id, Unset):
            app_client_id = UNSET
        else:
            app_client_id = self.app_client_id

        object_id: Union[None, Unset, str]
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        subject: Union[None, Unset, str]
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        vault_entity_id: Union[None, Unset, str]
        if isinstance(self.vault_entity_id, Unset):
            vault_entity_id = UNSET
        else:
            vault_entity_id = self.vault_entity_id

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "logon_name": logon_name,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if upd_by_id is not UNSET:
            field_dict["upd_by_id"] = upd_by_id
        if descr is not UNSET:
            field_dict["descr"] = descr
        if status is not UNSET:
            field_dict["status"] = status
        if other_attributes is not UNSET:
            field_dict["other_attributes"] = other_attributes
        if sync_source is not UNSET:
            field_dict["sync_source"] = sync_source
        if api_access is not UNSET:
            field_dict["api_access"] = api_access
        if app_object_id is not UNSET:
            field_dict["app_object_id"] = app_object_id
        if app_client_id is not UNSET:
            field_dict["app_client_id"] = app_client_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if vault_entity_id is not UNSET:
            field_dict["vault_entity_id"] = vault_entity_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        logon_name = d.pop("logon_name")

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        def _parse_full_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        def _parse_create_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = isoparse(data)

                return create_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        create_time = _parse_create_time(d.pop("create_time", UNSET))

        def _parse_update_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = isoparse(data)

                return update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_added_by_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_by_id_type_0 = UUID(data)

                return added_by_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        added_by_id = _parse_added_by_id(d.pop("added_by_id", UNSET))

        def _parse_upd_by_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upd_by_id_type_0 = UUID(data)

                return upd_by_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        upd_by_id = _parse_upd_by_id(d.pop("upd_by_id", UNSET))

        def _parse_descr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        descr = _parse_descr(d.pop("descr", UNSET))

        status = d.pop("status", UNSET)

        def _parse_other_attributes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        other_attributes = _parse_other_attributes(d.pop("other_attributes", UNSET))

        def _parse_sync_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sync_source = _parse_sync_source(d.pop("sync_source", UNSET))

        def _parse_api_access(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        api_access = _parse_api_access(d.pop("api_access", UNSET))

        def _parse_app_object_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_object_id = _parse_app_object_id(d.pop("app_object_id", UNSET))

        def _parse_app_client_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_client_id = _parse_app_client_id(d.pop("app_client_id", UNSET))

        def _parse_object_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_subject(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_vault_entity_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vault_entity_id = _parse_vault_entity_id(d.pop("vault_entity_id", UNSET))

        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        user = cls(
            email=email,
            logon_name=logon_name,
            is_active=is_active,
            is_superuser=is_superuser,
            full_name=full_name,
            create_time=create_time,
            update_time=update_time,
            added_by_id=added_by_id,
            upd_by_id=upd_by_id,
            descr=descr,
            status=status,
            other_attributes=other_attributes,
            sync_source=sync_source,
            api_access=api_access,
            app_object_id=app_object_id,
            app_client_id=app_client_id,
            object_id=object_id,
            subject=subject,
            vault_entity_id=vault_entity_id,
            id=id,
        )

        user.additional_properties = d
        return user

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
