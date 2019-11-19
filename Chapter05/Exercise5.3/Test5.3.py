import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise5_2
		self.exercises = Exercise5_2
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/taxstats2015.csv'		
		self.df = pd.read_csv(self.file_url, usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
		self.X = self.df[['Average total business income', 'Average total business expenses']]
		self.kmeans = KMeans(random_state=42, n_clusters=4)
		self.kmeans.fit(self.X)
		self.df['cluster2'] = self.kmeans.predict(self.X)

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_list(self):
		self.assertCountEqual(self.exercises.y_preds, self.y_preds)


if __name__ == '__main__':
	unittest.main()
