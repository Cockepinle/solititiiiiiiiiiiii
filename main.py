from web3 import Web3
from web3.middleware import geth_poa_middleware
from conract_info import address_contract, abi

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=address_contract, abi=abi)
#print(contract.address)
#print(w3.eth.get_balance('0x8B114f51b452FF5c3D991EfbD43e4188b202B487'))

accounts = w3.eth.accounts

for i, account in enumerate(accounts):
    balance = w3.eth.get_balance(account)
    balance_in_ether = w3.from_wei(balance, 'ether')
    print(f"Баланс {i+1} аккаунта: {balance_in_ether} ETH")

for i in range(len(accounts)):     
    print(f"Баланс {i+1} аккаунт: {w3.eth.get_balance(accounts[i])}") 