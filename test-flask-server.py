# this script tests if a flask server is running locally
import requests
import unittest

class TestFlaskServer(unittest.TestCase):
    def setUp(self):
        self.base_url="http://0.0.0.0:5432"
        self.endpoint="/is_poisoned"

    def testServerRunning(self):
        try:
            response = requests.get(f"{self.base_url}{self.endpoint}")
            self.assertEqual(response.status_code, 200)
        except:
            self.fail("server is not running at 0.0.0.0:5432")

if __name__ == '__main__':
    unittest.main()