import requests
import unittest
def first_req_fun():
    r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=('user', 'pass'))
    return r.json()
print(first_req_fun())
class TestString(unittest.TestCase):
    
    def test_request_function(self):
        self.assertEqual(first_req_fun(), {'authenticated': True, 'user': 'user'})

if __name__ == '__main__':
    unittest.main()
