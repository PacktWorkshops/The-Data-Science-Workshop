import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import ensemble
from sklearn import model_selection
from scipy import stats

class Test(unittest.TestCase):
    def setUp(self):
        import Activity8_01
        self.exercises = Activity8_01

        self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter08/agaricus-lepiota.data'

        self.mushrooms = pd.read_csv(self.file_url, header=None)

        self.y_raw = self.mushrooms.iloc[:,0]

        self.X_raw = self.mushrooms.iloc[:,1:]

        self.y = (self.y_raw == 'p') * 1

        self.encoder = preprocessing.OneHotEncoder()

        self.encoder.fit(self.X_raw)

        self.X = self.encoder.transform(self.X_raw).toarray()

        self.rfc = ensemble.RandomForestClassifier(n_estimators=100, random_state=100)

        self.grid = {
            'criterion': ['gini', 'entropy'],
            'max_features': [2, 4, 6, 8, 10, 12, 14]
        }

        self.gscv = model_selection.GridSearchCV(estimator=self.rfc, param_grid=self.grid, cv=5, scoring='accuracy')

        self.gscv.fit(self.X,self.y)

        self.results = pd.DataFrame(self.gscv.cv_results_)

        np.random.seed(100)

        self.max_features = X.shape[1]

        self.param_dist = {
            'criterion': ['gini', 'entropy'],
            'max_features': stats.randint(low=1, high=self.max_features)
        }

        self.rscv = model_selection.RandomizedSearchCV(estimator=self.rfc, param_distributions=self.param_dist, n_iter=50, cv=5, scoring='accuracy', random_state=100)

        self.rscv.fit(self.X,self.y)

        self.results = pd.DataFrame(self.rscv.cv_results_)

    def test_result(self):
        self.assertEqual(
            self.exercises.results["mean_test_score"].max()
            , self.results["mean_test_score"].max()
        )


if __name__ == '__main__':
    unittest.main()
