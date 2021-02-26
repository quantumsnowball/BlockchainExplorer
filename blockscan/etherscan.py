from pathlib import Path


ETHERSCAN_API_KEY = (Path(__file__).parent / './api_keys/bscscan').read_text()
