#youtube.com/watch?v=FpSopSupizo
import yfinance as yf
import ta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from backtesting import Backtest, Strategy
from backtesting.lib 
import crossover


class SMAcross(Strategy):
    n1 = 50
    n2 = 100

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n1)
        self.sma2 = self.I(ta.trend.sma_indicator, pd.Series(close), self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()
df = yf.download("PETR4.SA", start="2020-01-01")

bt = Backtest(df, SMAcross, cash=1000, commission=0.002, exclusive_orders=True)
output = bt.run()

#bt.plot()

stats, optim = bt.optimize(n1 = range(50,160,10), n2=range(50,160,10),
        constraint= lambda x: x.n2 - x.n1 > 20, maximize="Return [%]",
        max_tries=200, random_state=0, return_heatmap=True)

optim = pd.DataFrame(optim)
print(optim["Return [%]"].max())
#hm = optim.groupby(["n1", "n2"]).mean().unstack()
#print(hm)
#sns.heatmap(hm[::-1], cmap="viridis")
#plt.show()
