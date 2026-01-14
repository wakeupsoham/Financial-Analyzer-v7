import matplotlib.pyplot as plt
import pandas as pd
import os

def setup_plot_style():
    """Configures matplotlib style."""
    plt.style.use('ggplot')
    plt.rcParams['figure.figsize'] = (12, 6)

def save_plot(filename):
    """Saves the current plot to the output directory."""
    os.makedirs('output', exist_ok=True)
    path = os.path.join('output', filename)
    plt.savefig(path)
    plt.close()
    print(f"Saved plot to {path}")

def plot_cumulative_returns(cumulative_returns):
    setup_plot_style()
    cumulative_returns.plot(linewidth=2)
    plt.title('Cumulative Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend(cumulative_returns.columns)
    plt.grid(True)
    save_plot('cumulative_returns.png')

def plot_returns_distribution(returns):
    setup_plot_style()
    returns.hist(bins=50, alpha=0.6, figsize=(12, 6))
    plt.suptitle('Distribution of Daily Returns')
    save_plot('returns_distribution.png')

def plot_rolling_volatility(rolling_vol):
    setup_plot_style()
    rolling_vol.plot(linewidth=1.5)
    plt.title('30-Day Rolling Volatility (Annualized)')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend(rolling_vol.columns)
    save_plot('rolling_volatility.png')
