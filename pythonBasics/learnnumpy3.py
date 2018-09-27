import numpy as np

a = np.array([4,5,4])
print(a[0])

b = np.array([[1,3],[4,5],[2,4]])
print(b)

print(b.ndim)#print the dimensions of the array
print(a.ndim)
print(a.itemsize)# the number of bytes the array has
print(b.dtype)

a = np.array([[1,2],[2,4],[5,6]], dtype=np.float64)#now they occupy 8 bytes
print(a.itemsize)
print(a.size)

print(a.shape)#it output the shape of the array 3rows and 2 cols
a = np.array([[1,2],[2,4],[5,6]], dtype=complex)

arr = np.zeros((4,4))#4rows 4 cols
print(arr)
print(np.ones((3,4)))


for i in np.arange(5):
    print(i)

print(np.linspace(1,5,10))


print(a.shape)
print(a.reshape(2,3))

print(a.ravel())#this will flatten ur array in a 1 dimensional and it return a new array

print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(np.sqrt(a))

print(np.std(b))#standard deviation



d = np.array([[1,2],[4,5]])
e = np.array([[15,45],[45,98]])

#u can do  basic operation on the matrixs
d.dot(e)#dot product

