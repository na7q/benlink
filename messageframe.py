import typing as t
from enum import IntEnum, IntFlag


class FrameOptions(IntFlag):
    NONE = 0
    CHECKSUM = 1


class FrameTypeGroup(IntEnum):
    BASIC = 2
    EXTENDED = 10


class FrameTypeExtended(IntEnum):
    GET_BT_SIGNAL = 769
    GET_DEV_STATE_VAR = 16387


class FrameTypeBasic(IntEnum):
    UNKNOWN = 0
    GET_DEV_ID = 1
    SET_REG_TIMES = 2
    GET_REG_TIMES = 3
    GET_DEV_INFO = 4
    READ_STATUS = 5
    REGISTER_NOTIFICATION = 6
    CANCEL_NOTIFICATION = 7
    GET_NOTIFICATION = 8
    EVENT_NOTIFICATION = 9
    READ_SETTINGS = 10
    WRITE_SETTINGS = 11
    STORE_SETTINGS = 12
    READ_RF_CH = 13
    WRITE_RF_CH = 14
    GET_IN_SCAN = 15
    SET_IN_SCAN = 16
    SET_REMOTE_DEVICE_ADDR = 17
    GET_TRUSTED_DEVICE = 18
    DEL_TRUSTED_DEVICE = 19
    GET_HT_STATUS = 20
    SET_HT_ON_OFF = 21
    GET_VOLUME = 22
    SET_VOLUME = 23
    RADIO_GET_STATUS = 24
    RADIO_SET_MODE = 25
    RADIO_SEEK_UP = 26
    RADIO_SEEK_DOWN = 27
    RADIO_SET_FREQ = 28
    READ_ADVANCED_SETTINGS = 29
    WRITE_ADVANCED_SETTINGS = 30
    HT_SEND_DATA = 31
    SET_POSITION = 32
    READ_BSS_SETTINGS = 33
    WRITE_BSS_SETTINGS = 34
    FREQ_MODE_SET_PAR = 35
    FREQ_MODE_GET_STATUS = 36
    READ_RDA1846S_AGC = 37
    WRITE_RDA1846S_AGC = 38
    READ_FREQ_RANGE = 39
    WRITE_DE_EMPH_COEFFS = 40
    STOP_RINGING = 41
    SET_TX_TIME_LIMIT = 42
    SET_IS_DIGITAL_SIGNAL = 43
    SET_HL = 44
    SET_DID = 45
    SET_IBA = 46
    GET_IBA = 47
    SET_TRUSTED_DEVICE_NAME = 48
    SET_VOC = 49
    GET_VOC = 50
    SET_PHONE_STATUS = 51
    READ_RF_STATUS = 52
    PLAY_TONE = 53
    GET_DID = 54
    GET_PF = 55
    SET_PF = 56
    RX_DATA = 57
    WRITE_REGION_CH = 58
    WRITE_REGION_NAME = 59
    SET_REGION = 60
    SET_PP_ID = 61
    GET_PP_ID = 62
    READ_ADVANCED_SETTINGS2 = 63
    WRITE_ADVANCED_SETTINGS2 = 64
    UNLOCK = 65
    DO_PROG_FUNC = 66
    SET_MSG = 67
    GET_MSG = 68
    BLE_CONN_PARAM = 69
    SET_TIME = 70
    SET_APRS_PATH = 71
    GET_APRS_PATH = 72
    READ_REGION_NAME = 73
    SET_DEV_ID = 74
    GET_PF_ACTIONS = 75


class DevStateVar(IntEnum):
    START = 0
    RSSI_LOW_THRESHOLD = 1
    RSSI_HIGH_THRESHOLD = 2
    BATTERY_LOW_THRESHOLD = 3
    BATTERY_HIGH_THRESHOLD = 4
    DEVICE_STATE_CHANGED = 5
    PIO_CHANGED = 6
    DEBUG_MESSAGE = 7
    BATTERY_CHARGED = 8
    CHARGER_CONNECTION = 9
    CAPSENSE_UPDATE = 10
    USER_ACTION = 11
    SPEECH_RECOGNITION = 12
    AV_COMMAND = 13
    REMOTE_BATTERY_LEVEL = 14
    KEY = 15
    DFU_STATE = 16
    UART_RECEIVED_DATA = 17
    VMU_PACKET = 18


class ReplyStatus(IntEnum):
    SUCCESS = 0
    NOT_SUPPORTED = 1
    NOT_AUTHENTICATED = 2
    INSUFFICIENT_RESOURCES = 3
    AUTHENTICATING = 4
    INVALID_PARAMETER = 5
    INCORRECT_STATE = 6
    IN_PROGRESS = 7


class GetDevInfo(t.NamedTuple):
    body: bytes
    type_group: t.Literal[FrameTypeGroup.BASIC] = FrameTypeGroup.BASIC
    is_reply: t.Literal[False] = False
    type: t.Literal[FrameTypeBasic.GET_DEV_INFO] = FrameTypeBasic.GET_DEV_INFO
    checksum: None | int = None


class GetDevInfoReply(t.NamedTuple):
    body: bytes
    type_group: t.Literal[FrameTypeGroup.BASIC] = FrameTypeGroup.BASIC
    is_reply: t.Literal[True] = True
    type: t.Literal[FrameTypeBasic.GET_DEV_INFO] = FrameTypeBasic.GET_DEV_INFO
    checksum: None | int = None


class GetDevStateVar(t.NamedTuple):
    body: bytes
    type_group: t.Literal[FrameTypeGroup.EXTENDED] = FrameTypeGroup.EXTENDED
    is_reply: t.Literal[False] = False
    type: t.Literal[FrameTypeExtended.GET_DEV_STATE_VAR] = FrameTypeExtended.GET_DEV_STATE_VAR
    checksum: None | int = None


class GetDevStateVarReply(t.NamedTuple):
    body: bytes
    type_group: t.Literal[FrameTypeGroup.EXTENDED] = FrameTypeGroup.EXTENDED
    is_reply: t.Literal[True] = True
    type: t.Literal[FrameTypeExtended.GET_DEV_STATE_VAR] = FrameTypeExtended.GET_DEV_STATE_VAR
    checksum: None | int = None


class UnknownMessageFrame(t.NamedTuple):
    body: bytes
    type_group: int
    is_reply: bool
    type: int
    checksum: None | int = None


MessageFrame = t.Union[
    GetDevInfo,
    GetDevInfoReply,
    GetDevStateVar,
    GetDevStateVarReply,
]