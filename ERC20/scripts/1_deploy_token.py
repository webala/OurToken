from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000, 'ether')

def main():
    account = get_account()
    print(account)
    our_token = OurToken.deploy(INITIAL_SUPPLY, {"from": account})
    print(our_token.name())