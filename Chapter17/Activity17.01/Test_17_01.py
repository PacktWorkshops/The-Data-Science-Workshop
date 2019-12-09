import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Activity_17_01_Classification_model_after_automated_feature_generation
        self.exercises = Activity_17_01_Classification_model_after_automated_feature_generation		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter17/Datasets/adult.csv'	
        self.adultData = pd.read_csv(self.filename,sep=",",na_values = " ?")
        self.adultData = self.adultData.dropna(axis = 0, how = 'any')

        self.Y = self.adultData.pop('label')
        self.adultData['parentID'] = self.adultData.index.values
        self.adultData.loc[self.adultData.workclass == ' Federal-gov','workId']= '1'
        self.adultData.loc[self.adultData.occupation == ' Adm-clerical','occuId']= '1'
        self.dataShape = self.adultData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.file_url, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.adultData.shape, self.dataShape)

    #def test_df(self):
        #pd_testing.assert_frame_equal(self.exercises.adultData, self.adultData)		


if __name__ == '__main__':
    unittest.main()
