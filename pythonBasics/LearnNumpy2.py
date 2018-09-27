import numpy as np
import time
import sys

size = 1000
#list array
l1 = range(size)
l2 = range(size)

for l3 in range(1,11,2):
    print(l3)

#numpy array
a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print('python list took : ',(time.time()-start)* 1000)
start = time.time()
result = a1 +a2

print('the numpy took ',(time.time()-start)*1000)


b1=np.array([2,45,6])
b2 = np.array([4,4,12])
c= b1+b2
print(c)