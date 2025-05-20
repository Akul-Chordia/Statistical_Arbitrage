# Statistical Arbitrage - Pairs Trading Strategy

This project implements a pairs trading strategy based on statistical arbitrage principles using Python. It uses pre-built implementations of key statistical tests using libraries like `statsmodels`.

## Overview

Pairs trading identifies two cointegrated assets whose price spread tends to revert to a mean. This strategy:

- Tests time series stationarity using the Augmented Dickey-Fuller (ADF) test.
- Detects cointegration between asset pairs via the Engle-Granger two-step method.
- Calculates the spread and normalizes it into a z-score for trading signals.
- Uses simple entry and exit thresholds on the z-score to generate trading positions.
- Backtests the strategy on historical data and plots cumulative returns.

## Features

- **Statistical Tests:** ADF test, and cointegration test
- **Z-Score Based Mean Reversion:** Trading signals generated based on spread deviation.
- **Backtesting:** Simple backtest logic with position sizing and returns calculation.
- **Visualization:** Plots for z-score and cumulative strategy returns.

## Photos

<img width="646" alt="image" src="https://github.com/user-attachments/assets/a4c13f04-3f68-43d4-a8cf-b7a5961b4178" />
<img width="840" alt="image" src="https://github.com/user-attachments/assets/81154223-3941-4cd4-97c7-57e2769c39f1" />
<img width="840" alt="image" src="https://github.com/user-attachments/assets/d6ff7289-4d4b-4a5a-aac4-a99dac14c1f1" />
