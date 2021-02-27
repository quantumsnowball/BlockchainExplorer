from pathlib import Path
import requests
import json


ETHERSCAN_API_KEY = (Path(__file__).parent / './api_keys/etherscan').read_text()


def eth_balance(address):
    url = 'https://api.etherscan.io/api?' \
          'module=account&' \
          'action=balance&' \
          f'address={address}&' \
          'tag=latest&' \
          f'apikey={ETHERSCAN_API_KEY}'
    resp = requests.get(url)
    obj = json.loads(resp.content)
    return obj


def erc20_token_total_supply(contract_address):
    url = 'https://api.etherscan.io/api?' \
          'module=stats&' \
          'action=tokensupply&' \
          f'contractaddress={contract_address}&' \
          f'apikey={ETHERSCAN_API_KEY}'
    resp = requests.get(url)
    obj = json.loads(resp.content)
    return obj
