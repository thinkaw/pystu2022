# import web3

# print('hello,world')
# print('hello,world too~')

# i = '='*10
# print('+'*10)

# from web3 import Web3
# from web3 import  HTTPProvider
# from web3 import Web3, EthereumTesterProvider
# w3 = Web3(EthereumTesterProvider())

# block = w3.eth.getBlock('latest')
# # 输出区块信息
# print(block)
# # 输出区块链
# print(block['number'])
# # 输出区块哈希码
# print(block['hash'])
# # 用另外一种方法输出区块的哈希码
# print(block.hash)

from web3 import Web3
# w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/352b1dd7e7934d9cb476cecc9691c5bc'))
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
block = w3.eth.getBlock(12345)
# 输出区块信息
print(block)
# 输出区块链
print(block['timestamp'])