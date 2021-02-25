import requests
import json


with open('api_keys/bscscan', 'r') as f:
    BSCSCAN_API_KEY = f.read()
with open('api_keys/etherscan', 'r') as f:
    ETHERSCAN_API_KEY = f.read()


def bnb_balance(address):
    url = 'https://api.bscscan.com/api?' \
          'module=account&' \
          'action=balance&' \
          f'address={address}&' \
          'tag=latest&' \
          f'apikey={BSCSCAN_API_KEY}'
    resp = requests.get(url)
    obj = json.loads(resp.content)
    return obj


def bnb_normal_transaction(address):
    url = 'https://api.bscscan.com/api?' \
          'module=account&' \
          'action=txlist&' \
          f'address={address}&' \
          'startblock=0&' \
          'endblock=99999999&' \
          'sort=asc&' \
          f'apikey={BSCSCAN_API_KEY}'
    resp = requests.get(url)
    obj = json.loads(resp.content)
    return obj


def bep20_token_total_supply(contract_address):
    url = 'https://api.bscscan.com/api?' \
          'module=stats&' \
          'action=tokensupply&' \
          f'contractaddress={contract_address}&' \
          f'apikey={BSCSCAN_API_KEY}'
    resp = requests.get(url)
    obj = json.loads(resp.content)
    return obj


if __name__ == '__main__':
    print(bep20_token_total_supply('0xa184088a740c695e156f91f5cc086a06bb78b827')) # AUTOv2
    print(bep20_token_total_supply('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')) # PancakeSwap Token
