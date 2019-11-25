import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise12_01
		self.exercises = Exercise12_01
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/taxstats2015.csv'
		self.df = pd.read_csv(self.file_url)
		self.postcode_url = 'https://github.com/PacktWorkshops/The-Data-Science-Workshop/blob/master/Chapter12/Dataset/taxstats2016individual06taxablestatusstateterritorypostcodetaxableincome%20(2).xlsx?raw=true'
		self.postcode_df = pd.read_excel(self.postcode_url, sheet_name='Individuals Table 6B', header=2)		
		self.merged_df = pd.merge(self.df, self.postcode_df, how='left', on='Postcode')



	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_postcode_url(self):
                self.assertEqual(self.exercises.postcode_url, self.postcode_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_postcode_df(self):
                pd_testing.assert_frame_equal(self.exercises.postcode_df, self.postcode_df)

	def test_merged_df(self):
                pd_testing.assert_frame_equal(self.exercises.merged_df, self.merged_df)

if __name__ == '__main__':
	unittest.main()
