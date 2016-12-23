import pandas as pd
import numpy as np
from sklearn import preprocessing
from fantasize import players as pl


def teams(clf, players):

    df = pl.play_dataframe(players)
    if df.shape[0] == 0:
        return None
    df.dropna(inplace=True)
    X = np.array(df.drop(['Player', 'Salary', 'Pos'], axis=1))
    # X = preprocessing.scale(X)
    df['PFDP'] = clf.predict(X)

    print df.head()
