import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.formula.api as smf

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise2_05
		self.exercises = Exercise2_05

		self.rawBostonData = pd.read_csv('https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter02/Dataset/Boston.csv')
		self.rawBostonData = self.rawBostonData.dropna()
		self.rawBostonData = self.rawBostonData.drop_duplicates()
		self.renamedBostonData = self.rawBostonData.rename(columns={'CRIM': 'crimeRatePerCapita',
														  ' ZN ': 'landOver25K_sqft',
														  'INDUS ': 'non-retailLandProptn',
														  'CHAS': 'riverDummy',
														  'NOX': 'nitrixOxide_pp10m',
														  'RM': 'AvgNo.RoomsPerDwelling',
														  'AGE': 'ProptnOwnerOccupied',
														  'DIS': 'weightedDist',
														  'RAD': 'radialHighwaysAccess',
														  'TAX': 'propTaxRate_per10K',
														  'PTRATIO': 'pupilTeacherRatio',
														  'LSTAT': 'pctLowerStatus',
														  'MEDV': 'medianValue_Ks'})
		self.X = self.renamedBostonData.drop('crimeRatePerCapita', axis=1)
		self.y = self.renamedBostonData[['crimeRatePerCapita']]
		self.seed = 10
		self.test_data_size = 0.3
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=self.test_data_size, random_state=self.seed)
		self.train_data = pd.concat([self.X_train, self.y_train], axis=1)
		self.test_data = pd.concat([self.X_test, self.y_test], axis=1)

		self.multiLinearModel = smf.ols(formula= \
									   'crimeRatePerCapita ~ pctLowerStatus + radialHighwaysAccess +\
                                       medianValue_Ks + nitrixOxide_pp10m', data=self.train_data)
		self.multiLinearModResult = self.multiLinearModel.fit()

	def test_rawBostonData(self):
		pd_testing.assert_frame_equal(self.exercises.rawBostonData, self.rawBostonData)

	def test_renamedBostonData(self):
		pd_testing.assert_frame_equal(self.exercises.renamedBostonData, self.renamedBostonData)

	def test_X(self):
		np_testing.assert_array_equal(self.exercises.X , self.X)

	def test_y(self):
		np_testing.assert_array_equal(self.exercises.y , self.y)

	def test_seed(self):
		self.assertEqual(self.exercises.seed, self.seed)

	def test_test_data_size(self):
		self.assertEqual(self.exercises.test_data_size, self.test_data_size)

	def test_X_train(self):
		np_testing.assert_array_equal(self.exercises.X_train , self.X_train)

	def test_X_test(self):
		np_testing.assert_array_equal(self.exercises.X_test, self.X_test)

	def test_y_train(self):
		np_testing.assert_array_equal(self.exercises.y_train , self.y_train)

	def test_y_test(self):
		np_testing.assert_array_equal(self.exercises.y_test , self.y_test)

	def test_train_data(self):
		pd_testing.assert_frame_equal(self.exercises.train_data, self.train_data)

	def test_test_data(self):
		pd_testing.assert_frame_equal(self.exercises.test_data, self.test_data)

	def test_params(self):
		np_testing.assert_array_equal(self.exercises.multiLinearModResult.params, self.multiLinearModResult.params)

if __name__ == '__main__':
	unittest.main()
