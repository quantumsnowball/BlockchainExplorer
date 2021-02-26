import click


@click.command()
def cli():
    from .etherscan import ETHERSCAN_API_KEY
    from .bscscan import bep20_token_total_supply
    print(bep20_token_total_supply('0xa184088a740c695e156f91f5cc086a06bb78b827')) # AUTOv2
    print(bep20_token_total_supply('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')) # PancakeSwap Token
