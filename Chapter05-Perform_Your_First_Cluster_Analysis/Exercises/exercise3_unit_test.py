import unittest
import pytest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
	def setUp(self):
		import Chapter5_Exercise_3_instructions_rev1
		self.exercises = Chapter5_Exercise_3_instructions_rev1

	def test_dataframe(self):
		result = pd.read_pickle('exercise3_df.pkl')
		pd_testing.assert_frame_equal(self.exercises.df, result)

if __name__ == '__main__':
	unittest.main()

