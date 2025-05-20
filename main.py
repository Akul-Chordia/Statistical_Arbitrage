import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, coint

ticker1 = input("Ticker 1 : ")
ticker2 = input("Ticker 2 : ")

tickers = [ticker1, ticker2]
data = yf.download(tickers, start='2018-01-01', end='2023-12-31', auto_adjust=True)


data = data['Close'].dropna()
data.columns.name = None

def adf_test(series, name=''):
    result = adfuller(series)
    print(f'ADF Test for {name}:')
    print(f'ADF Statistic : {result[0]}')
    print(f'p-value       : {result[1]}')
    print('Stationary' if result[1] < 0.05 else 'Non-stationary')
    print('-' * 50)

adf_test(data[ticker1], ticker1)
adf_test(data[ticker2], ticker2)

score, pvalue, _ = coint(data[ticker1], data[ticker2])
print(f'Engle-Granger Cointegration Test p-value: {pvalue}')
print('Cointegrated' if pvalue < 0.05 else 'Not cointegrated')
print('-' * 50)

def calculate_spread_zscore(X, Y):
    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    spread = Y - model.predict(X)
    zscore = (spread - spread.mean()) / spread.std()
    return spread, zscore

spread, zscore = calculate_spread_zscore(data[ticker1], data[ticker2])

plt.figure(figsize=(12, 6))
plt.plot(zscore)
plt.axhline(1.0, color='red', linestyle='--')
plt.axhline(-1.0, color='green', linestyle='--')
plt.axhline(0, color='black', linestyle='-')
plt.title('Z-Score of Spread')
plt.show()

entry_threshold = 1.0
exit_threshold = 0.0

longs = zscore < -entry_threshold
shorts = zscore > entry_threshold
exits = abs(zscore) < exit_threshold

positions = pd.DataFrame(index=data.index, columns=[ticker1, ticker2])
positions.iloc[:] = 0

positions.loc[longs, ticker1] = -1
positions.loc[longs, ticker2] = 1

positions.loc[shorts, ticker1] = 1
positions.loc[shorts, ticker2] = -1

positions.loc[exits, :] = 0

daily_returns = data.pct_change()
strategy_returns = (positions.shift(1) * daily_returns).sum(axis=1)

cumulative_returns = (1 + strategy_returns).cumprod()

plt.figure(figsize=(12, 6))
plt.plot(cumulative_returns, label='Strategy Returns')
plt.title('Cumulative Returns of Pairs Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.show()
