print('this is the start')
import numpy as np
import sys
a = np.array([1,2,4])

print(a)
print(a[0])
#observation:it looks like a normal python list so why use it
#deduction there must be something special about it
#it takes less memory,its fast its convenient

list = range(1000)#observation nmbers in the range of 1000

print(sys.getsizeof(5) * len(list)) #observation: size in bytes of the entire list item*nmber 14 bytes per item
array = np.arange(1000)
print(array.size * array.itemsize) #observation: size of the entire numpy array, 4 bytes per item