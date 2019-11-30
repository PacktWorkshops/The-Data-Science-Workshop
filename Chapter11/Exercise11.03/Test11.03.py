import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise11_03
		self.exercises = Exercise11_03
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter11/dataset/officers.csv'
		self.df = pd.read_csv(self.file_url)
		self.il_mask = self.df['State'].isin(['il', 'Il', 'iL', 'Il'])
		self.df.loc[self.il_mask, 'State'] = 'IL'
		for val in ['II', 'I', '8I', '60']:
			self.df.loc[self.df['State'] == val, 'State'] = 'IL'
		self.df.loc[self.df['State'].str.contains('In', na=False), 'State'] = 'IN'


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_il_mask(self):
		np_testing.assert_array_equal(self.exercises.il_mask, self.il_mask)

if __name__ == '__main__':
	unittest.main()
