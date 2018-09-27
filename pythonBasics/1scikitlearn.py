"""
        first machine learning try
    this programm is meant to classify images of digits into their corresponding numbers
    it uses scikit learn and its digit dataset i used SVC(support vector classifier)
    as an estimator and fitted to all my training set except the last data
    and i used the last data as my testing data


"""
#it's a program that classify images of digits into their corresponding numbers
from sklearn import datasets

#step 1 load ur dataset

digits = datasets.load_digits()
#that is the answers we are supposed to get or at least what our answers are supposed to look like
print("digit targets :",digits.target)

#step 2 we shape the array in this case its already done so we dont have to


#step 3 learning and predicting

from sklearn import svm
clf = svm.SVC(gamma=0.01)#here we set the parameter manually but we dont have to
#   SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0,
#   decision_function_shape=None, degree=3, gamma=0.001, kernel='rbf',
#   max_iter=-1, probability=False, random_state=None, shrinking=True,
#   tol=0.001, verbose=False)

clf.fit(digits.data[:-1], digits.target[:-1])#here we trained using our dataset except the last data hence the [:-1]syntax
#   now we ll try to predict a new value what is the digit of our last image given our traiing model

print(clf.predict(digits.data[-1:]))
