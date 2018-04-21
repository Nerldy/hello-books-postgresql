import unittest
from app import app


class ProjectTests(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		self.app = app.test_client()

		self.assertEquals(app.debug, False)

	# executed after each test
	def tearDown(self):
		pass

	def test_main(self):
		response = self.app.get('/')
		self.assertIn(b'Hello World', response.data)


if __name__ == "__main__":
	unittest.main()
