import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

class Test(unittest.TestCase):
	def setUp(self):
		import Exercise1_01
		self.exercises = Exercise1_01
		
		self.algorithm = ['Linear Regression', 'Logistic Regression', 'RandomForest', 'a3c']
		self.learning = ['Supervised', 'Supervised', 'Supervised', 'Reinforcement']
		self.algorithm_type = ['Regression', 'Classification', 'Regression or Classification', 'Game AI']
		self.algorithm.append('k-means')
		self.learning.append('Unsupervised')
		self.algorithm_type.append('Clustering')
		self.machine_learning = {}
		self.machine_learning['algorithm'] = self.algorithm
		self.machine_learning['learning'] = self.learning
		self.machine_learning['algorithm_type'] = self.algorithm_type
		self.machine_learning['algorithm'].remove('a3c')
		self.machine_learning['learning'].remove('Reinforcement')
		self.machine_learning['algorithm_type'].remove('Game AI')

	def test_algorithm(self):
		np_testing.assert_array_equal(self.exercises.algorithm, self.algorithm)

	def test_learning(self):
		np_testing.assert_array_equal(self.exercises.learning, self.learning)

	def test_algorithm_type(self):
		np_testing.assert_array_equal(self.exercises.algorithm_type, self.algorithm_type)

	def test_machine_learning(self):
		self.assertEqual(self.exercises.machine_learning, self.machine_learning)

if __name__ == '__main__':
	unittest.main()
