import unittest
import pytest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
	def setUp(self):
		import Chapter5_Activity_instructions_rev1
		self.exercises = Chapter5_Activity_instructions_rev1

	def test_df(self):
		result = pd.read_pickle('activity_df.pkl')
		pd_testing.assert_frame_equal(self.exercises.df, result)

	def test_clusters(self):
		result = pd.read_pickle('activity_clusters.pkl')
		pd_testing.assert_frame_equal(self.exercises.clusters, result)

	def test_clusters_number(self):
		assert(self.exercises.clusters_number, 5)

if __name__ == '__main__':
	unittest.main()

