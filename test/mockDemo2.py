import requests

class PayApi(object):
    @staticmethod
    def auth(card,amout):
        '''
        第三方支付接口
        :param card:卡号
        :param amout: 支付金额
        :return:
        '''
        pay_url ="http://www.zhifubao.com"  #第三方支付接口地址
        data = {"card":card,"amount":amout}
        response=requests.post(pay_url,data=data)   #请求第三方支付接口
        return response #返回状态码
    def pay(self,user_id,card,amound):
        '''
        我们自己的支付接口
        :param user_id:用户id
        :param card: 卡号
        :param amound: 支付金额
        :return:
        '''
        #调用第三方支付接口
        response = self.auth(card,amound)
        try:
            if response['status_code']=='200':
                print('用户{}支付金额{}成功'.format(user_id,amound))
                return '支付成功'
            elif response['status_code']=='500':
                print('用户{}支付失败，金额不变'.format(user_id))
                return '支付失败'
            else:
                return '未知错误'
        except Exception:
            return "Error,服务器异常！"
if __name__=='__main__':
    pass