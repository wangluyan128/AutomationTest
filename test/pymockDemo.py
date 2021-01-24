import pytest


def userinfo():
    return 'ok'

def get_userinfo():
    return userinfo()

def test_for_userinfo(mocker):
    mkd1 = mocker.patch('pymockDemo.userinfo',return_value='not ok')
    assert get_userinfo()=='not ok'

def test_for_user(mocker):
    mkd2 = mocker.patch('pymockDemo.userinfo',return_value='mocked')
    assert mkd2()=='mocked'

if __name__=='__main__':
    command=['-q','pymockDemo.py']
    pytest.main(command)

'''
_init__：

    name: mock 对象的标识

    spec: 设置对象属性

    return_value: 对象调用时的返回值

    side_effect: 覆盖return_value, 当对象被调用时返回

Assert_method:

    assert_called_with: 断言 mock 对象的参数是否正确

    assert_called_once_with: 检查某个对象如果被调用多次抛出异常，只允许一次

    assert_any_call: 检查对象在全局过程中是否调用了该方法

    assert_has_calls: 检查调用的参数和顺序是否正确

Management:

    attach_mock: 添加对象到另一个mock对象中

    configure_mock: 重新设置对象的返回值

    mock_add_spec: 新增对象属性

    reset_mock: 重置对象

Count:

    called: 对象调用的访问器

    call_count: 对象调用次数

    call_args: 对象调用时的参数（最近）

    call_args_list: 获取对用时所有的参数list

    method_calls: 统计对象调用的所有方法，返回list

    mock_calls: 统计工厂调用、方法调用
'''