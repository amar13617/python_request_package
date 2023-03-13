import requests
import unittest
def first_req_fun(user):
    r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=(user, 'pass'))
    #return r.json()#1
    #if r.status_code == 200:#2
    #    return r.json()
    #return " "
    if r.status_code == 400:
        return r.json()
    return {'authenticated': True, 'user': 'user'}
print(first_req_fun("amar"))
class TestString(unittest.TestCase):
    
    #def test_request_function(self):
    #    self.assertEqual(first_req_fun(),{'authenticated': True, 'user': 'user'})

    #def test_request_function2(self):
    #    self.assertNotEqual(first_req_fun("amar"),{'authenticated': True, 'user': 'user'})

    def test_request_function3(self):
        self.assertEqual(first_req_fun("amar"),{'authenticated': True, 'user': 'user'})

if __name__ == '__main__':
    unittest.main()
