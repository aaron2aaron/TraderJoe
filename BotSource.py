import alpaca_trade_api as tradeapi
import datetime
import time
"""
lastGMETrade = datetime.datetime.now()
time.sleep(100)
#When trading, confirm it is not a day trade 
if lastGMETrade.day == datetime.datetime.now().day:
    print("Day Trade - CANCELLED" + "\n" + "Last traded" + str(datetime.datetime.now() - lastGMETrade))
"""
publicKey = "PKKEDRLM7ELD6TNUL3E5"
privateKey = "3P5en0knAcPGciXmSG6t0SAPGIYavxytsgsuQcar"
baseURL = "https://paper-api.alpaca.markets/"
api = tradeapi.REST(publicKey, privateKey, baseURL)
"""
api.submit_order(
        symbol="GME",
        qty=1,
        side="buy",
        type="market",
        time_in_force="gtc"
)
"""
account = api.get_account()
#print(account)
trade = False
last = 0
while True:
    print(datetime.datetime.now())
    data = api.get_barset("SPY", "minute", limit=1)
    spyDATA = data["SPY"]
    for data in spyDATA:
        print(data.l, "vs", last)
    if data.l < (last * .997):
        api.submit_order(symbol="SPY", qty=1, side="buy",type="market",time_in_force='gtc')
        trade = True
    if data.l > (last * 1.003) and trade == True:
        api.submit_order(symbol="SPY", qty=1, side="sell",type="market",time_in_force="gtc")
        trade = False
    last = data.l
    time.sleep(3)
    
"""
from alpaca_trade_api.stream import Stream
async def trade_callback(t):
    print('trade',t)

stream = Stream(publicKey, privateKey, baseURL) 

stream.subscribe_trades(trade_callback, 'SPY')

stream.run()
"""
