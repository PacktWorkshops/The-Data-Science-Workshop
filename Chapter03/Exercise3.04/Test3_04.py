import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
from sklearn import preprocessing

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise3_04
        self.exercises = Exercise3_04
        self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter03/bank-full.csv'
        self.bankData = pd.read_csv(self.file_url, sep=";")
        self.x = self.bankData[['balance']].values.astype(float)
        self.minmaxScaler = preprocessing.MinMaxScaler()
        self.bankData['balanceTran'] = self.minmaxScaler.fit_transform(self.x)
        self.bankData['balanceTran'] = self.bankData['balanceTran'] + 0.00001
        self.bankData['loanTran'] = 1
        self.bankData.loc[self.bankData['loan'] == 'no', 'loanTran'] = 5
        self.bankData['houseTran'] = 5
        self.bankData.loc[self.bankData['housing'] == 'no', 'houseTran'] = 1
        self.bankData['assetIndex'] = self.bankData['balanceTran'] * self.bankData['loanTran'] * self.bankData['houseTran']
        self.bankData['assetClass'] = 'Quant1'
        self.bankData.loc[(self.bankData['assetIndex'] > 0.38) & (self.bankData['assetIndex'] < 0.57), 'assetClass'] = 'Quant2'
        self.bankData.loc[(self.bankData['assetIndex'] > 0.57) & (self.bankData['assetIndex'] < 1.9), 'assetClass'] = 'Quant3'
        self.bankData.loc[self.bankData['assetIndex'] > 1.9, 'assetClass'] = 'Quant4'        
        	

    def test_file_url(self):
        self.assertEqual(self.exercises.file_url, self.file_url)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.bankData, self.bankData)

			


if __name__ == '__main__':
	unittest.main()
