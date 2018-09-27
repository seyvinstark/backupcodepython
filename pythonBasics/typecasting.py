import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X,dtype='float32')
print(X.dtype)
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)#this is just to fit and transform from 32float to 64float
print(X_new.dtype)