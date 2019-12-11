import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_13_03_Logistic_Regression_Model_with_SMOTE_v1_0
        self.exercises = Exercise_13_03_Logistic_Regression_Model_with_SMOTE_v1_0		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter13/Dataset/bank-full.csv'	
        self.bankData = pd.read_csv(self.filename, sep=";")        
        self.dataShape = self.bankData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.filename, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.bankData.shape, self.dataShape)		


if __name__ == '__main__':
    unittest.main()
