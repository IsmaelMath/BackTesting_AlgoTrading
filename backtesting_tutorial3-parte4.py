from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, TrailingStrategy
print(GOOG)
x = []
class Strat(TrailingStrategy):
    
    def init(self):
        super().init()
        super().set_trailing_sl(5)
        pass

    def next(self):
        super().next()

        if self.position:
            pass
        else:
            price = self.data.Close[-1]
            self.buy(size=1, sl = price-10, tp = price+20)
            
            
            
bt = Backtest(GOOG, Strat, cash=10_000)
stats = bt.run()
#bt.plot()
print(stats)
print(len(x))
print(GOOG)

