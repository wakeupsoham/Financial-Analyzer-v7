from lib import data, metrics, plotting
import pandas as pd

def main():
    # Configuration
    TICKERS = ['SPY', 'QQQ', 'GLD'] # S&P 500, Nasdaq-100, Gold
    START_DATE = '2020-01-01'
    END_DATE = '2023-12-31'
    RISK_FREE_RATE = 0.04  # 4% annual risk-free rate

    print("=== Financial Returns and Volatility Analyzer ===")
    
    # 1. Fetch Data
    prices = data.fetch_data(TICKERS, START_DATE, END_DATE)
    if prices.empty:
        print("No data found. Exiting.")
        return

    # 2. Calculate Metrics
    print("\nCalculating metrics...")
    daily_returns = metrics.calculate_arithmetic_returns(prices)
    log_returns = metrics.calculate_log_returns(prices)
    cumulative_returns = metrics.calculate_cumulative_returns(daily_returns)
    daily_volatility = metrics.calculate_daily_volatility(daily_returns)
    rolling_volatility = metrics.calculate_rolling_volatility(daily_returns, window=30)
    
    sharpe = metrics.calculate_sharpe_ratio(daily_returns, RISK_FREE_RATE)
    sortino = metrics.calculate_sortino_ratio(daily_returns, RISK_FREE_RATE)

    # 3. Display Statistics
    print("\n--- Performance Summary (Annualized) ---")
    summary = pd.DataFrame({
        'Volatility': daily_volatility,
        'Sharpe Ratio': sharpe,
        'Sortino Ratio': sortino,
        'Total Return': (1 + daily_returns).prod() - 1
    })
    print(summary)

    # 4. Generate Plots
    print("\nGenerating plots in 'output/' directory...")
    plotting.plot_cumulative_returns(cumulative_returns)
    plotting.plot_returns_distribution(daily_returns)
    plotting.plot_rolling_volatility(rolling_volatility)
    
    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()
