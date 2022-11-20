from scripts.utils import get_account, upgrade, encode_function_data
from brownie import VaultV2, ProxyAdmin, TransparentUpgradeableProxy, Contract


def main():
    account = get_account()
    vault_v2 = VaultV2.deploy({"from": account})
    proxy_admin = ProxyAdmin[-1]
    proxy = TransparentUpgradeableProxy[-1]
    tx = upgrade(account, proxy, vault_v2.address, proxy_admin, vault_v2.store, 4)
    tx.wait(1)
    proxy_vault_v2 = Contract.from_abi("VaultV2", proxy.address, VaultV2.abi)
    print("_______")
    print(proxy_vault_v2.retrieve())
    print("_______")

    tx2 = proxy_vault_v2.increment({"from": account})
    tx2.wait(1)
    print("_______")
    print(proxy_vault_v2.retrieve())
    print("_______")
