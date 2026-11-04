import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.set_page_config(page_title="SmartFolio Tracker", layout="wide")
st.title("📈 SmartFolio Portfolio Tracker & Rebalancer")

st.sidebar.header("Portfolio Inputs")
tickers = st.sidebar.text_input("Enter Tickers (comma-separated)", "GOOGL, QLD, 000660.KS")

if tickers:
    ticker_list = [t.strip() for t in tickers.split(",")]
    st.write(f"Tracking Assets: **{', '.join(ticker_list)}**")
    
    # Placeholder for AI assistant session: 
    # Fetch historical data, compute drawdown, and build rebalancing logic
    st.info("Ready for feature integration: Data pipeline and Plotly charts will be implemented here.")
