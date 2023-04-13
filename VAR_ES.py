import numpy as np
import pandas as pd
from scipy.stats import norm

def calculate_var(portfolio, alpha=0.05):
    portfolio_returns = portfolio.pct_change()
    portfolio_returns.dropna(inplace=True)
    portfolio_value = portfolio.iloc[-1]
    portfolio_mean = np.mean(portfolio_returns)
    portfolio_std = np.std(portfolio_returns)
    z_value = norm.ppf(1 - alpha)
    var = portfolio_value * (portfolio_mean - z_value * portfolio_std)
    return var

def calculate_es(portfolio, alpha=0.05):
    portfolio_returns = portfolio.pct_change()
    portfolio_returns.dropna(inplace=True)
    portfolio_value = portfolio.iloc[-1]
    portfolio_mean = np.mean(portfolio_returns)
    portfolio_std = np.std(portfolio_returns)
    z_value = norm.ppf(1 - alpha)
    es = -portfolio_value * (portfolio_mean - z_value * portfolio_std)
    return es

# Example usage
portfolio_data = pd.read_csv('C:/Users/matia/Downloads/ARKK.csv', index_col='Date', parse_dates=True)
portfolio_value = portfolio_data['Close']
var = calculate_var(portfolio_value)
es = calculate_es(portfolio_value)
print('VaR: ', var)
print('ES: ', es)


