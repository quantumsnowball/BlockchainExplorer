import click


@click.command()
def cli():
    from .etherscan import eth_balance, erc20_token_total_supply
    print(eth_balance('0x1311160372Ca71507f69FF8B3Ca2FeF0630dBb26')) # AUTOv2
    print(erc20_token_total_supply('0x1f9840a85d5af5bf1d1762f925bdaddc4201f984')) # UniswapV2
    print(erc20_token_total_supply('0x111111111117dc0aa78b770fa6a738034120c302')) # 1INCH Token
    from .bscscan import bep20_token_total_supply
    print(bep20_token_total_supply('0xa184088a740c695e156f91f5cc086a06bb78b827')) # AUTOv2
    print(bep20_token_total_supply('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82')) # PancakeSwap Token
