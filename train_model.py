from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier()
clf.fit(X, y)

with open('app/model.pkl', 'wb') as f:
    pickle.dump(clf, f)
