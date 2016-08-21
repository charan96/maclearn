import numpy as np
import pandas, quandl
from sklearn import cross_validation, preprocessing
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/AAPL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df.fillna(value=-99999, inplace=True)

X = np.array(df['HL_PCT'])
X = preprocessing.scale(X)
y = np.array(df['Adj. Open'])

df.dropna(inplace=True)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)
clf = LinearRegression(n_jobs=-1)

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
