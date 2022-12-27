from __future__ import annotations

from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import (
	OrgFreedesktopAccountsInterface,
    OrgFreedesktopAccountsUserInterface
)

ACCOUNT_SERVICE_BUS_NAME = 'org.freedesktop.Accounts'
ACCOUNT_SERVICE_PATH = '/org/freedesktop/Accounts'

class AccountsService(OrgFreedesktopAccountsInterface):
    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
		TODO
        """
        super().__init__()
        self._connect(
            ACCOUNT_SERVICE_BUS_NAME,
            ACCOUNT_SERVICE_PATH,
            bus
        )

class AccountsUser(OrgFreedesktopAccountsUserInterface):
    def __init__(self, uid: int, bus: Optional[SdBus] = None) -> None:
        """
		TODO
        """
        super().__init__()
        self._connect(
            ACCOUNT_SERVICE_BUS_NAME,
            f"{ACCOUNT_SERVICE_PATH}/User{uid}",
            bus
        )
