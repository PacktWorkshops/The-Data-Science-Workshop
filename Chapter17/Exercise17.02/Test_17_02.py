import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_17_02_Feature_Engineering_with_Feature_tools
        self.exercises = Exercise_17_02_Feature_Engineering_with_Feature_tools		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter17/Datasets/bank-full.csv'	
        self.bankData = pd.read_csv(self.filename,sep=";")
        self.Y = self.bankData.pop('y')
        self.bankData['custID'] = self.bankData.index.values
        self.bankData['custID'] = 'cust' + self.bankData['custID'].astype(str)
        self.bankData['AssetId'] = 0
        self.bankData.loc[self.bankData.housing == 'yes','AssetId']= 1        
        self.bankData['LoanId'] = 0 
        self.bankData.loc[self.bankData.loan == 'yes','LoanId']= 1
        self.bankData['FinbehId'] = 0 
        self.bankData.loc[self.bankData.default == 'yes','FinbehId']= 1        
        self.dataShape = self.bankData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.file_url, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.bankData.shape, self.dataShape)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.bankData, self.bankData,check_dtype=False)		


if __name__ == '__main__':
    unittest.main()
