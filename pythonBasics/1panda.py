# this makes the rows title defined and the data attributed however we like
import pandas as pd
data = [[30,21],[45,5]]
df = pd.DataFrame(data,columns=['Apples','Bananas'],index=['first','last'])
print(df)
#another way to do that
print(pd.DataFrame({'Apples':[30],'Bananas':[21]}))

# this gives rows and name indexes
data ={'Apples':[35,41],'Bananas':[21,34]}
df = pd.DataFrame(data,index=['2017 Sales','2018 Sales'])
print(df)


#to create a serie with its name

data = ['4 cups','1 cup','2 large','1 can']
serie = pd.Series(data,index=['Flour','Milk','Eggs','Spam'], name = 'Dinner')
print(serie)


data1 = [['1','sammy'],['2','tshepang'],['3','sam'],['4','alixe'],['5','christian']]
df1 = pd.DataFrame(data1,columns=['ID','NAME'])
print(df1)