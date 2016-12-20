import sqlite3
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect('database.db')

data = (pd.read_sql('select * from stats', conn))
data.dropna(inplace=True)

X = np.array(data.drop(['Player','Pos','FDP'], axis=1))
X = preprocessing.scale(X)
y = np.array(data['FDP'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)
