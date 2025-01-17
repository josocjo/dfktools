"""
https://docs.uniswap.org/protocol/V2/reference/smart-contracts/factory
"""

from web3 import Web3

CONTRACT_ADDRESS_Serendale = '0x9014B937069918bd319f80e8B3BB4A2cf6FAA5F7'
CONTRACT_ADDRESS_Crystalvale = '0x794C07912474351b3134E6D6B3B7b3b4A07cbAAa'

ABI = """
    [
        {"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},
        {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},
        {"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},
        {"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},
        {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"stateMutability":"nonpayable","type":"function"},
        {"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
        {"inputs":[],"name":"pairCodeHash","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"pure","type":"function"},
        {"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"stateMutability":"nonpayable","type":"function"}
    ]
    """


def all_pairs_length_Serendale(rpc_address):

    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Serendale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.allPairsLength().call()


def all_pairs_Serendale(index, rpc_address):
    '''
    Return the address of the liquidity pair at index
    :param index:
    :param rpc_address:
    :return:
    '''
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Serendale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.allPairs(index).call()


def get_pair_Serendale(token_address_1, token_address_2, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Serendale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPair(token_address_1, token_address_2).call()

def all_pairs_length_Crystalvale(rpc_address):

    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Crystalvale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.allPairsLength().call()


def all_pairs_Crystalvale(index, rpc_address):
    '''
    Return the address of the liquidity pair at index
    :param index:
    :param rpc_address:
    :return:
    '''
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Crystalvale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.allPairs(index).call()


def get_pair_Crystalvale(token_address_1, token_address_2, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS_Crystalvale)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getPair(token_address_1, token_address_2).call()
