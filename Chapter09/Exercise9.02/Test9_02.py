import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


class Test(unittest.TestCase):
	def setUp(self):
		import Exercise9_02
		self.exercises = Exercise9_02

		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter09/Dataset/phpYYZ4Qc.csv'
		self.df = pd.read_csv(self.file_url)
		self.df.head()
		self.y = self.df.pop('rej')

		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df, self.y, test_size=0.3,
																				random_state=1)

		self.rf_model = RandomForestRegressor(random_state=1, n_estimators=50, max_depth=6, min_samples_leaf=60)
		self.rf_model.fit(self.X_train, self.y_train)

		self.preds_train = self.rf_model.predict(self.X_train)
		self.preds_test = self.rf_model.predict(self.X_test)

		self.train_mse = mean_squared_error(self.y_train, self.preds_train)
		self.test_mse = mean_squared_error(self.y_test, self.preds_test)

		self.varimp_df = pd.DataFrame()
		self.varimp_df['feature'] = self.df.columns
		self.varimp_df['importance'] = self.rf_model.feature_importances_


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

	def test_preds_train(self):
		np_testing.assert_array_equal(self.exercises.preds_train , self.preds_train)

	def test_preds_test(self):
		np_testing.assert_array_equal(self.exercises.preds_test, self.preds_test)

	def test_train_mse(self):
		self.assertEqual(self.exercises.train_mse, self.train_mse)

	def test_test_mse(self):
		self.assertEqual(self.exercises.test_mse, self.test_mse)

	def test_varimp_df(self):
		pd_testing.assert_frame_equal(self.exercises.varimp_df, self.varimp_df)


if __name__ == '__main__':
	unittest.main()
