import unittest
import pytest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
	def setUp(self):
		import Chapter5_Exercise_4_instructions_rev1
		self.exercises = Chapter5_Exercise_4_instructions_rev1

	def test_df(self):
		result = pd.read_pickle('exercice4_df.pkl')
		pd_testing.assert_frame_equal(self.exercises.df, result)

	def test_centroids(self):
		result = pd.read_pickle('exercise4_centroids.pkl')
		pd_testing.assert_frame_equal(self.exercises.centroids, result)

	def test_values(self):
		assert(self.exercises.business_income_min, 0)
		assert(self.exercises.business_income_max, 876324)
		assert(self.exercises.business_expenses_min, 0)
		assert(self.exercises.business_expenses_max, 884659)
		assert(self.exercises.data_x, 210901)
		assert(self.exercises.data_y, 222191)

	def test_list(self):
		self.assertCountEqual(self.exercises.distances, [191720607520, 15734674436, 44775930196, 297515003418])

if __name__ == '__main__':
	unittest.main()

