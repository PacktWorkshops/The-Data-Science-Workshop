import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Activity_13_01_Comparison_of_all_methods_v2_0
        self.exercises = Activity_13_01_Comparison_of_all_methods_v2_0		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter13/Dataset/churn.csv'	
        self.churnData = pd.read_csv(self.filename, sep=",")        
        self.dataShape = self.churnData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.filename, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.churnData.shape, self.dataShape)		


if __name__ == '__main__':
    unittest.main()
