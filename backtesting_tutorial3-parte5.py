import pandas as pd
import numpy as np
import ta
import yfinance as yf

from backtesting import Backtest, Strategy
#from backtesting.test import GOOG
from backtesting.lib import crossover

GOOG = yf.download("PETR4.SA", start="2023-01-01")

class TrailingStrategy(Strategy):

    __dollar_amount = 20.
    

    def init(self):
        super().init()
        

    def set_trailing_sl(self, dollar_amount: float = 6):
        self.__dollar_amount = dollar_amount

    def next(self):
        super().next()
        index = len(self.data)-1

        for trade in self.trades:
            if trade.is_long:
                trade.sl = max(trade.sl or -np.inf,
                        self.data.Close[index] - self.__dollar_amount)
            else:
                trade.sl = min(trade.sl or np.inf,
                        self.data.Close[index] + self.dollar_amount)
class Strat(TrailingStrategy):

    def init(self):
        super().init()
        super().set_trailing_sl(5)
        

    def next(self):
        super().next()

        if self.position:
            pass
        else:
            price = self.data.Close[-1]
            self.buy(size=1, sl = price - 1.5, tp = price + 1)

bt = Backtest(GOOG, Strat, cash=15_000)
stats = bt.run()
print(stats)
bt.plot()
