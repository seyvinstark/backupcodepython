import pandas as pd
import numpy as np


''''
    vectors
'''

vtr = "hello you've got 98"
print(vtr)
''''
matrix
    tables of numbers with row and columns

matrix = range(30)
for matrix in range(5,30):
    print(matrix)


'''

matrix1 = np.matrix(range(30))
print('=====================')
matrix2 = np.matrix(range(30))
matrix3 = matrix1+matrix2
print(matrix3)
print('============')
sam = range(3,30)
for i in sam:
    print(i)

matrix4 = np.matrix([[4,2,6],[6,7,8],[4,2,5]])
print(matrix4)


''''
lists
'''
list1 = ['sammy gasana','male',1000000000]
print('=============list===')
print(list1)

''''
dataframes
'''
import pandas as pd
data = [[4,5,7,4,3,34,5,7,5],[4,7,4,3,5,6]]
df = pd.DataFrame(data)
print(data)
''''
control statements
'''