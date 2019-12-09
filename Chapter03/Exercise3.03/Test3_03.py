import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn import preprocessing

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise3_03
        self.exercises = Exercise3_03
        self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter03/bank-full.csv'
        self.bankData = pd.read_csv(self.file_url, sep=";")
        self.bankData['balanceClass'] = 'Quant1'
        self.bankData.loc[(self.bankData['balance'] > 72) & (self.bankData['balance'] < 448), 'balanceClass'] = 'Quant2'
        self.bankData.loc[(self.bankData['balance'] > 448) & (self.bankData['balance'] < 1428), 'balanceClass'] = 'Quant3'
        self.bankData.loc[self.bankData['balance'] > 1428, 'balanceClass'] = 'Quant4'        
        	

    def test_file_url(self):
        self.assertEqual(self.exercises.file_url, self.file_url)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.bankData, self.bankData)

			


if __name__ == '__main__':
	unittest.main()
