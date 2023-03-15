import requests
import unittest
def request_func():
    resp = requests.post('https://httpbin.org/post', data={'website': 'datagy.io'})
    #return resp.status_code
    return resp.ok

print(request_func())

class testpost(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(request_func(), True)

if __name__ == '__main__':
    unittest.main()
