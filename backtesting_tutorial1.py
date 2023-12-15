from backtesting import Backtest, Strategy
#from backtesting.test import GOOG
from backtesting.lib import crossover

import talib
import yfinance as yf

GOOG = yf.download("PETR4.SA", start="2023-01-01")
"""
def optim_func(series):
    if series["# Trades"]<5:
        return -1
    return series["Equity Final [$]"] / series["Exposure Time [%]"]
"""
class RsiOscillator(Strategy):
    
    upper_bound = 65
    lower_bound = 40
    rsi_window = 20
    def init(self):
    	self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
    	
    

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

bt = Backtest(GOOG, RsiOscillator, cash=50_000)

#stats = bt.run()
# upper_bound = range(50, 85, 5)
# rsi_window = range(10, 30, 2)
# maximize = "Sharpe Ratio"

stats = bt.optimize(upper_bound = range(55, 85, 5), 
        lower_bound = range(10, 45, 5), 
        rsi_window = range(10, 30, 1), maximize="Sharpe Ratio") 
"""        maximize= optim_func, 
        constraint = lambda param: param.upper_bound > param.lower_bound, 
        max_tries = 100)
"""

stats = bt.run()
print(stats)
print(stats["# Trades"])
# =========================================
# Verificando os parâmetros utilizados
#print(stats["_strategy"].lower_bound)
#print(stats["_strategy"].upper_bound)
#print(stats["_strategy"].rsi_window)
# =========================================
#bt.plot()
