import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Chapter_14_Activity_14_02_Comparison_of_different_methods_v1
        self.exercises = Chapter_14_Activity_14_02_Comparison_of_different_methods_v1		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter14/Dataset/ad.data'	
        self.adData = pd.read_csv(self.filename,sep=",",header = None,error_bad_lines=False)        
        self.dataShape = self.adData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.filename, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.adData.shape, self.dataShape)		


if __name__ == '__main__':
    unittest.main()
