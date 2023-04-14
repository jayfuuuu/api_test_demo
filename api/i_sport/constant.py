from enum import Enum, IntEnum


class ERROR_CODE(str, Enum):
    SUCCESS = "0000"


class COUNTRY(str, Enum):
    TAIPEI = "A"
    TAICHUNG = "B"
    KEELUNG = "C"


class ACTIVITY_TYPE(IntEnum):
    SPORTS_EVENTS = 1
    SERIES_OF_EVENTS = 2
    SPORTS_COURSE = 3
