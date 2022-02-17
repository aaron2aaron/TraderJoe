#import alpaca_trade_api as tradeapi
import datetime
import time
lastGMETrade = datetime.datetime.now()
time.sleep(100)
#When trading, confirm it is not a day trade 
if lastGMETrade.day == datetime.datetime.now().day:
    print("Day Trade - CANCELLED" + "\n" + "Last traded" + str(datetime.datetime.now() - lastGMETrade))

"""

privateKey = ""
publicKey = ""
baseURL = "https://paper-api.alpaca.markets/"
api = tradeapi.REST(publicKey, privateKey, baseURL)

bars = api.get_bars("GME", 'minute', 5)
for bar in bars:
    print(bar)
    """