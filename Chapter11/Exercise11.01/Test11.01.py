import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise11_01
		self.exercises = Exercise11_01
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter11/dataset/breast-cancer-wisconsin.data'
		self.df = pd.read_csv(self.file_url, header=None)
		self.col_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
					 'Marginal Adhesion', 'Single Epithelial Cell Size',
					 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
		self.df.columns = self.col_names
		self.df_unique = self.df.drop_duplicates(keep='first')


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_df_unique(self):
		pd_testing.assert_frame_equal(self.exercises.df_unique, self.df_unique)

if __name__ == '__main__':
	unittest.main()
