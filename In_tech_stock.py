# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:05:21 2020

@author: Siddharth Gupta
"""


import pandas as pd
import numpy as np
from datetime import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
import seaborn as sns


symbols = ["TCS.NS", "WIPRO.NS", "TECHM.NS", "INFY.NS", "HCLTECH.NS"]


start_date = datetime(2010,1,1)
end_date = datetime (2019,12,31)
stock_data = web.get_data_yahoo(symbols, start_date, end_date)
#print(stock_data)
ax, fig = plt.subplots()
for i in symbols:
    plt.plot(stock_data["Adj Close"].index, stock_data["Adj Close"][i])
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price")
plt.title("Top Indian Tech Stocks Adjusted Price")
plt.legend(symbols)
plt.show()
#data was not visibile so increased figuresize for better visualisation
plt.figure(figsize=(15,6))

for j in symbols:
    #took a long time to figure this out , alternatively this can be done as -
    #plt.plot(stock_data['Adj Close'].index,stock_data['Adj Close'][symbol].pct_change())
    stock_data["daily return"] = ((stock_data["Adj Close"][j].shift(-1) - stock_data["Adj Close"][j])/stock_data["Adj Close"][j])
    
    plt.plot(stock_data["Adj Close"].index, stock_data["daily return"])
plt.xlabel("Date")
plt.ylabel("% Change in Adjusted Close price")
plt.title("Daily Simple Rate of Return")
plt.legend(symbols)
plt.show()
plt.figure(figsize = (25,15))


for k in range(len(symbols)):
    plt.subplot(2,3,k+1)
    plt.plot(stock_data['Adj Close'].index,stock_data['Adj Close'][symbols[k]].pct_change())
    plt.xlabel("Date")
    plt.ylabel("% Change in Adjusted Close Price")
    plt.title(symbols[k])
 
symbols = ["TCS.NS", "WIPRO.NS", "TECHM.NS", "INFY.NS", "HCLTECH.NS"]
    
mean = []
for a in symbols:
    mean.append(stock_data['Adj Close'][a].pct_change().mean())
#print(mean)

plt.figure()
plt.bar(symbols,mean) 
plt.xlabel("Stock")
plt.ylabel("Mean Rate of Return")
plt.title("Mean of Daily Returns")
plt.show()

var = []
for b in symbols:
    var.append(stock_data['Adj Close'][b].pct_change().var())

plt.figure()
plt.bar(symbols,var) 
plt.xlabel("Stock")
plt.ylabel("Variance in Rate of Return")
plt.title("Vairance in Daily Returns")
plt.show()

stddev = []
for c in symbols:
    stddev.append(stock_data['Adj Close'][c].pct_change().var())

plt.figure()
plt.bar(symbols,var) 
plt.xlabel("Stock")
plt.ylabel("Standard deviation in Rate of Return")
plt.title("Standard deviation in Daily Returns")
plt.show()

agg_returns = pd.DataFrame(stock_data['Adj Close'].pct_change(), columns = symbols)
    

corr = agg_returns.corr()
#print(corr.type())
sns.heatmap(corr, annot = True)
plt.show()
#sns.pairplot(agg_returns)