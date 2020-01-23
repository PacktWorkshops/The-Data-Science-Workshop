import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class Test(unittest.TestCase):
	def setUp(self):
		import Activity4_1
		self.exercises = Activity4_1

		self.file_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter04/Dataset/test/phpB0xrNj.csv'
		self.df = pd.read_csv(self.file_url)
		self.y = self.df.pop('class')

		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.df, self.y, test_size=0.3, random_state=888)

		self.rf_1 = self.train_rf(self.X_train, self.y_train)
		self.trn_preds, self.tst_preds = self.get_preds(self.rf_1, self.X_train, self.X_test)
		self.trn_acc, self.tst_preds = self.print_accuracy(self.y_train, self.y_test, self.trn_preds, self.tst_preds)

		self.rf_model_1, self.trn_preds_1, self.tst_preds_1, self.trn_acc_1, self.tst_acc_1 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=20,max_depth=None, min_samples_leaf=1,max_features='sqrt')
		self.rf_model_2, self.trn_preds_2, self.tst_preds_2, self.trn_acc_2, self.tst_acc_2 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=None, min_samples_leaf=1,max_features='sqrt')
		self.rf_model_3, self.trn_preds_3, self.tst_preds_3, self.trn_acc_3, self.tst_acc_3 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=5, min_samples_leaf=1,max_features='sqrt')
		self.rf_model_4, self.trn_preds_4, self.tst_preds_4, self.trn_acc_4, self.tst_acc_4 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=10, min_samples_leaf=1,max_features='sqrt')
		self.rf_model_5, self.trn_preds_5, self.tst_preds_5, self.trn_acc_5, self.tst_acc_5 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=10, min_samples_leaf=10,max_features='sqrt')
		self.rf_model_6, self.trn_preds_6, self.tst_preds_6, self.trn_acc_6, self.tst_acc_6 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=10, min_samples_leaf=50,max_features='sqrt')
		self.rf_model_7, self.trn_preds_7, self.tst_preds_7, self.trn_acc_7, self.tst_acc_7 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=10, min_samples_leaf=50,max_features=0.5)
		self.rf_model_8, self.trn_preds_8, self.tst_preds_8, self.trn_acc_8, self.tst_acc_8 = self.fit_predict_rf(self.X_train, self.X_test, self.y_train, self.y_test,random_state=888, n_estimators=50,max_depth=10, min_samples_leaf=50,max_features=0.3)


	def train_rf(self, X_train, y_train, random_state=888, n_estimators=10, max_depth=None, min_samples_leaf=1,
				 max_features='sqrt'):
		rf_model = RandomForestClassifier(random_state=random_state, n_estimators=n_estimators, max_depth=max_depth,
										  min_samples_leaf=min_samples_leaf, max_features=max_features)
		rf_model.fit(X_train, y_train)
		return rf_model

	def get_preds(self, rf_model, X_train, X_test):
		train_preds = rf_model.predict(X_train)
		test_preds = rf_model.predict(X_test)
		return train_preds, test_preds

	def print_accuracy(self, y_train, y_test, train_preds, test_preds):
		train_acc = accuracy_score(y_train, train_preds)
		test_acc = accuracy_score(y_test, test_preds)
		return train_acc, test_acc

	def fit_predict_rf(self, X_train, X_test, y_train, y_test, random_state=888, n_estimators=10, max_depth=None,
					   min_samples_leaf=1, max_features='sqrt'):
		rf_model = self.train_rf(X_train, y_train, random_state=random_state, n_estimators=n_estimators, max_depth=max_depth,
							min_samples_leaf=min_samples_leaf, max_features=max_features)
		train_preds, test_preds = self.get_preds(rf_model, X_train, X_test)
		train_acc, test_acc = self.print_accuracy(y_train, y_test, train_preds, test_preds)
		return rf_model, train_preds, test_preds, train_acc, test_acc

	def test_file_url(self):
		self.assertEqual(self.exercises.file_url, self.file_url)

	def test_df(self):
		pd_testing.assert_frame_equal(self.exercises.df, self.df)

	def test_y(self):
		np_testing.assert_array_equal(self.exercises.y , self.y)

	def test_X_train(self):
		np_testing.assert_array_equal(self.exercises.X_train , self.X_train)

	def test_X_test(self):
		np_testing.assert_array_equal(self.exercises.X_test, self.X_test)

	def test_y_train(self):
		np_testing.assert_array_equal(self.exercises.y_train , self.y_train)

	def test_y_test(self):
		np_testing.assert_array_equal(self.exercises.y_test , self.y_test)

	def test_rf_model(self):
		np_testing.assert_array_equal(self.exercises.trn_preds, self.trn_preds)
		np_testing.assert_array_equal(self.exercises.tst_preds, self.tst_preds)
		self.assertEqual(self.exercises.trn_acc, self.trn_acc)
		self.assertEqual(self.exercises.tst_preds, self.tst_preds)

	def test_rf_model_1(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_1, self.trn_preds_1)
		np_testing.assert_array_equal(self.exercises.tst_preds_1, self.tst_preds_1)
		self.assertEqual(self.exercises.trn_acc_1, self.trn_acc_1)
		self.assertEqual(self.exercises.tst_acc_1, self.tst_acc_1)

	def test_rf_model_2(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_2, self.trn_preds_2)
		np_testing.assert_array_equal(self.exercises.tst_preds_2, self.tst_preds_2)
		self.assertEqual(self.exercises.trn_acc_2, self.trn_acc_2)
		self.assertEqual(self.exercises.tst_acc_2, self.tst_acc_2)

	def test_rf_model_3(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_3, self.trn_preds_3)
		np_testing.assert_array_equal(self.exercises.tst_preds_3, self.tst_preds_3)
		self.assertEqual(self.exercises.trn_acc_3, self.trn_acc_3)
		self.assertEqual(self.exercises.tst_acc_3, self.tst_acc_3)

	def test_rf_model_4(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_4, self.trn_preds_4)
		np_testing.assert_array_equal(self.exercises.tst_preds_4, self.tst_preds_4)
		self.assertEqual(self.exercises.trn_acc_4, self.trn_acc_4)
		self.assertEqual(self.exercises.tst_acc_4, self.tst_acc_4)

	def test_rf_model_5(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_5, self.trn_preds_5)
		np_testing.assert_array_equal(self.exercises.tst_preds_5, self.tst_preds_5)
		self.assertEqual(self.exercises.trn_acc_5, self.trn_acc_5)
		self.assertEqual(self.exercises.tst_acc_5, self.tst_acc_5)

	def test_rf_model_6(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_6, self.trn_preds_6)
		np_testing.assert_array_equal(self.exercises.tst_preds_6, self.tst_preds_6)
		self.assertEqual(self.exercises.trn_acc_6, self.trn_acc_6)
		self.assertEqual(self.exercises.tst_acc_6, self.tst_acc_6)

	def test_rf_model_7(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_7, self.trn_preds_7)
		np_testing.assert_array_equal(self.exercises.tst_preds_7, self.tst_preds_7)
		self.assertEqual(self.exercises.trn_acc_7, self.trn_acc_7)
		self.assertEqual(self.exercises.tst_acc_7, self.tst_acc_7)

	def test_rf_model_8(self):
		np_testing.assert_array_equal(self.exercises.trn_preds_8, self.trn_preds_8)
		np_testing.assert_array_equal(self.exercises.tst_preds_8, self.tst_preds_8)
		self.assertEqual(self.exercises.trn_acc_8, self.trn_acc_8)
		self.assertEqual(self.exercises.tst_acc_8, self.tst_acc_8)

if __name__ == '__main__':
	unittest.main()
