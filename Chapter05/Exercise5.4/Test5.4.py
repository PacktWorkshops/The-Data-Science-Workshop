import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn.cluster import KMeans
import random

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise5_04
		self.exercises = Exercise5_04
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/taxstats2015.csv'		
		self.df = pd.read_csv(self.file_url, usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
		self.X = self.df[['Average total business income', 'Average total business expenses']]
		self.kmeans = KMeans(random_state=1, n_clusters=4, init='random', n_init=1)
		self.kmeans.fit(self.X)
		self.df['cluster3'] = self.kmeans.predict(self.X)
		self.kmeans = KMeans(random_state=1, n_clusters=4, init='random', n_init=10)
		self.kmeans.fit(self.X)
		self.df['cluster4'] = self.kmeans.predict(self.X)
		self.kmeans = KMeans(random_state=1, n_clusters=4, init='random', n_init=100)
		self.kmeans.fit(self.X)
		self.df['cluster5'] = self.kmeans.predict(self.X)


	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)


if __name__ == '__main__':
	unittest.main()
