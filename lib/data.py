import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    """
    Fetches historical adjusted close prices for the given tickers.
    
    Args:
        tickers (list): List of ticker symbols (e.g., ['AAPL', 'MSFT']).
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        
    Returns:
        pd.DataFrame: DataFrame containing Adjusted Close prices.
    """
    print(f"Fetching data for {tickers} from {start_date} to {end_date}...")
    try:
        data = yf.download(tickers, start=start_date, end=end_date, progress=False)
        
        # Handle MultiIndex columns (e.g. ('Adj Close', 'AAPL'))
        if isinstance(data.columns, pd.MultiIndex):
            # check available levels for 'Adj Close' or 'Close'
            level_0 = data.columns.get_level_values(0)
            if 'Adj Close' in level_0:
                data = data.xs('Adj Close', axis=1, level=0)
            elif 'Close' in level_0:
                data = data.xs('Close', axis=1, level=0)
        elif 'Adj Close' in data.columns:
            data = data['Adj Close']
        elif 'Close' in data.columns:
            data = data['Close']
            
        print(f"Data shape after filtering: {data.shape}")
        
        # If we only fetched one ticker, it might come as a Series or single-column DF.
        if isinstance(data, pd.Series):
            data = data.to_frame(name=tickers[0])
            
        print("Data fetch successful.")
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
