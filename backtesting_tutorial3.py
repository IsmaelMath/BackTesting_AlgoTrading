# youtube.com/watch?v=xljQpeYQYKl
import yfinance as yf
import pandas as pd
import numpy as np

from backtesting import Backtest, Strategy
#from backtesting.test import GOOG

GOOG = yf.download("PETR4.SA", start="2023-01-01")

GOOG["Signal"] = np.random.randint(-1, 2, len(GOOG))

print(GOOG)

class SignalStrategy(Strategy):
    
    def init(self):
        pass

    def next(self):
        
        current_signal = self.data.Signal[-1]
        
        if current_signal == 1:
            if not self.position:
                self.buy()
        elif current_signal == -1:
            if self.position:
                self.position.close()

bt = Backtest(GOOG, SignalStrategy, cash=10_000)

stats = bt.run()
bt.plot()
#print(stats)
