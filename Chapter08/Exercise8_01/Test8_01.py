import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn import neighbors, datasets, model_selection

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_8_1
        self.exercises = Exercise_8_1

        self.cancer = datasets.load_breast_cancer()

        self.y = self.cancer.target

        self.X = self.cancer.data

        self.knn = neighbors.KNeighborsClassifier(n_neighbors=5, weights='distance')

        self.cv = model_selection.cross_val_score(self.knn, self.X, self.y, cv=10, scoring='precision')

    def test_result(self):
        self.assertEqual(self.exercises.cv.mean(), self.cv.mean())


if __name__ == '__main__':
    unittest.main()
