import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
#from yellowbrick.classifier import ConfusionMatrix


class Test(unittest.TestCase):
	def setUp(self):
		import Exercise4_01
		self.exercises = Exercise4_01

		file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter04/Dataset/openml_phpZNNasq.csv'
		df = pd.read_csv(file_url)
		y = df.pop('type')
		df.drop(columns='animal', inplace=True)

		X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.4, random_state=188)

		rf_model = RandomForestClassifier(random_state=42)
		rf_model.fit(X_train, y_train)
		train_preds = rf_model.predict(X_train)

		train_acc = accuracy_score(y_train, train_preds)
		test_preds = rf_model.predict(X_test)
		test_acc = accuracy_score(y_test, test_preds)

		#cm = ConfusionMatrix(rf_model, classes=y.unique())
		#cm.fit(X_train, y_train)
		#cm.score(X_test, y_test)





	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_postcode_url(self):
                self.assertEqual(self.exercises.postcode_url, self.postcode_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_postcode_df(self):
                pd_testing.assert_frame_equal(self.exercises.postcode_df, self.postcode_df)

	def test_merged_df(self):
                pd_testing.assert_frame_equal(self.exercises.merged_df, self.merged_df)

if __name__ == '__main__':
	unittest.main()
