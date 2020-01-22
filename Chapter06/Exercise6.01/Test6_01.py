import unittest

import import_ipynb
import pandas as pd
from sklearn.model_selection import train_test_split
import pandas.testing as pd_testing
import numpy.testing as np_testing


class MyTestCase(unittest.TestCase):
    def setUp(self):
        import Exercise6_01
        self.exercises = Exercise6_01

        self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter06/Dataset/car.data'
        self.headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'car']
        self.df = pd.read_csv(self.file_url, names=self.headers, index_col=None)
        self.training, self.evaluation = train_test_split(self.df, test_size=0.3, random_state=0)
        self.validation, self.test = train_test_split(self.evaluation, test_size=0.5, random_state=0)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.df, self.df)

    def test_training(self):
        pd_testing.assert_frame_equal(self.exercises.training, self.training)

    def test_validation(self):
        pd_testing.assert_frame_equal(self.exercises.validation, self.validation)

    def test_test(self):
        pd_testing.assert_frame_equal(self.exercises.test, self.test)

if __name__ == '__main__':
    unittest.main()
