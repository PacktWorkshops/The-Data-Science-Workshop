import unittest
import import_ipynb
import pandas as pd
import numpy as np
import pandas.testing as pd_testing
import numpy.testing as np_testing
from sklearn.cluster import KMeans

class Test(unittest.TestCase):
	def setUp(self):
		import Activity12_01
		self.exercises = Activity12_01

		self.disp_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/disp.csv'
		self.trans_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/trans.csv'
		self.account_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/account.csv'
		self.client_url = 'https://raw.githubusercontent.com/PacktWorkshops/The-Data-Science-Workshop/master/Chapter12/Dataset/client.csv'

		self.df_disp = pd.read_csv(self.disp_url, sep=';')
		self.df_trans = pd.read_csv(self.trans_url, sep=';')
		self.df_account = pd.read_csv(self.account_url, sep=';')
		self.df_client = pd.read_csv(self.client_url, sep=';')

		self.df_trans_acc = pd.merge(self.df_trans, self.df_account, how='left', on='account_id')
		self.df_disp_owner = self.df_disp[self.df_disp['type'] == 'OWNER']
		self.df_trans_acc_disp = pd.merge(self.df_trans_acc, self.df_disp_owner, how='left', on='account_id')
		self.df_merged = pd.merge(self.df_trans_acc_disp, self.df_client, how='left', on=['client_id', 'district_id'])
		self.df_merged.rename(columns={'date_x': 'trans_date', 'type_x': 'trans_type', 'date_y': 'account_creation',
								  'type_y': 'client_type'}, inplace=True)
		self.df_merged['trans_date'] = pd.to_datetime(self.df_merged['trans_date'], format="%y%m%d")
		self.df_merged['account_creation'] = pd.to_datetime(self.df_merged['account_creation'], format="%y%m%d")
		self.df_merged['is_female'] = (self.df_merged['birth_number'] % 10000) / 5000 > 1
		self.df_merged.loc[self.df_merged['is_female'] == True, 'birth_number'] -= 5000
		self.df_merged['birth_number'] = self.df_merged['birth_number'].astype(str)
		self.df_merged.loc[self.df_merged['birth_number'] == 'nan', 'birth_number'] = np.nan
		self.df_merged.loc[~self.df_merged['birth_number'].isna(), 'birth_number'] = '19' + self.df_merged.loc[
			~self.df_merged['birth_number'].isna(), 'birth_number']
		self.df_merged['birth_number'] = pd.to_datetime(self.df_merged['birth_number'], format="%Y%m%d", errors='coerce')
		self.df_merged['age_at_creation'] = self.df_merged['account_creation'] - self.df_merged['birth_number']
		self.df_merged['age_at_creation'] = self.df_merged['age_at_creation'] / np.timedelta64(1, 'Y')
		self.df_merged['age_at_creation'] = self.df_merged['age_at_creation'].round()

	def test_disp_url(self):
		self.assertEqual(self.exercises.disp_url, self.disp_url)

	def test_client_url(self):
		self.assertEqual(self.exercises.client_url, self.client_url)

	def test_trans_url(self):
		self.assertEqual(self.exercises.trans_url, self.trans_url)

	def test_account_url(self):
		self.assertEqual(self.exercises.account_url, self.account_url)

	def test_df_trans_acc(self):
		pd_testing.assert_frame_equal(self.exercises.df_trans_acc, self.df_trans_acc)

	def test_df_disp_owner(self):
		pd_testing.assert_frame_equal(self.exercises.df_disp_owner, self.df_disp_owner)

	def test_df_trans_acc_disp(self):
		pd_testing.assert_frame_equal(self.exercises.df_trans_acc_disp, self.df_trans_acc_disp)

	def test_df_merged(self):
		pd_testing.assert_frame_equal(self.exercises.df_merged, self.df_merged)


if __name__ == '__main__':
	unittest.main()
