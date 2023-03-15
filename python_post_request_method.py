import requests
import unittest
def request_func():
    resp = requests.post('https://httpbin.org/post', data={'data1': 'value1', 'data2': 'value2'})
    #return resp.status_code
    #return resp.ok #1
    #return resp.text #2
    return resp.encoding

print(request_func())

class testpost(unittest.TestCase):

    #def test_case1(self):
    #    self.assertEqual(request_func(), True)#1

    #def test_case2(self):#doubt
    #    self.assertEqual(request_func(),'{\n  "args": {}, \n  "data": "", \n  "fi[485 chars]n}\n')

    #def test_case2(self):
    #    self.assertEqual(request_func(),'utf-8')


if __name__ == '__main__':
    unittest.main()
