Usually i don't concern myself for adding a description but here we are
# Financial Analyzer 
this is a partially reliable Python tool to fetch stock data (taken from Yahoo Finance), calculates returns/volatility, and visualize performance with fancy graphs beacuse why not.

# Follow these steps to start your painful journey

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run analysis:
   ```bash
   python main.py
   ```
3. View results:
   Check the `output/` folder for volatility and return plots.

## features that i think are cool
- Arithmetic & Log Returns
- Sharpe & Sortino Ratios
- Rolling Volatility
- Matplotlib visualizations

## Example output ss

![Cumulative Returns](output/cumulative_returns.png)
![Rolling Volatility](output/rolling_volatility.png)
![Returns Distribution](output/returns_distribution.png)
