import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn.cluster import KMeans
import random

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise5_4
		self.exercises = Exercise5_4
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter05/DataSet/taxstats2015.csv'		
		self.df = pd.read_csv(self.file_url, usecols=['Postcode', 'Average total business income', 'Average total business expenses'])
		self.X = self.df[['Average total business income', 'Average total business expenses']]
		self.business_income_min = self.df['Average total business income'].min()
		self.business_income_max = self.df['Average total business income'].max()
		self.business_expenses_min = self.df['Average total business expenses'].min()
		self.business_expenses_max = self.df['Average total business expenses'].max()
		random.seed(42)
		self.centroids = pd.DataFrame()

		self.centroids['Average total business income'] = random.sample(range(self.business_income_min, self.business_income_max), 4)
		self.centroids['Average total business expenses'] = random.sample(range(self.business_expenses_min, self.business_expenses_max), 4)
		self.centroids['cluster'] = self.centroids.index

		def squared_euclidean(data_x, data_y, centroid_x, centroid_y, ):
			return (data_x - centroid_x)**2 + (data_y - centroid_y)**2

		self.data_x = self.df.at[0, 'Average total business income']
		self.data_y = self.df.at[0, 'Average total business expenses']
		self.distances = [squared_euclidean(self.data_x, self.data_y, self.centroids.at[i, 'Average total business income'], self.centroids.at[i, 'Average total business expenses']) for i in range(4)]
		self.cluster_index = self.distances.index(min(self.distances))
		self.df.at[0, 'cluster'] = self.cluster_index
		self.distances = [squared_euclidean(self.df.at[1, 'Average total business income'], self.df.at[1, 'Average total business expenses'], self.centroids.at[i, 'Average total business income'], self.centroids.at[i, 'Average total business expenses']) for i in range(4)]
		self.df.at[1, 'cluster'] = self.distances.index(min(self.distances))

		self.distances = [squared_euclidean(self.df.at[2, 'Average total business income'], self.df.at[2, 'Average total business expenses'], self.centroids.at[i, 'Average total business income'], self.centroids.at[i, 'Average total business expenses']) for i in range(4)]
		self.df.at[2, 'cluster'] = self.distances.index(min(self.distances))

		self.distances = [squared_euclidean(self.df.at[3, 'Average total business income'], self.df.at[3, 'Average total business expenses'], self.centroids.at[i, 'Average total business income'], self.centroids.at[i, 'Average total business expenses']) for i in range(4)]
		self.df.at[3, 'cluster'] = self.distances.index(min(self.distances))

		self.distances = [squared_euclidean(self.df.at[4, 'Average total business income'], self.df.at[4, 'Average total business expenses'], self.centroids.at[i, 'Average total business income'], self.centroids.at[i, 'Average total business expenses']) for i in range(4)]
		self.df.at[4, 'cluster'] = self.distances.index(min(self.distances))

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_distances(self):
		self.assertCountEqual(self.exercises.distances, self.distances)


if __name__ == '__main__':
	unittest.main()
