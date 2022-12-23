"""TODO"""
# Generated by:
# python -m sdbus gen-from-connection --system \
#     org.freedesktop.Accounts \
#     /org/freedesktop/Accounts \
#     /org/freedesktop/Accounts/User1000

# Disables errors in generated client code
# pylint: disable=redefined-builtin, invalid-name, unused-import
# pylint: disable=missing-class-docstring, missing-function-docstring
# pylint: disable=too-many-public-methods

from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (DbusDeprecatedFlag, DbusInterfaceCommonAsync,
                   DbusNoReplyFlag, DbusPropertyConstFlag,
                   DbusPropertyEmitsChangeFlag,
                   DbusPropertyEmitsInvalidationFlag, DbusPropertyExplicitFlag,
                   DbusUnprivilegedFlag, dbus_method_async,
                   dbus_property_async, dbus_signal_async)


class OrgFreedesktopAccountsInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Accounts',
):

    @dbus_method_async(
        result_signature='ao',
    )
    async def list_cached_users(
        self,
    ) -> List[str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='x',
        result_signature='o',
    )
    async def find_user_by_id(
        self,
        id: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def find_user_by_name(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ssi',
        result_signature='o',
    )
    async def create_user(
        self,
        name: str,
        fullname: str,
        account_type: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def cache_user(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def uncache_user(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='xb',
    )
    async def delete_user(
        self,
        id: int,
        remove_files: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def daemon_version(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def has_no_users(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def has_multiple_users(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ao',
    )
    def automatic_login_users(self) -> List[str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def user_added(self) -> str:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def user_deleted(self) -> str:
        raise NotImplementedError


class ComEndlessmParentalControlsAccountInfoInterface(
    DbusInterfaceCommonAsync,
    interface_name='com.endlessm.ParentalControls.AccountInfo',
):

    @dbus_property_async(
        property_signature='b',
    )
    def is_parent(self) -> bool:
        raise NotImplementedError


class OrgFreedesktopAccountsUserInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Accounts.User',
):

    @dbus_method_async(
        input_signature='s',
    )
    async def set_user_name(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_real_name(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_email(
        self,
        email: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_language(
        self,
        language: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_x_session(
        self,
        x_session: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_session(
        self,
        session: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_session_type(
        self,
        session_type: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_location(
        self,
        location: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_home_directory(
        self,
        homedir: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_shell(
        self,
        shell: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_icon_file(
        self,
        filename: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='b',
    )
    async def set_locked(
        self,
        locked: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='i',
    )
    async def set_account_type(
        self,
        account_type: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='i',
    )
    async def set_password_mode(
        self,
        mode: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
    )
    async def set_password(
        self,
        password: str,
        hint: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def set_password_hint(
        self,
        hint: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='b',
    )
    async def set_automatic_login(
        self,
        enabled: bool,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='xxxxxx',
    )
    async def get_password_expiration_policy(
        self,
    ) -> Tuple[int, int, int, int, int, int]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def uid(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def user_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def real_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
    )
    def account_type(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def home_directory(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def shell(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def email(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def language(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def session(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def session_type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def x_session(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def location(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def login_frequency(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='x',
    )
    def login_time(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(xxa{sv})',
    )
    def login_history(self) -> List[Tuple[int, int, Dict[str, Tuple[str, Any]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def icon_file(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def saved(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def locked(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
    )
    def password_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def password_hint(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def automatic_login(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def system_account(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def local_account(self) -> bool:
        raise NotImplementedError

    @dbus_signal_async(
    )
    def changed(self) -> None:
        raise NotImplementedError


class ComEndlessmParentalControlsAppFilterInterface(
    DbusInterfaceCommonAsync,
    interface_name='com.endlessm.ParentalControls.AppFilter',
):

    @dbus_property_async(
        property_signature='(bas)',
    )
    def app_filter(self) -> Tuple[bool, List[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(sa{ss})',
    )
    def oars_filter(self) -> Tuple[str, Dict[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def allow_user_installation(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def allow_system_installation(self) -> bool:
        raise NotImplementedError


class ComEndlessmParentalControlsSessionLimitsInterface(
    DbusInterfaceCommonAsync,
    interface_name='com.endlessm.ParentalControls.SessionLimits',
):

    @dbus_property_async(
        property_signature='u',
    )
    def limit_type(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(uu)',
    )
    def daily_schedule(self) -> Tuple[int, int]:
        raise NotImplementedError
