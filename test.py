# stock data into excel

import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

user_ticker = str(input('Please input your ticker > \t'))

download_file = (r'C:\Users\robas\github\Beginner\stock data\{0}.xlsx'.format(user_ticker))

start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df = pdr.get_data_yahoo(user_ticker,start,end)


df.to_excel(download_file,
            sheet_name = user_ticker,)

daily_returns = df['Adj Close'].pct_change()
monthly_returns = df['Adj Close'].resample('M').ffill().pct_change()
cum_returns = (daily_returns + 1).cumprod()


fig = plt.figure()
ax1 = fig.add_axes(([0.1,0.1,0.8,0.8]))
ax1.plot(cum_returns)
ax1.set_xlabel('Date')
ax1.set_ylabel('Growth of $1 Investment')
ax1.set_title("{0} daily culmulative returns".format(user_ticker))
plt.show()
