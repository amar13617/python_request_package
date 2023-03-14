import requests
import unittest
def request_func(user):
    r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=('user', 'pass'))
    return user

print(request_func(20))

class teststring(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(request_func(20), 20)
    

if __name__ == '__main__':
    unittest.main()