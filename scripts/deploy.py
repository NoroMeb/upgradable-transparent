from scripts.utils import get_account, encode_function_data
from brownie import Vault, ProxyAdmin, TransparentUpgradeableProxy, Contract


def main():
    account = get_account()
    vault = Vault.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    vault_encoded_initializer_function = encode_function_data(vault.store, 1)
    proxy = TransparentUpgradeableProxy.deploy(
        vault.address,
        proxy_admin,
        vault_encoded_initializer_function,
        {"from": account},
    )
    proxy_vault = Contract.from_abi("Vault", proxy.address, Vault.abi)
    print("_______")
    print(proxy_vault.retrieve())
    print("_______")


def deploy_vault():
    account = get_account
