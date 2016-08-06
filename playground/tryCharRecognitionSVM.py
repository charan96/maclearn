import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC()
X = digits.data[:-10]
y = digits.target[:-10]

clf.fit(X, y)

print(clf.predict((digits.data[-5]).reshape(1,-1)))

plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()