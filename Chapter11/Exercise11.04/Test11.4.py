import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise11_04
		self.exercises = Exercise11_04
		
		self.file_url = 'http://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter11/dataset/horse-colic.data'
		self.df = pd.read_csv(self.file_url, header=None, sep='\s+', prefix='X', na_values='?')
		self.x0_mask = self.df['X0'].isna()
		self.x0_median = self.df['X0'].median()
		self.df['X0'].fillna(self.x0_median, inplace=True)
		for col_name in self.df.columns:
			col_median = self.df[col_name].median()
			self.df[col_name].fillna(col_median, inplace=True)


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_x0_mask(self):
		np_testing.assert_array_equal(self.exercises.x0_mask, self.x0_mask)

	def test_x0_median(self):
		np_testing.assert_array_equal(self.exercises.x0_median, self.x0_median)

if __name__ == '__main__':
	unittest.main()
