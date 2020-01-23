import unittest
import import_ipynb
import pandas as pd
import numpy as np
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class Test(unittest.TestCase):
	def setUp(self):
		import Activity5_1
		self.exercises = Activity5_1
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/german.data-numeric'
		self.df = pd.read_csv(self.file_url, header=None, sep='\s\s+', prefix='X')
		self.X = self.df[['X3', 'X9']]
		self.standard_scaler = StandardScaler()
		self.X_scaled = self.standard_scaler.fit_transform(self.X)
		self.clusters = pd.DataFrame()
		self.inertia = []
		self.clusters['cluster_range'] = range(1, 15)
		for k in self.clusters['cluster_range']:
			self.kmeans = KMeans(n_clusters=k, random_state=8).fit(self.X_scaled)
			self.inertia.append(self.kmeans.inertia_)
		self.clusters['inertia'] = self.inertia
		self.clusters_number = 5
		self.kmeans = KMeans(random_state=1, n_clusters=self.clusters_number, init='k-means++', n_init=50, max_iter=1000)
		self.kmeans.fit(self.X_scaled)
		self.df['cluster'] = self.kmeans.predict(self.X_scaled)

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_X_scaled(self):
		np_testing.assert_array_equal(self.exercises.X_scaled, self.X_scaled)

	def test_clusters(self):
		pd_testing.assert_frame_equal(self.exercises.clusters, self.clusters)

	def test_inertia(self):
		np_testing.assert_array_equal(self.exercises.inertia, self.inertia)

	def test_clusters_number(self):
		self.assertEqual(self.exercises.clusters_number, self.clusters_number)

if __name__ == '__main__':
	unittest.main()
