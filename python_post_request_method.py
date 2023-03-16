import requests
import unittest
def request_func():
    resp = requests.post('https://httpbin.org/post', data={ 'username': 'user@email.com', 'password': 'blahblahsecretpassw0rd' })
    #return resp.status_code
    #return resp.ok #1
    #return resp.text #2
    #return resp.encoding#3
    #return resp.headers['content-type']#4
    if resp.status_code == 200:#5
        return resp.content
    return ""

print(request_func())

class testpost(unittest.TestCase):

    #def test_case1(self):
    #    self.assertEqual(request_func(), True)#1

    #def test_case2(self):#doubt
    #    self.assertEqual(request_func(),'{\n  "args": {}, \n  "data": "", \n  "fi[485 chars]n}\n')

    #def test_case3(self):
    #    self.assertEqual(request_func(),'utf-8')

    #def test_case4(self):
    #    self.assertEqual(request_func(),'application/json')

    def test_case5(self):
        self.assertEqual(request_func(),)


if __name__ == '__main__':
    unittest.main()
