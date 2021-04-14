import yfinance as yf


print("please enter the ticker you would like to view: ")
getTicker= input()
tickerRetreve= yf.Ticker(getTicker)
print(tickerRetreve.info)

