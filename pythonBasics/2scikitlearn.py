from sklearn import svm
from sklearn import datasets
#this is our estimator
clf = svm.SVC()
#this is  the dataset that we're using iris dataset
iris = datasets.load_iris()
#here the training and target value is split into x and y variables
x, y = iris.data, iris.target
#we fit the model to our variables
clf.fit(x, y)
#import this so we can save our trained dataset
import pickle
#we save with pickle
s = pickle.dumps(clf)
#we load our data
clf2 = pickle.loads(s)
#predict from 1st to 2nd
clf2.predict(x[0:1])
print(y[0])

#we can do the same thing with joblib
from sklearn.externals import joblib
joblib.dump(clf,'firstfile.pkl')
clf3 = joblib.load('firstfile.pkl')
print(clf3)