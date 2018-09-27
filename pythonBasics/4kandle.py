#model validation
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

main_file_path = '../input/house-prices-advanced-regression-techniques/train.csv' # this is the path to the Iowa data that you will use
data = pd.read_csv(main_file_path)
price =['SalePrice']
y = data[price]
cols = ['Neighborhood','YrSold','SaleCondition','HouseStyle','Street','OverallQual']
x = data[cols]
#define the model
houseModel = DecisionTreeRegressor()
#fit the model
onehotmodelx = pd.get_dummies(x)
houseModel.fit(onehotmodelx, y)

#prediction functions
print('making prediction for the next 5 houses')
print(x.head())
print('the predictions are')
predictions = houseModel.predict(onehotmodelx.head())
print(predictions)
