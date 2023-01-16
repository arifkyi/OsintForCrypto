import requests
from web3 import Web3
import sys

address = sys.argv[1]

# Get Ether balance in wei
url = "https://api.etherscan.io/api"
params = {'module': 'account', 'action': 'balance', 'address': address, 'tag': 'latest', 'apikey': 'YourApiKeyToken'}
response = requests.get(url, params=params)
data = response.json()
wei_balance = int(data["result"])

# Convert Ether balance from wei to ETH
w3 = Web3()
eth_balance = w3.fromWei(wei_balance, 'ether')
print(f"balance is {eth_balance} ETH")

# Get current Ether price in USD
price_url = "https://api.coingecko.com/api/v3/simple/price"
price_params = {'ids':'ethereum','vs_currencies':'usd'}
price_response = requests.get(price_url,params = price_params)
price_data = price_response.json()
eth_usd_price = price_data['ethereum']['usd']

# Convert Ether balance from ETH to USD
usd_balance = float(eth_balance) * eth_usd_price
print(f"balance is {usd_balance} USD")
