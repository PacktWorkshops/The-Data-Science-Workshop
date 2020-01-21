import unittest

import import_ipynb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas.testing as pd_testing
import numpy.testing as np_testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        import Exercise6_05
        self.exercises = Exercise6_05

        self.headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'car']
        self.df = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/car.data', names=self.headers, index_col=None)
        self._df = pd.get_dummies(self.df, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
        self.features = self._df.drop(['car'], axis=1).values
        self.labels = self._df[['car']].values
        self.X_train, self.X_eval, self.y_train, self.y_eval = train_test_split(self.features, self.labels, test_size=0.3, random_state=0)
        self.X_val, self.X_test, self.y_val, self.y_test = train_test_split(self.X_eval, self.y_eval, test_size=0.5, random_state=0)
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_val)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises._df, self._df)

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

    def test_y_pred(self):
        np_testing.assert_array_equal(self.exercises.y_pred, self.y_pred)


if __name__ == '__main__':
    unittest.main()
