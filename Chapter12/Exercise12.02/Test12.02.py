import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise12_02
		self.exercises = Exercise12_02
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/ames_iowa_housing.csv'
		self.df = pd.read_csv(self.file_url)
		self.year_built = self.df['YearBuilt'].unique()
		self.decade_list = [year - (year % 10) for year in self.year_built]
		self.decade_built = sorted(set(self.decade_list))
		self.df['DecadeBuilt'] = pd.cut(self.df['YearBuilt'], bins=self.decade_built)


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_year_built(self):
		np_testing.assert_array_equal(self.exercises.year_built, self.year_built)

	def test_decade_list(self):
		self.assertEqual(self.exercises.decade_list, self.decade_list)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)


if __name__ == '__main__':
	unittest.main()
