import pandas_datareader.data as web
import math
import pandas as pd
all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG','TSLA']}
price = pd.DataFrame({ticker: data['Adj Close']
 for ticker, data in all_data.items()})
volume =pd.DataFrame({ticker: data['Volume']
 for ticker, data in all_data.items()})
#********
#1
A=(price.loc['2018-12-31',['GOOG']])['GOOG']
print("1- Google closing price in 2018: "+"$"+str(round(A,2)))
#********
#2
x=[]
for i in range(0,len(price.index)):
 if str(price.index[i]).split('-')[0]=='2020' and str(price.index[i]).split('-')[1]=='10':
    x.append(i)
y=0
for i in range(0,len(x)):
 y=y+(volume.iloc[x[i],[0]])
print("2- Apple trading volume in Oct 2020:",int(y))
#********
#3
Open= pd.DataFrame({ticker: data['Open']
 for ticker, data in all_data.items()})
l=[]
for i in range(0,len(Open.index)):
 if str(Open.index[i]).split('-')[0]=='2019':
    l.append(i)
m=0
for j in range(0,len(l)):
 if Open.iloc[l[j],[2]].values >150:
 m=m+1
print("3- Number of days Microsoft stock price opened higher than $150: ",m)
#********
#4
AdjClose= pd.DataFrame({ticker: data['Adj Close']
 for ticker, data in all_data.items()})
r=[]
for i in range(0,len(AdjClose.index)):
 if str(AdjClose.index[i]).split('-')[0]=='2017':
    r.append(i)
AdjClose_New=AdjClose.iloc[r[0]:]
max=AdjClose_New.pct_change().corr().iloc[0:-1]['TSLA'].max()
d=((AdjClose_New.pct_change().corr()[AdjClose_New.pct_change().corr()['TSLA']==max]).index)[0]
print("4- Tesla has the highest correlation with: ",d)
#********
#5
e=[]
for i in range(0,len(volume.index)):
 if str(volume.index[i]).split('-')[0]=='2020' and str(volume.index[i]).split('-')[1]=='01':
    e.append(i)
all_data_New=all_data['IBM'].iloc[e[0]:e[len(e)-1]+1,[-2,-1]]
f=round(sum(all_data_New['Volume']*all_data_New['Adj Close']),2)
print("5- IBM's trading amount in Jan 2020: "+"$"+str(f))
