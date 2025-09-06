from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isolation_window_count import IsolationWindowCount
    from ..models.ms_level_count import MsLevelCount
    from ..models.polarity_count import PolarityCount
    from ..models.transition import Transition


T = TypeVar("T", bound="AcquisitionMetaData")


@_attrs_define
class AcquisitionMetaData:
    """
    Attributes:
        acquisition_name (str): This is the ID of the user
        source_files (list[str]): The vendor files that constitute this acquisition
        acquisition_start (int):
        software_version (str):
        acquisition_mode (str):
        vendor (str):
        polarity_count (Union[None, Unset, list['PolarityCount']]): How many scans are negative and how many are
            positive
        instrument_serial_number (Union[None, Unset, str]):
        ms_level_count (Union[None, Unset, list['MsLevelCount']]): How many Spectra are MS1 levels and how many are MS2
            levels
        isolation_window_count (Union[None, Unset, list['IsolationWindowCount']]):
        transitions (Union[None, Unset, list['Transition']]):
        number_of_spectra (Union[None, Unset, int]):
        number_of_chromatograms (Union[None, Unset, int]):
    """

    acquisition_name: str
    source_files: list[str]
    acquisition_start: int
    software_version: str
    acquisition_mode: str
    vendor: str
    polarity_count: Union[None, Unset, list["PolarityCount"]] = UNSET
    instrument_serial_number: Union[None, Unset, str] = UNSET
    ms_level_count: Union[None, Unset, list["MsLevelCount"]] = UNSET
    isolation_window_count: Union[None, Unset, list["IsolationWindowCount"]] = UNSET
    transitions: Union[None, Unset, list["Transition"]] = UNSET
    number_of_spectra: Union[None, Unset, int] = UNSET
    number_of_chromatograms: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acquisition_name = self.acquisition_name

        source_files = self.source_files

        acquisition_start = self.acquisition_start

        software_version = self.software_version

        acquisition_mode = self.acquisition_mode

        vendor = self.vendor

        polarity_count: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.polarity_count, Unset):
            polarity_count = UNSET
        elif isinstance(self.polarity_count, list):
            polarity_count = []
            for polarity_count_type_0_item_data in self.polarity_count:
                polarity_count_type_0_item = polarity_count_type_0_item_data.to_dict()
                polarity_count.append(polarity_count_type_0_item)

        else:
            polarity_count = self.polarity_count

        instrument_serial_number: Union[None, Unset, str]
        if isinstance(self.instrument_serial_number, Unset):
            instrument_serial_number = UNSET
        else:
            instrument_serial_number = self.instrument_serial_number

        ms_level_count: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.ms_level_count, Unset):
            ms_level_count = UNSET
        elif isinstance(self.ms_level_count, list):
            ms_level_count = []
            for ms_level_count_type_0_item_data in self.ms_level_count:
                ms_level_count_type_0_item = ms_level_count_type_0_item_data.to_dict()
                ms_level_count.append(ms_level_count_type_0_item)

        else:
            ms_level_count = self.ms_level_count

        isolation_window_count: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.isolation_window_count, Unset):
            isolation_window_count = UNSET
        elif isinstance(self.isolation_window_count, list):
            isolation_window_count = []
            for isolation_window_count_type_0_item_data in self.isolation_window_count:
                isolation_window_count_type_0_item = isolation_window_count_type_0_item_data.to_dict()
                isolation_window_count.append(isolation_window_count_type_0_item)

        else:
            isolation_window_count = self.isolation_window_count

        transitions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.transitions, Unset):
            transitions = UNSET
        elif isinstance(self.transitions, list):
            transitions = []
            for transitions_type_0_item_data in self.transitions:
                transitions_type_0_item = transitions_type_0_item_data.to_dict()
                transitions.append(transitions_type_0_item)

        else:
            transitions = self.transitions

        number_of_spectra: Union[None, Unset, int]
        if isinstance(self.number_of_spectra, Unset):
            number_of_spectra = UNSET
        else:
            number_of_spectra = self.number_of_spectra

        number_of_chromatograms: Union[None, Unset, int]
        if isinstance(self.number_of_chromatograms, Unset):
            number_of_chromatograms = UNSET
        else:
            number_of_chromatograms = self.number_of_chromatograms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acquisitionName": acquisition_name,
                "sourceFiles": source_files,
                "acquisitionStart": acquisition_start,
                "softwareVersion": software_version,
                "acquisitionMode": acquisition_mode,
                "vendor": vendor,
            }
        )
        if polarity_count is not UNSET:
            field_dict["polarityCount"] = polarity_count
        if instrument_serial_number is not UNSET:
            field_dict["instrumentSerialNumber"] = instrument_serial_number
        if ms_level_count is not UNSET:
            field_dict["msLevelCount"] = ms_level_count
        if isolation_window_count is not UNSET:
            field_dict["isolationWindowCount"] = isolation_window_count
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if number_of_spectra is not UNSET:
            field_dict["numberOfSpectra"] = number_of_spectra
        if number_of_chromatograms is not UNSET:
            field_dict["numberOfChromatograms"] = number_of_chromatograms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.isolation_window_count import IsolationWindowCount
        from ..models.ms_level_count import MsLevelCount
        from ..models.polarity_count import PolarityCount
        from ..models.transition import Transition

        d = dict(src_dict)
        acquisition_name = d.pop("acquisitionName")

        source_files = cast(list[str], d.pop("sourceFiles"))

        acquisition_start = d.pop("acquisitionStart")

        software_version = d.pop("softwareVersion")

        acquisition_mode = d.pop("acquisitionMode")

        vendor = d.pop("vendor")

        def _parse_polarity_count(data: object) -> Union[None, Unset, list["PolarityCount"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                polarity_count_type_0 = []
                _polarity_count_type_0 = data
                for polarity_count_type_0_item_data in _polarity_count_type_0:
                    polarity_count_type_0_item = PolarityCount.from_dict(polarity_count_type_0_item_data)

                    polarity_count_type_0.append(polarity_count_type_0_item)

                return polarity_count_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["PolarityCount"]], data)

        polarity_count = _parse_polarity_count(d.pop("polarityCount", UNSET))

        def _parse_instrument_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instrument_serial_number = _parse_instrument_serial_number(d.pop("instrumentSerialNumber", UNSET))

        def _parse_ms_level_count(data: object) -> Union[None, Unset, list["MsLevelCount"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ms_level_count_type_0 = []
                _ms_level_count_type_0 = data
                for ms_level_count_type_0_item_data in _ms_level_count_type_0:
                    ms_level_count_type_0_item = MsLevelCount.from_dict(ms_level_count_type_0_item_data)

                    ms_level_count_type_0.append(ms_level_count_type_0_item)

                return ms_level_count_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MsLevelCount"]], data)

        ms_level_count = _parse_ms_level_count(d.pop("msLevelCount", UNSET))

        def _parse_isolation_window_count(data: object) -> Union[None, Unset, list["IsolationWindowCount"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                isolation_window_count_type_0 = []
                _isolation_window_count_type_0 = data
                for isolation_window_count_type_0_item_data in _isolation_window_count_type_0:
                    isolation_window_count_type_0_item = IsolationWindowCount.from_dict(
                        isolation_window_count_type_0_item_data
                    )

                    isolation_window_count_type_0.append(isolation_window_count_type_0_item)

                return isolation_window_count_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IsolationWindowCount"]], data)

        isolation_window_count = _parse_isolation_window_count(d.pop("isolationWindowCount", UNSET))

        def _parse_transitions(data: object) -> Union[None, Unset, list["Transition"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transitions_type_0 = []
                _transitions_type_0 = data
                for transitions_type_0_item_data in _transitions_type_0:
                    transitions_type_0_item = Transition.from_dict(transitions_type_0_item_data)

                    transitions_type_0.append(transitions_type_0_item)

                return transitions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Transition"]], data)

        transitions = _parse_transitions(d.pop("transitions", UNSET))

        def _parse_number_of_spectra(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_spectra = _parse_number_of_spectra(d.pop("numberOfSpectra", UNSET))

        def _parse_number_of_chromatograms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_chromatograms = _parse_number_of_chromatograms(d.pop("numberOfChromatograms", UNSET))

        acquisition_meta_data = cls(
            acquisition_name=acquisition_name,
            source_files=source_files,
            acquisition_start=acquisition_start,
            software_version=software_version,
            acquisition_mode=acquisition_mode,
            vendor=vendor,
            polarity_count=polarity_count,
            instrument_serial_number=instrument_serial_number,
            ms_level_count=ms_level_count,
            isolation_window_count=isolation_window_count,
            transitions=transitions,
            number_of_spectra=number_of_spectra,
            number_of_chromatograms=number_of_chromatograms,
        )

        acquisition_meta_data.additional_properties = d
        return acquisition_meta_data

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
