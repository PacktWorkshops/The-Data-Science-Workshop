import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class Test(unittest.TestCase):
	def setUp(self):
		import Exercise4_01
		self.exercises = Exercise4_01

		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter04/Dataset/openml_phpZNNasq.csv'
		self.df = pd.read_csv(self.file_url)
		self.y = self.df.pop('type')
		self.df.drop(columns='animal', inplace=True)

		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df, self.y, test_size=0.4, random_state=188)

		self.rf_model = RandomForestClassifier(random_state=42)
		self.rf_model.fit(self.X_train, self.y_train)
		self.train_preds = self.rf_model.predict(self.X_train)
		self.test_preds = self.rf_model.predict(self.X_test)
		self.train_acc = accuracy_score(self.y_train, self.train_preds)
		self.test_acc = accuracy_score(self.y_test, self.test_preds)

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_y(self):
		np_testing.assert_array_equal(self.exercises.y , self.y)

	def test_X_train(self):
		np_testing.assert_array_equal(self.exercises.X_train , self.X_train)

	def test_X_test(self):
		np_testing.assert_array_equal(self.exercises.X_test, self.X_test)

	def test_y_train(self):
		np_testing.assert_array_equal(self.exercises.y_train , self.y_train)

	def test_y_test(self):
		np_testing.assert_array_equal(self.exercises.y_test , self.y_test)

	def test_train_preds(self):
		np_testing.assert_array_equal(self.exercises.train_preds , self.train_preds)

	def test_test_preds(self):
		np_testing.assert_array_equal(self.exercises.test_preds, self.test_preds)

	def test_train_acc(self):
		self.assertEqual(self.exercises.train_acc, self.train_acc)

	def test_test_acc(self):
		self.assertEqual(self.exercises.test_acc, self.test_acc)

if __name__ == '__main__':
	unittest.main()
