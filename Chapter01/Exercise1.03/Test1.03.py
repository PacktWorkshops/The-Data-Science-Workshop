import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise1_03
		self.exercises = Exercise1_03

		self.features, self.target = load_breast_cancer(return_X_y=True)
		self.seed = 888
		self.rf_model = RandomForestClassifier(random_state=self.seed)
		self.rf_model.fit(self.features, self.target)
		self.preds = self.rf_model.predict(self.features)

	def test_features(self):
		np_testing.assert_array_equal(self.exercises.features, self.features)

	def test_target(self):
		np_testing.assert_array_equal(self.exercises.target, self.target)

	def test_seed(self):
		self.assertEqual(self.exercises.seed, self.seed)

	def test_preds(self):
		np_testing.assert_array_equal(self.exercises.preds, self.preds)

if __name__ == '__main__':
	unittest.main()
