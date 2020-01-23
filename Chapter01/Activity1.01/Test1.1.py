import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class Test(unittest.TestCase):
	def setUp(self):
		import Activity1_1
		self.exercises = Activity1_1

		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/dataset_44_spambase.csv'
		self.df = pd.read_csv(self.file_url)
		self.target = self.df.pop('class')
		self.seed = 168
		self.rf_model = RandomForestClassifier(random_state=self.seed)
		self.rf_model.fit(self.df, self.target)
		self.preds = self.rf_model.predict(self.df)
		self.acc_score = accuracy_score(self.target, self.preds)

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_target(self):
		np_testing.assert_array_equal(self.exercises.target, self.target)

	def test_seed(self):
		self.assertEqual(self.exercises.seed, self.seed)

	def test_preds(self):
		np_testing.assert_array_equal(self.exercises.preds, self.preds)

	def test_acc_score(self):
		self.assertEqual(self.exercises.acc_score, self.acc_score)


if __name__ == '__main__':
	unittest.main()
