import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Activity11_1
		self.exercises = Activity11_1
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter11/dataset/Speed_Dating_Data.csv'
		self.df = pd.read_csv(self.file_url)

		self.scale_1_10 = ['imprace', 'imprelig', 'sports', 'tvsports', 'exercise', 'dining',
				  'museums', 'art', 'hiking', 'gaming', 'clubbing', 'reading', 'tv',
				  'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga',
				  'exphappy', 'satis_2']

		self.unexpected_mask = self.check_range(self.df['imprace'], 1, 10)
		self.replace_value(self.df, 'gaming', 14, 10)
		self.replace_value(self.df, 'reading', 13, 10)
		for col_name in ['attr3_3', 'sinc3_3', 'intel3_3', 'fun3_3', 'amb3_3']:
			self.replace_value(self.df, col_name, 12, 10)
		self.num_cols = ['round', 'order', 'int_corr', 'age', 'mn_sat', 'income', 'expnum']
		self.cat_cols = self.df.columns.difference(self.num_cols)
		for col_name in self.cat_cols:
			self.df[col_name] = self.df[col_name].astype('category')
		self.int_corr_mean = self.df['int_corr'].mean()
		self.df['int_corr'].fillna(self.int_corr_mean, inplace=True)
		self.missing_num_cols = ['age', 'mn_sat', 'income', 'expnum']
		for col_name in self.missing_num_cols:
			col_median = self.df[col_name].median()
			self.df[col_name].fillna(col_median, inplace=True)



	def check_range(self, column, min_value, max_value):
		return (column < min_value) | (column > max_value)

	def replace_value(self, df, col_name, incorrect_value, new_value):
		df.loc[df[col_name] == incorrect_value, col_name] = new_value

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_scale_1_10(self):
		np_testing.assert_array_equal(self.exercises.scale_1_10, self.scale_1_10)

	def test_unexpected_mask(self):
		np_testing.assert_array_equal(self.exercises.unexpected_mask, self.unexpected_mask)

	def test_num_cols(self):
		np_testing.assert_array_equal(self.exercises.num_cols, self.num_cols)

	def test_cat_cols(self):
		np_testing.assert_array_equal(self.exercises.cat_cols, self.cat_cols)

	def test_int_corr_mean(self):
		np_testing.assert_array_equal(self.exercises.int_corr_mean, self.int_corr_mean)

	def test_missing_num_cols(self):
		np_testing.assert_array_equal(self.exercises.missing_num_cols, self.missing_num_cols)

if __name__ == '__main__':
	unittest.main()
