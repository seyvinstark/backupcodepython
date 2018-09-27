import pandas as pd
#import seaborn as sns


reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
# to see the column names
print(reviews.columns)
#to select the description columns
data = ['description']
print(reviews[data])
#this does the same thing as the method above
reviews.description
#this get the description for one column
reviews.description[0]

#this get a whole 1 st rows
reviews.iloc[0]
#the first 10 items from the description column
reviews.description[0:10]
#does the same thing
reviews.iloc[0:10]
#specific rows
print(reviews.loc[[1,2,3,4,8]])
#specific column and rows
data = ['country','province','region_1','region_2']
ans=reviews[data]
print(ans.iloc[[0,1,10,100]])

#first hundred rows of 2 columns
data = ['country','variety']
ans=reviews[data]
print(ans.iloc[0:100])
#select all rows where all the wines are from italy
reviews.loc[reviews.country=='Italy']
#where region2 arent NAN values
reviews.loc[reviews.region_2.notnull()]
#whats their rating or their point

reviews.points[0:1000]
#the last 1000 values
reviews.points[-1000:]
#points for the wines from italy
reviews.points[reviews.country=='Italy']
#Who produces more above-averagely good wines, France or Italy? Select the `country` column, but only  when said `country` is one of those two options, _and_ the `points` column is greater than or equal to 90.
reviews[reviews.country.isin(['Italy','France'])&(reviews.points >=90)].country

