import unittest
from unittest import mock


class SubClass(object):
    def add(self,a,b):
        '''两个数相加'''
        pass

class TestSub(unittest.TestCase):
    '''测试两个数相加用例'''
    def test_sub(self):
        sub = SubClass() #初始化被测函数类实例
        sub.add = mock.Mock(return_value=10) #mock add方法返回10
        result = sub.add(5,5) #调用被测函数
        self.assertEqual(result,10) #断言实际结果和预期结果

if __name__=='__main__':
    unittest.main()