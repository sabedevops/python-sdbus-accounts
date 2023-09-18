#!/usr/bin/env python
import asyncio
import sdbus
from sdbus_async.accounts import AccountsService, AccountsUser

bus = sdbus.sd_bus_open_system()

async def test_accounts_service() -> None:
    accounts = AccountsService(bus)
    print('CachedUsers: ', await accounts.list_cached_users())

async def test_accounts_user() -> None:
    user = AccountsUser(1000, bus)
    print('UserName: ', await user.user_name )

async def main():
    accounts = await test_accounts_service()
    user = await test_accounts_user()

asyncio.run(main())
