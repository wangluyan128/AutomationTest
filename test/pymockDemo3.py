import sys
import allure
import pytest
from common.logger import Log
from common.read_yaml import ReadYaml

from pymockDemo3_1 import Api_Person_Auth

testdata = ReadYaml("person_auth.yml").get_yaml_data()#读取参数化的数据

@allure.feature('实名认证')
class Test_person_Auth(object):
    log = Log()
    @allure.title('实名认证')
    #使用parametrize参数化请求参数、状态码和返回信息
    @pytest.mark.parametrize('real_name,id_card,mobile,expect', testdata['person_auth'],
                             ids=['正确传入参数',
                                  '全部参数为空',
                                  '姓名为空',
                                  '姓名错误'])
    def test_person_auth(self, mocker,real_name, id_card, mobile, expect):
        self.log.info('%s,%s' % ((sys._getframe().f_code.co_name, '------认证接口-----')))
        shili = Api_Person_Auth()  # 实例化
        #方法一
        shili.api_person_auth = mocker.patch.object(Api_Person_Auth,'api_person_auth',
                                                    return_value={'resultcode': expect['resultcode']})#引用参数化状态码
        #当传入side_effect时，return_value就会失效，当调用真实的认证方法时，就会使用真实的认证方法，从而达到真实的测试如下：
        # shili.api_person_auth = mocker.patch.object(Api_Person_Auth, 'api_person_auth',
        #                                             return_value={'resultcode': code},side_effect=shili.api_person_auth)
        #方法二
        # mocker.patch第一个参数传模拟对象的具体路径api.api_person_auth.api_person_auth.Api_Person_Auth.api_person_auth
        # shili.api_person_auth = mocker.patch('api.api_person_auth.api_person_auth.Api_Person_Auth.'
        #         'api_person_auth', 'api_person_auth',return_value={'resultcode': '100'})
        #加入side_effect参数，代码稍作修改，要调用真实认证方法
        #msg = shili.api_person_auth(real_name,id_card,mobile)
        #不加入side_effect参数，调用自写的认证方法
        msg = shili.api_my_auth(real_name,id_card,mobile)
        #加入side_effect参数，真实情况下返回msg.json()
        #self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg.json())))
        #不加入side_effect参数，模拟情况下直接返回msg
        self.log.info('%s:%s' % ((sys._getframe().f_code.co_name, '获取请求结果：%s' % msg)))
        # 模拟情况下断言
        assert msg == expect['resultmsg']#断言响应信息