import requests
import unittest
def first_req_fun():
    r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=('user', 'pass'))
    #return r.json()#1
    #if r.status_code == 200:#2
    #    return r.json()
    #return " "
    #if r.status_code == 400:#3
    #    return r.json()
    #return {'authenticated': True, 'user': 'user'}
    #if r.status_code == 200:#4 all blank
    #    return r.json()
    #return " "
    #if r.status_code == 400:#5
    #    return r.json()
    #return " "
    #return r.text # 6
    #if r.status_code == 200:#7
    #    return r.text
    #else:
    #    return None
    if r.status_code == 400:
        return r.text
    else:
        return None


print(first_req_fun())
class TestString(unittest.TestCase):
    
    #def test_request_function(self):
    #    self.assertEqual(first_req_fun(),{'authenticated': True, 'user': 'user'})

    #def test_request_function2(self):
    #    self.assertNotEqual(first_req_fun("amar"),{'authenticated': True, 'user': 'user'})

    #def test_request_function3(self):
    #    self.assertEqual(first_req_fun("amar"),{'authenticated': True, 'user': 'user'})

    #def test_request_function4(self):
    #    self.assertEqual(first_req_fun(),{'authenticated': True, 'user': 'user'})

    #def test_request_function5(self):
    #    self.assertEqual(first_req_fun(),' ')
    
    #def test_request_function6(self):
    #    self.assertEqual(first_req_fun(),'{\n  "authenticated": true, \n  "user": "user"\n}\n')

    #def test_request_function7(self):#7
    #    self.assertEqual(first_req_fun(),'{\n  "authenticated": true, \n  "user": "user"\n}\n')
    #def test_request_function8(self):#8
    #    self.assertEqual(first_req_fun(),None)

if __name__ == '__main__':
    unittest.main()
