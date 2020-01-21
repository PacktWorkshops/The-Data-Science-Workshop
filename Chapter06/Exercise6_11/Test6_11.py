import unittest

import import_ipynb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import pandas.testing as pd_testing
import numpy.testing as np_testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        import Exercise6_11
        self.exercises = Exercise6_11

        self.headers = ['Age', 'Delivery_Nbr', 'Delivery_Time', 'Blood_Pressure', 'Heart_Problem', 'Caesarian']
        self.df = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/caesarian.csv.arff', names=self.headers, index_col=None, skiprows=15)
        self.features = self.df.drop(['Caesarian'], axis=1).values
        self.labels = self.df[['Caesarian']].values
        self.X_train, self.X_eval, self.y_train, self.y_eval = train_test_split(self.features, self.labels, test_size=0.2, random_state=0)
        self.X_val, self.X_test, self.y_val, self.y_test = train_test_split(self.X_eval, self.y_eval, test_size=0.5, random_state=0)
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        self.y_proba = self.model.predict_proba(self.X_val)
        self._false_positive, self._true_positive, self._thresholds = roc_curve(self.y_val, self.y_proba[:, 0])

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.df, self.df)

    def test_features(self):
        np_testing.assert_array_equal(self.exercises.features, self.features)

    def test_labels(self):
        np_testing.assert_array_equal(self.exercises.labels, self.labels)

    def test_X_train(self):
        np_testing.assert_array_equal(self.exercises.X_train, self.X_train)

    def test_X_val(self):
        np_testing.assert_array_equal(self.exercises.X_val, self.X_val)

    def test_X_test(self):
        np_testing.assert_array_equal(self.exercises.X_test, self.X_test)

    def test_y_train(self):
        np_testing.assert_array_equal(self.exercises.y_train, self.y_train)

    def test_y_val(self):
        np_testing.assert_array_equal(self.exercises.y_val, self.y_val)

    def test_y_test(self):
        np_testing.assert_array_equal(self.exercises.y_test, self.y_test)

    def test_y_proba(self):
        np_testing.assert_array_equal(self.exercises.y_proba, self.y_proba)

    def test_false_positive(self):
        np_testing.assert_array_equal(self.exercises._false_positive, self._false_positive)

    def test_true_positive(self):
        np_testing.assert_array_equal(self.exercises._true_positive, self._true_positive)

    def test_thresholds(self):
        np_testing.assert_array_equal(self.exercises._thresholds, self._thresholds)


if __name__ == '__main__':
    unittest.main()
