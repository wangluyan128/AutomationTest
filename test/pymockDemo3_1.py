import requests

class Api_Person_Auth(object):
    #第三方认证接口
    def api_person_auth(self,real_name,id_card,mobile):
        url = 'http://v.juhe.cn/telecom/query'#第三方认证接口
        body = {
            "real_name":real_name,
            "id_card":id_card,
            "mobile":mobile
        }
        r = requests.post(url, json=body)#请求第三方认证接口
        #print(r.text)
        return r #返回信息

        #我们的认证接口
    def api_my_auth(self,real_name,id_card,mobile):
        #调用第三方认证接口
        response = self.api_person_auth(real_name,id_card,mobile)
        try:
            if response['resultcode'] == '100':
                return '认证成功'
            elif response['resultcode'] == '101':
                return '认证失败'
            elif response['resultcode'] == "102":
                return '有必填参数为空'
            else:
                return '未定义错误'
        except Exception:
            return '系统异常'


if __name__ == '__main__':
    Api_Person_Auth().api_person_auth()