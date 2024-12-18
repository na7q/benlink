from __future__ import annotations
from ..bitfield import (
    Bitfield,
    bf_int,
    bf_int_enum,
    bf_dyn,
    bf_bytes,
    bf_str,
    bf_lit_int,
)
import typing as t
from enum import IntEnum
from .common import ReplyStatus


class PacketFormat(IntEnum):
    BSS = 0
    APRS = 1


# Really should be named "Packet Settings" or something
class BSSSettings(Bitfield):
    max_fwd_times: int = bf_int(4)
    time_to_live: int = bf_int(4)
    ptt_release_send_location: bool
    ptt_release_send_id_info: bool
    ptt_release_send_bss_user_id: bool  # (Applies when BSS is turned on)
    should_share_location: bool
    send_pwr_voltage: bool
    packet_format: PacketFormat = bf_int_enum(PacketFormat, 1)
    allow_position_check: bool
    _pad: t.Literal[0] = bf_lit_int(1, default=0)
    aprs_ssid: int = bf_int(4)
    _pad2: t.Literal[0] = bf_lit_int(4, default=0)
    location_share_interval: int = bf_int(8)
    bss_user_id: int = bf_int(32)
    ptt_release_id_info: bytes = bf_bytes(12)
    beacon_message: str = bf_str(18)
    aprs_symbol: str = bf_str(2)
    aprs_callsign: str = bf_str(6)


class BSSSettingsExt(Bitfield):
    bss_user_id: int = bf_int(64)
    max_fwd_times: int = bf_int(4)
    time_to_live: int = bf_int(4)
    ptt_release_send_location: bool
    ptt_release_send_id_info: bool
    ptt_release_send_bss_user_id: bool  # (Applies when BSS is turned on)
    should_share_location: bool
    send_pwr_voltage: bool
    packet_format: PacketFormat = bf_int_enum(PacketFormat, 1)
    allow_position_check: bool
    _pad: t.Literal[0] = bf_lit_int(1, default=0)
    aprs_ssid: int = bf_int(4)
    _pad2: t.Literal[0] = bf_lit_int(4, default=0)
    location_share_interval: int = bf_int(8)
    # bss_user_id (reordered; 32)
    ptt_release_id_info: bytes = bf_bytes(12)
    beacon_message: str = bf_str(18)
    aprs_symbol: str = bf_str(2)
    aprs_callsign: str = bf_str(6)
    # bss_user_id_upper (reordered; 32)

    _reorder = [*range(368, 368+32), *range(32, 32+32)]


class ReadBSSSettingsBody(Bitfield):
    unknown: int = bf_int(8)


def bss_settings_disc(_: None, n: int):
    if n == BSSSettings.length():
        return BSSSettings
    if n == BSSSettingsExt.length():
        return BSSSettingsExt
    raise ValueError(f"Unknown size for BSSSettings ({n})")


class ReadBSSSettingsReplyBody(Bitfield):
    reply_status: ReplyStatus = bf_int_enum(ReplyStatus, 8)
    bss_settings: BSSSettings | BSSSettingsExt = bf_dyn(bss_settings_disc)


class WriteBSSSettingsBody(Bitfield):
    bss_settings: BSSSettings | BSSSettingsExt = bf_dyn(bss_settings_disc)


class WriteBSSSettingsReplyBody(Bitfield):
    reply_status: ReplyStatus = bf_int_enum(ReplyStatus, 8)
