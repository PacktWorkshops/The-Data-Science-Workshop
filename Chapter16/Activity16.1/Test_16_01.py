import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

class Test(unittest.TestCase):
    def setUp(self):
        import Activity_16_01_Complete_ML_workflow_using_Pipeline_with_Heart_Disease_data_set_v1_0
        self.exercises = Activity_16_01_Complete_ML_workflow_using_Pipeline_with_Heart_Disease_data_set_v1_0		
        self.filename = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter16/Dataset/processed.cleveland.data'	
        self.heartData = pd.read_csv(self.filename,sep=",",header = None,na_values = "?")
        self.heartData.columns = ['age','sex', 'cp', 'trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','label']
        self.heartData.loc[self.heartData['label'] > 0 , 'label'] = 1        
        self.dataShape = self.heartData.shape 

    def test_file_url(self):
        self.assertEqual(self.exercises.filename, self.filename)       
        

    def test_shape(self):
        self.assertEqual(self.exercises.heartData.shape, self.dataShape)

    def test_df(self):
        pd_testing.assert_frame_equal(self.exercises.heartData, self.heartData)		


if __name__ == '__main__':
    unittest.main()
