#-*- coding:utf8 -*-
import mitmproxy.http
import typing
from mitmproxy import ctx, http
from mitmproxy.contentviews import json


class HTTPRecordModifier:

    def __init__(self):#, flow: http.HTTPFlow
        #self.flow = flow
        self.num =0
    #针对 HTTP 生命周期
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 收到了来自客户端的 HTTP CONNECT 请求。在 flow 上设置非 2xx 响应将返回该响应并断开连接。CONNECT 不是常用的 HTTP 请求方法，目的是与服务器建立代理连接，仅是 client 与 proxy 的之间的交流，所以 CONNECT 请求不会触发 request、response 等其他常规的 HTTP 事件
        """
        #因为谷歌是个不存在的网站，所有就不要浪费时间去尝试连接服务端了，所有当发现客户端试图访问谷歌时，直接断开连接
        #确认客户端是想访问www.goolge.com
        if flow.request.host == "www.goolge.com":
            #返回一个非2XX响应断开连接
            flow.response = http.HTTPResponse.make(404)


    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 来自客户端的 HTTP 请求的头部被成功读取。此时 flow 中的 request 的 body 是空的。
        """
        

    def request_1(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 来自客户端的 HTTP 请求被成功完整读取。
        """
        '''
        #这里编写我们的 mock 逻辑代码
        breakpoint_url = "https://frodo.douban.com/api/v2/user/91807076/following"
        if breakpoint_url in flow.request.pretty_url:
            response_content = json.loads(flow.response.content.decode("utf-8"))
            response_content['total'] = 20
            new_response = HTTPRecordModifier(flow)
            userinfo = {
                       #这里放置上面抓包获取的用户信息格式
            }
            for i in range(response_content['total']):
                #添加 20 个用户信息
                response_content['users'].append(userinfo)
            new_response.set_response_body(json.dumps(response_content))
        '''
    def request(self,flow:mitmproxy.http.HTTPFlow):
        #所有当客户端发起百度搜索时，记录下用户的搜索词，再修改请求，将搜索词改为“360 搜索”
        #忽略非百度搜索地址
        if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
            return
        #确认请求参数中有搜索词
        if "wd" not in flow.request.query.keys():
            ctx.log.warn("cat not get search word from %s" %flow.request.pretty_url)
            return
        #输出原始的搜索词
        ctx.log.info("catch search word:%s" %flow.request.query.get("wd"))
        #替换搜索词为“360搜索
        flow.request.query.set_all("wd",["360搜索"])


    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 来自服务端的 HTTP 响应的头部被成功读取。此时 flow 中的 response 的 body 是空的。
        """

    def response(self,flow: mitmproxy.http.HTTPFlow):
        #所有当客户端访问 360 搜索时，将页面中所有“搜索”字样改为“请使用谷歌”
        #忽略非360搜索地址
        if flow.request.host != "www.so.com":
            return
        #将响应中所有”搜索"替换为“请使用谷歌"
        text = flow.response.get_text()
        text = text.replace("搜索","请使用谷歌")
        flow.response.set_text(text)

    def response_1(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 来自服务端端的 HTTP 响应被成功完整读取。
        """
        self.num = self.num + 1
        flow.response.headers["count"] = str(self.num)
        print(str(flow.response.headers["count"]))
        ctx.log.info("We've seen %d flows"%self.num)


    def error(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 发生了一个 HTTP 错误。比如无效的服务端响应、连接断开等。注意与“有效的 HTTP 错误返回”不是一回事，后者是一个正确的服务端响应，只是 HTTP code 表示错误而已。
        """
    #针对 TCP 生命周期
    def tcp_start(self, flow: mitmproxy.tcp.TCPFlow):
        """
        (Called when) 建立了一个 TCP 连接。
        """
    def tcp_message(self, flow: mitmproxy.tcp.TCPFlow):
        """
        (Called when) TCP 连接收到了一条消息，最近一条消息存于 flow.messages[-1]。消息是可修改的。
        """
    def tcp_error(self, flow: mitmproxy.tcp.TCPFlow):
        """
        (Called when) 发生了 TCP 错误。
        """
    def tcp_end(self, flow: mitmproxy.tcp.TCPFlow):
        """
        (Called when) TCP 连接关闭。
        """
    #针对 Websocket 生命周期
    def websocket_handshake(self, flow: mitmproxy.http.HTTPFlow):
        """
        (Called when) 客户端试图建立一个 websocket 连接。可以通过控制 HTTP 头部中针对 websocket 的条目来改变握手行为。flow 的 request 属性保证是非空的的
        """
    def websocket_start(self, flow: mitmproxy.websocket.WebSocketFlow):
        """
        (Called when) 建立了一个 websocket 连接。
        """
    def websocket_message(self, flow: mitmproxy.websocket.WebSocketFlow):
        """
        (Called when) 收到一条来自客户端或服务端的 websocket 消息。最近一条消息存于 flow.messages[-1]。消息是可修改的。目前有两种消息类型，对应 BINARY 类型的 frame 或 TEXT 类型的 frame。
        """
    def websocket_error(self, flow: mitmproxy.websocket.WebSocketFlow):
        """
        (Called when) 发生了 websocket 错误。
        """
    def websocket_end(self, flow: mitmproxy.websocket.WebSocketFlow):
        """
        (Called when) websocket 连接关闭。
        """
    #针对网络连接生命周期
    def clientconnect(self, layer: mitmproxy.proxy.protocol.Layer):
        """
        (Called when) 客户端连接到了 mitmproxy。注意一条连接可能对应多个 HTTP 请求。
        """
    def clientdisconnect(self, layer: mitmproxy.proxy.protocol.Layer):
        """
        (Called when) 客户端断开了和 mitmproxy 的连接。
        """
    def serverconnect(self, conn: mitmproxy.connections.ServerConnection):
        """
        (Called when) mitmproxy 连接到了服务端。注意一条连接可能对应多个 HTTP 请求。
        """
    def serverdisconnect(self, conn: mitmproxy.connections.ServerConnection):
        """
        (Called when) mitmproxy 断开了和服务端的连接。
        """
    def next_layer(self, layer: mitmproxy.proxy.protocol.Layer):
        """
        (Called when) 网络 layer 发生切换。你可以通过返回一个新的 layer 对象来改变将被使用的 layer
        """
    #通用生命周期
    def configure(self, updated: typing.Set[str]):
        """
        (Called when) 配置发生变化。updated 参数是一个类似集合的对象，包含了所有变化了的选项。在 mitmproxy 启动时，该事件也会触发，且 updated 包含所有选项。
        """
    def done(self):
        """
        (Called when) addon 关闭或被移除，又或者 mitmproxy 本身关闭。由于会先等事件循环终止后再触发该事件，所以这是一个 addon 可以看见的最后一个事件。由于此时 log 也已经关闭，所以此时调用 log 函数没有任何输出。
        """
    def load(self, entry: mitmproxy.addonmanager.Loader):
        """
        (Called when) addon 第一次加载时。entry 参数是一个 Loader 对象，包含有添加选项、命令的方法。这里是 addon 配置它自己的地方。
        """
    def log(self, entry: mitmproxy.log.LogEntry):
        """
        (Called when) 通过 mitmproxy.ctx.log 产生了一条新日志。小心不要在这个事件内打日志，否则会造成死循环。
        """
    def running(self):
        """
        (Called when) mitmproxy 完全启动并开始运行。此时，mitmproxy 已经绑定了端口，所有的 addon 都被加载了。
        """
    def update(self, flows: typing.Sequence[mitmproxy.flow.Flow]):
        """
        (Called when) 一个或多个 flow 对象被修改了，通常是来自一个不同的 addon。
        """

    #设置请求头信息
    def set_request_header(self, headers):
        for header_key, header_value in headers.items():
            self.flow.request.headers[header_key] = header_value

    #设置请求 body 参数
    def set_request_body(self, body):
        self.flow.request.content = bytes(body, "utf-8")

    #设置请求方法
    def set_request_method(self, method):
        self.flow.request.method = method

    #设置请求 query 参数
    def set_request_query(self, key, value):
        self.flow.request.query[key] = value

    #设置响应状态码
    def set_response_status_code(self, code):
        self.flow.response.status_code = code

    #设置响应头信息
    def set_response_header(self, headers):
        for header_key, header_value in headers.items():
            self.flow.response.headers[header_key] = header_value

    #设置响应体内容
    def set_response_body(self, body):
        self.flow.response.content = bytes(body, "utf-8")

    #构造响应报文
    def create_mocked_response(self, code=200, header={}, body=""):
        self.flow.response = http.HTTPResponse.make(code, bytes(body, "utf-8"), header)

#将上述功能组装成名为 Joker 的 addon，并保留之前展示名为 Counter 的 addon，都加载进 mitmproxy

#这个是固定格式
addons=[
    HTTPRecordModifier()
]