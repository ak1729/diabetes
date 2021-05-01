from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

features = iris.data
labels = iris.target

clf = KNeighborsClassifier()
clf.fit(features, labels)

pre = clf.predict([[7.7, 3.8, 6.7, 2.2]])
if(pre == 0):
    print('This is Setosa')
elif(pre == 1):
    print('This is Versicolour')
else:
    print('This is Virginica')