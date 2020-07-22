'''

Simple Monte Carlo Simulation for stock prices

Uses a pandas dataframe and numpy to simulate random variations in price

7/19/2020

Jeb Ely

'''

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Start and End dates for the data
start = dt.datetime(2019, 7, 18)
end = dt.datetime(2020, 7, 18)

# Choose the stock you want to simulate
ticker = 'SPY'

prices = web.DataReader(ticker, 'yahoo', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

# Number of simulations
num_sims = 1000

# Number of trading days to simulate
num_days = 252

sim_df = pd.DataFrame()


for x in range(num_sims):
    count = 0
    daily_vol= returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == (num_days - 1):
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
        
    sim_df[x] = price_series
    
# storing the ending price in an array
results = sim_df[num_days - 1]
    
# plot the simlutaions
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: ' + ticker)
plt.plot(sim_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()

# histogram of ending stock values
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: ' + ticker)
plt.hist(results,bins='auto')
plt.xlabel('Price')
plt.ylabel('# of Sims')
plt.show()