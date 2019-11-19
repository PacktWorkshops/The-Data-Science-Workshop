import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise12_03
		self.exercises = Exercise12_03
		
		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/Consumer_Complaints.csv'
		self.df = pd.read_csv(self.file_url)
		self.df['Date received'] = pd.to_datetime(self.df['Date received'])
		self.df['Date sent to company'] = pd.to_datetime(self.df['Date sent to company'])
		self.df['YearReceived'] = self.df['Date received'].dt.year
		self.df['MonthReceived'] = self.df['Date received'].dt.month
		self.df['DomReceived'] = self.df['Date received'].dt.day
		self.df['DowReceived'] = self.df['Date received'].dt.dayofweek
		self.df['IsWeekendReceived'] = self.df['DowReceived'] >= 5
		self.df['RoutingDays'] = self.df['Date sent to company'] - self.df['Date received']
		self.df['RoutingDays'] = self.df['RoutingDays'].dt.days

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)


if __name__ == '__main__':
	unittest.main()
