import alpaca_trade_api as tradeapi
privateKey = ""
publicKey = ""
baseURL = "https://paper-api.alpaca.markets/"
api = tradeapi.REST(publicKey, privateKey, baseURL)

bars = api.get_bars("GME", 'minute', 5)
for bar in bars:
    print(bar)