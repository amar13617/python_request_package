import requests
import unittest
def request_func(user):
    r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=(user, 'pass'))
    #return data #1
    return user

print(request_func("amar"))

class TestIntStringMethod(unittest.TestCase):

    #def test_case_1(self):#1
    #    self.assertEqual(request_func(20), 20)

    #def test_case_2(self):#2 here user is what.
    #    self.assertEqual(request_func(20), 20)

    #def test_case_3(self):#3
    #    self.assertEqual(request_func("amar"), "amar")






    

if __name__ == '__main__':
    unittest.main()