# Portfolio Analysis function in FinanceYourFuture Project

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

plt.style.use('fivethirtyeight')

# Assume these are the options available for our pension app
Port_Assets = ['BND', 'VOO', 'TLT', 'QQQ', 'VGK']

# Assign default weight recommended by FinanaceYourFuture
weights = np.array([0.2, 0.2, 0.3, 0.1, 0.2])

# assume user starts portfolio with FinanaceYourFuture on 5 Mar 2019
Port_Start_Date = '2019-03-05'

today = datetime.date.today().strftime('%Y-%m-%d')

# Portfolio asset value as of today
df = pd.DataFrame()

# extract assets price of portfolio
for stock in Port_Assets:
    df[stock] = pdr.DataReader(stock, data_source='yahoo', start=Port_Start_Date, end=today)['Adj Close']

my_portfolio = df

# assume 252 trading days per year
returns = df.pct_change()
Port_Yearly_Return = np.sum(returns.mean() * weights * 252)
Return_Percent = str(round(Port_Yearly_Return, 2) * 100) + '%'
print('Your Annual Return for Current Pension Plan: ' + Return_Percent)

# Portfolio Assets Performance Visualisation
title = 'Stocks Performance in Portfolio'
my_portfolio['WMean'] = np.average(my_portfolio[Port_Assets], weights=weights, axis=1)

plt.figure(1)
plt.plot(my_portfolio) # print the overall stock performance
plt.title(title)
plt.xlabel('Date', fontsize = 15)
plt.ylabel('Stock Values USD', fontsize = 15)
plt.legend(my_portfolio.columns.values, loc = 'upper left')
plt.show()

r = Port_Yearly_Return
n = 12 # no. of months in a year
t = 40 # assumed total years of compounding
monthlycontributionin = input("Enter monthly contribution amount: $")
M = int(monthlycontributionin)
P = int(monthlycontributionin) #principal: initial balance = 1st monthly contribution
Target = input("Enter target retirement balance: $")
T = int(Target)

# Prepare a DataFrame to store the Year and Final Balance
results = pd.DataFrame(columns = ['Year', 'Amount'])

# Iterate through each year to find the ending balance
for i in range(1,t+1):
  Year = i
  Amount = P*np.power((1 + r / n), n * i)+(M)*(np.power((1+ r / n ), n * i)-1)/(r / n)
  if Amount >= T:
      T_year = 2019 + i
      print('Great Job! It is predicted that you will reach retirement goal in: ' + str(T_year))
      break

results =  results.append({'Year': Year, 'Amount': Amount}, ignore_index = True)

# Convert Year's data type to integer from a float
results['Year'] = results['Year'].astype('int')

plt.figure(2)
plt.plot(results)
plt.title('Balance Prediction')
plt.xlabel('Year (since joining FinanceYourFuture)', fontsize = 15)
plt.ylabel('Portfolio Values USD', fontsize = 15)
plt.show()