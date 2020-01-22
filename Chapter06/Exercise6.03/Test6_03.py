import unittest

import import_ipynb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas.testing as pd_testing
import numpy.testing as np_testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        import Exercise6_03
        self.exercises = Exercise6_03

        self.headers = ['CIC0', 'SM1', 'GATS1i', 'NdsCH', 'Ndssc', 'MLOGP', 'response']
        self.df = pd.read_csv(
            'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/qsar_fish_toxicity.csv',
            names=self.headers, sep=';')
        self.features = self.df.drop('response', axis=1).values
        self.labels = self.df[['response']].values
        self.X_train, self.X_eval, self.y_train, self.y_eval = train_test_split(self.features, self.labels, test_size=0.2, random_state=0)
        self.X_val, self.X_test, self.y_val, self.y_test = train_test_split(self.X_eval, self.y_eval, random_state=0)
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_val)
        self.mae = mean_absolute_error(self.y_val, self.y_pred)
        self.r2 = self.model.score(self.X_val, self.y_val)

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

    def test_y_pred(self):
        np_testing.assert_array_equal(self.exercises.y_pred, self.y_pred)

    def test_r2(self):
        self.assertEqual(self.exercises.r2, self.r2)

    def test_mae(self):
        self.assertEqual(self.exercises.mae, self.mae)


if __name__ == '__main__':
    unittest.main()
