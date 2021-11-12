#!/bin/env python3

from bitcoinrpc.authproxy import AuthServiceProxy

# Requires a local bitcoind running mainnet (testnet port 18232)
api = AuthServiceProxy("http://lmr:lmr@127.0.0.1:8332")

print("hello, world!")

print("test the api to bitcoind, should see help text:")
print(api.help(''))