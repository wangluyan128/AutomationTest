import unittest
from unittest import mock

class SubClass(object):
    def add(self,a,b):
        '''两个数相加'''
        return a+b

class TestSub(unittest.TestCase):
    '''测试两个数相加'''
    def test_sub(self):
        sub = SubClass()    #初始化被测函数类实例
        sub.add = mock.Mock(return_value=10,side_effect=sub.add)    #传递side_effect关键字参数，会覆盖return_value参数值,使用真实的add方法测试
        result = sub.add(5,11)  #真正的调用被测函数
        self.assertEqual(result,16) #断言实际结果与预期结果

if __name__=='__main__':
    unittest.main()