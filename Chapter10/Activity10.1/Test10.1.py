import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Activity10_01
		self.exercises = Activity10_01
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter10/dataset/churn.csv'
		self.df = pd.read_csv(self.file_url)
		self.num_df = self.df.select_dtypes(include='number')
		self.num_cols = self.num_df.columns


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_num_df(self):
		pd_testing.assert_frame_equal(self.exercises.num_df, self.num_df)

	def test_num_cols(self):
		np_testing.assert_array_equal(self.exercises.num_cols, self.num_cols)

if __name__ == '__main__':
	unittest.main()
