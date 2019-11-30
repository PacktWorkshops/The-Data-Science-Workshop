import unittest
import import_ipynb
import pandas as pd
import pandas.testing as pd_testing
import numpy.testing as np_testing

import socket
import threading
import requests
import json
from flask import Flask, jsonify, request


class Test(unittest.TestCase):
	def setUp(self):
		import Exercise10_02
		self.exercises = Exercise10_02
		
		self.ip_address = socket.gethostbyname(socket.gethostname())
		app = Flask(__name__)

		@app.route("/")
		def welcome():
			return "Welcome to my API!"

		@app.route('/empty', methods=['POST'])
		def check_empty():
			data = request.get_json()
			return jsonify(not data)

		flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 80})
		flask_thread.start()

		self.r = requests.get(f"http://{self.ip_address}")

		self.empty_json = json.dumps([])
		self.headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
		self.r_empty = requests.post(f"http://{self.ip_address}/empty", data=self.empty_json, headers=self.headers)

		self.not_empty_json = json.dumps(['Data Science', 'is', 'so', 'cool', '!'])
		self.r_not_empty = requests.post(f"http://{self.ip_address}/empty", data=self.not_empty_json, headers=self.headers)


	def test_ip_address(self):
		self.assertEqual(self.exercises.ip_address, self.ip_address)

	def test_empty_json(self):
		self.assertEqual(self.exercises.empty_json, self.empty_json)

	def test_headers(self):
		self.assertEqual(self.exercises.headers, self.headers)

	def test_r(self):
		self.assertEqual(self.exercises.r.text, self.r.text)

	def test_r_empty(self):
		self.assertEqual(self.exercises.r_empty.text, self.r_empty.text)

	def test_r_not_empty(self):
		self.assertEqual(self.exercises.r_not_empty.text, self.r_not_empty.text)


if __name__ == '__main__':
	unittest.main()
