# SmartFolio-Tracker

An interactive personal investment dashboard built with Python and Streamlit to monitor multi-currency equity portfolios, calculate risk-adjusted performance metrics, and automate rebalancing targets.

## Features
- **Real-Time Market Data**: Fetches historical and current price data using `yfinance`.
- **Multi-Currency Adjustment**: Supports simultaneous tracking of domestic (KRW) and international (USD) equities with automated currency conversion.
- **Risk & Performance Analytics**: Calculates Cumulative Return, Volatility, Maximum Drawdown (MDD), and Sharpe Ratio.
- **Target Rebalancing Calculator**: Generates actionable buy/sell share orders based on target asset allocation weights.

## Tech Stack
- **Language**: Python 3.10+
- **Framework**: Streamlit
- **Libraries**: Pandas, NumPy, yfinance, Plotly
