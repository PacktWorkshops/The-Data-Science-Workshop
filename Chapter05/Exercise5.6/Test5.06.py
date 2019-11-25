import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy as np
import numpy.testing as np_testing
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise5_5
		self.exercises = Exercise5_5
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/taxstats2015.csv'		
		self.df = pd.read_csv(self.file_url, usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
		self.X = self.df[['Average total business income', 'Average total business expenses']]
		self.min_max_scaler = MinMaxScaler()
		self.min_max_scaler.fit(self.X)
		self.X_min_max = self.min_max_scaler.transform(self.X)
		self.kmeans = KMeans(random_state=1, n_clusters=4, init='k-means++', n_init=5)
		self.kmeans.fit(self.X_min_max)
		self.df['cluster8'] = self.kmeans.predict(self.X_min_max)
		self.standard_scaler = StandardScaler()
		self.X_scaled = self.standard_scaler.fit_transform(self.X)
		self.kmeans = KMeans(random_state=1, n_clusters=4, init='k-means++', n_init=5)
		self.kmeans.fit(self.X_scaled)
		self.df['cluster9'] = self.kmeans.predict(self.X_scaled)

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_X_min_max(self):
		np_testing.assert_array_equal(self.exercises.X_min_max, self.X_min_max)

	def test_X_scaled(self):
                np_testing.assert_array_equal(self.exercises.X_scaled, self.X_scaled)

if __name__ == '__main__':
	unittest.main()
