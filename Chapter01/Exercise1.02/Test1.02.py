import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing


class Test(unittest.TestCase):
	def setUp(self):
		import Exercise1_02
		self.exercises = Exercise1_02
		
		self.csv_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.csv'
		self.csv_df = pd.read_csv(self.csv_url, skiprows=1)
		self.tsv_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter01/Dataset/overall_topten_2012-2013.tsv'
		self.tsv_df = pd.read_csv(self.tsv_url, skiprows=1, sep='\t')
		self.xlsx_url = 'https://github.com/PacktWorkshops/The-Data-Science-Workshop/blob/master/Chapter01/Dataset/overall_topten_2012-2013.xlsx?raw=true'
		self.xlsx_df = pd.read_excel(self.xlsx_url)
		self.xlsx_df1 = pd.read_excel(self.xlsx_url, skiprows=1, sheet_name=1)

	def test_csv_url(self):
		self.assertEqual(self.exercises.csv_url, self.csv_url)

	def test_csv_df(self):
		np_testing.assert_array_equal(self.exercises.csv_df, self.csv_df)

	def test_tsv_url(self):
		self.assertEqual(self.exercises.tsv_url, self.tsv_url)

	def test_tsv_df(self):
		np_testing.assert_array_equal(self.exercises.tsv_df, self.tsv_df)

	def test_xlsx_url(self):
		self.assertEqual(self.exercises.xlsx_url, self.xlsx_url)

	def test_xlsx_df(self):
		np_testing.assert_array_equal(self.exercises.xlsx_df, self.xlsx_df)

	def test_xlsx_df1(self):
		np_testing.assert_array_equal(self.exercises.xlsx_df1, self.xlsx_df1)


if __name__ == '__main__':
	unittest.main()
