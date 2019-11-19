import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise12_04
		self.exercises = Exercise12_04
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/ames_iowa_housing.csv'
		self.df = pd.read_csv(self.file_url)
		self.df_agg = self.df.groupby(['Neighborhood', 'YrSold']).agg({'SalePrice': 'max'}).reset_index()
		self.df_agg.columns = ['Neighborhood', 'YrSold', 'SalePriceMax']
		self.df_new = pd.merge(self.df, self.df_agg, how='left', on=['Neighborhood', 'YrSold'])
		self.df_new['SalePriceRatio'] = self.df_new['SalePrice'] / self.df_new['SalePriceMax']
		self.df_agg2 = self.df.groupby(['Neighborhood', 'YrSold']).agg({'LotArea': 'max'}).reset_index()
		self.df_agg2.columns = ['Neighborhood', 'YrSold', 'LotAreaMax']
		self.df_final = pd.merge(self.df_new, self.df_agg2, how='left', on=['Neighborhood', 'YrSold'])
		self.df_final['LotAreaRatio'] = self.df_final['LotArea'] / self.df_final['LotAreaMax']


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_df_agg(self):
                pd_testing.assert_frame_equal(self.exercises.df_agg, self.df_agg)

	def test_df_new(self):
                pd_testing.assert_frame_equal(self.exercises.df_new, self.df_new)

	def test_df_agg2(self):
                pd_testing.assert_frame_equal(self.exercises.df_agg2, self.df_agg2)

if __name__ == '__main__':
	unittest.main()
