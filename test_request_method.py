import requests
import unittest
r = requests.get('https://httpbin.org/basic-auth/amar/kumar',auth=('amar', 'kumar'))
#r1 = requests.get('https://www.w3schools.com/python/-auth/amar/kumar',auth=('amar', 'kumar'))
print(r.text)

class TestIntStringMethod(unittest.TestCase):
    def test_case1(self):
        self.assertEqual({'authenticated': True, 'user': 'amar'},{'authenticated': True, 'user': 'amar'})
    def test_case2(self):
        self.assertEqual({"authenticated": True,"user": "amar"},{"authenticated": True,"user": "amar"})
if __name__ == '__main__':
    unittest.main()