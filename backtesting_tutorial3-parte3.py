import pandas as pd
import numpy as np
import yfinance as yf

from backtesting import Backtest, Strategy

dados = yf.download("PETR4.SA", start="2022-01-01")

def indicator(data):
    return data.Close.s.pct_change(periods=7) * 100

class MomentumStrategy(Strategy):

    def init(self):
    
        self.pct_change = self.I(indicator, self.data)
        #print(self.pct_change)
        #pass

    def next(self):
        change = self.pct_change[-1]

        if self.position:
            if change <0:
               
                self.position.close()
        else:
            if change > 5 and self.pct_change[-2] > 5:
                
                self.buy()
        #pass

bt = Backtest(dados, MomentumStrategy, cash=1_000)

stats = bt.run()
print(stats)

# Verificar como colocar stop_loss e stop_gain estrategia visualmente é boa
# só precisa ser mais calibrada.
