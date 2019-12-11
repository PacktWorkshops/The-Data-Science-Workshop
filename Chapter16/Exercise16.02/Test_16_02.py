import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Exercise_16_02_Preprocessing_using_ML_pipeline_v1_0
        self.exercises = Exercise_16_02_Preprocessing_using_ML_pipeline_v1_0		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter15/Dataset/crx.data'	
        self.credData = pd.read_csv(self.filename,sep=",",header = None,na_values = "?")
        self.credData.loc[self.credData[15] == '+' , 15] = 1

        self.credData.loc[self.credData[15] == '-' , 15] = 0
        self.dataShape = self.credData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.filename, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.credData.shape, self.dataShape)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.credData, self.credData)		


if __name__ == '__main__':
    unittest.main()
