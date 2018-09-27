#to read a csv file  and put it into a dataframe
import pandas as pd
data = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv')
df = pd.DataFrame(data)
print(df)
#to read an excel file
data = pd.read_excel('../input/publicassistance/xls_files_all/WICAgencies2014ytd.xls')
df = pd.DataFrame(data)
print(df)

#to transform our data frame to a csv file


q6_df = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
sol = q6_df.to_csv('cows_and_goats.csv')
#to read from sqlite

import sqlite3
connection = sqlite3.connect("../input/pitchfork-data/database.sqlite")
select = pd.read_sql_query('SELECT * FROM ARTISTS',connection)
print(select)