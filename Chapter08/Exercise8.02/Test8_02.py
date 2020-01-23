import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn import datasets, svm, model_selection

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_8_2
        self.exercises = Exercise_8_2

        self.digits = datasets.load_digits()

        self.y = self.digits.target

        self.X = self.digits.data

        self.clr = svm.SVC(gamma='scale')

        self.grid = [
            {'kernel': ['linear']},
            {'kernel': ['poly'], 'degree': [2, 3, 4]}
        ]

        self.cv_spec = model_selection.GridSearchCV(estimator=self.clr, param_grid=self.grid, scoring='accuracy', cv=10)

        self.cv_spec.fit(self.X, self.y)

    def test_result(self):
        self.assertEqual(
            self.exercises.cv_spec.cv_results_["mean_test_score"].max()
            , self.cv_spec.cv_results_["mean_test_score"].max()
        )


if __name__ == '__main__':
    unittest.main()
