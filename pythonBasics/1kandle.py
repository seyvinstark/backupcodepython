import pandas as pd
data = pd.read_csv('AAPL.csv')
#print(data.describe)
#print(data.columns)
#dates = data.Date
#print(dates)

col = ['Date','Open','Volume']
x = data[col]
tcol = ['Close']
y = data[tcol]
print(x)

#usually the one col u want to predict is y and the data u use to predict it will be called x in this case
#coldata is x and close will be y since i want to predict the close