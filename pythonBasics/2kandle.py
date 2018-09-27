from sklearn.tree import DecisionTreeRegressor
import pandas as pd

data = pd.read_csv('AAPL.csv')

col = ['Date', 'Open', 'Volume']
x = data[col]
tcol = ['Close']
y = data[tcol]

# define our model
model = DecisionTreeRegressor()
#print(x)
# fit our model in this case maybe i need to handle NAN
model.fit(x,y)
#sometimes u also need to learn how to handle categorical data with one hot encoding

    #option one drop nan: datanomissingval = x.dropna(axis =1)
#model.fit(x, y)
