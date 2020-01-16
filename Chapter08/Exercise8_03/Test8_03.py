import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn import datasets
from sklearn import ensemble
from scipy import stats
from sklearn import model_selection
import pandas as pd
import numpy as np

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_8_3
        self.exercises = Exercise_8_3

        self.digits = datasets.load_digits()

        self.y = self.digits.target

        self.X = self.digits.data

        self.rfc = ensemble.RandomForestClassifier(n_estimators=100, random_state=100)

        self.n_features = X.shape[1]

        np.random.seed(100)

        self.param_dist = {
            'criterion': ['gini', 'entropy'],
            'max_features': stats.randint(low=1, high=self.n_features)
        }

        self.rscv = model_selection.RandomizedSearchCV(estimator=self.rfc, param_distributions=self.param_dist, n_iter=50, cv=5, scoring='accuracy', random_state=100)

        self.rscv.fit(self.X,self.y)

        self.results = pd.DataFrame(self.rscv.cv_results_)

        self.distinct_results = self.results.loc[:,['params','mean_test_score']]

        self.distinct_results.loc[:,'params'] = self.distinct_results.loc[:,'params'].astype('str')

        self.distinct_results.drop_duplicates(inplace=True)

    def test_result(self):
        self.assertEqual(
            self.exercises.distinct_results["mean_test_score"].max()
            , self.distinct_results["mean_test_score"].max()
        )


if __name__ == '__main__':
    unittest.main()
