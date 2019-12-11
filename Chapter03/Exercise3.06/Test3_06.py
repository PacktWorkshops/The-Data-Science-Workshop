import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn import preprocessing
from matplotlib import pyplot

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise3_06
        self.exercises = Exercise3_06
        self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter03/bank-full.csv'
        self.bankData = pd.read_csv(self.file_url, sep=";")
        
        	

    def test_file_url(self):
        self.assertEqual(self.exercises.file_url, self.file_url)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.bankData, self.bankData)
        
    		


if __name__ == '__main__':
	unittest.main()
