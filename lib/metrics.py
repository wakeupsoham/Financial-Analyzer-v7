import numpy as np
import pandas as pd

def calculate_arithmetic_returns(prices):
    """Calculates daily arithmetic returns (percentage change)."""
    return prices.pct_change().dropna()

def calculate_log_returns(prices):
    """Calculates daily logarithmic returns."""
    return np.log(prices / prices.shift(1)).dropna()

def calculate_cumulative_returns(returns):
    """Calculates cumulative returns from daily returns."""
    return (1 + returns).cumprod() - 1

def calculate_daily_volatility(returns):
    """Calculates annualized volatility assuming 252 trading days."""
    return returns.std() * np.sqrt(252)

def calculate_rolling_volatility(returns, window=21):
    """Calculates annualized rolling volatility."""
    return returns.rolling(window=window).std() * np.sqrt(252)

def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    """
    Calculates the Sharpe Ratio.
    Assumes returns are daily. risk_free_rate should be annual (e.g., 0.02 for 2%).
    """
    # Convert annual RFR to daily
    daily_rfr = (1 + risk_free_rate) ** (1/252) - 1
    excess_returns = returns - daily_rfr
    return (excess_returns.mean() / returns.std()) * np.sqrt(252)

def calculate_sortino_ratio(returns, risk_free_rate=0.0, target_return=0.0):
    """
    Calculates the Sortino Ratio (downside risk only).
    """
    daily_rfr = (1 + risk_free_rate) ** (1/252) - 1
    excess_returns = returns - daily_rfr
    
    # Downside returns are those below the target (or RFR)
    downside_returns = excess_returns[excess_returns < 0]
    
    downside_deviation = downside_returns.std() * np.sqrt(252)
    
    # Handle division by zero
    return (excess_returns.mean() * 252) / downside_deviation.replace(0, np.nan)
