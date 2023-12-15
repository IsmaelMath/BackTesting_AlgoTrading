import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta as ta
from backtesting import Backtest, Strategy

data = yf.download("USIM5.SA", start="2020-01-01")

#GOOG["Signal"] = np.random.randint(-1,2, len(GOOG))

def indicator(data):
    # Data is going to be our OHLCV
    bbands = ta.bbands(close=data.Close.s, std = 1)
    
    return bbands.to_numpy().T[:3]


class BBStrategy(Strategy):
 
    def init(self):
        self.bbands = self.I(indicator, self.data)

    def next(self):

        lower_band = self.bbands[0]
        upper_band = self.bbands[2]
        
        if self.position:
            if self.data.Close[-1] > upper_band[-1]:
                self.position.close()
        else:
            if self.data.Close[-1] < lower_band[-1]:
                self.buy()

bt = Backtest(data, BBStrategy, cash=1_000)
stats = bt.run()
bt.plot()

print(stats)
