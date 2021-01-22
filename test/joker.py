#-*- coding:utf8 -*-
import mitmproxy.http
from mitmproxy import ctx, http


class Joker:
    def request(self,flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
            return
        if "wd" not in flow.request.query.keys():
            ctx.log.warn("can not get search word from %s"% flow.request.pretty_url)
            return
        ctx.log.info("catch search word:%s" %flow.request.query.get("wd"))
        flow.request.query.set_all("wd",["360搜索"])
    def response(self,flow: mitmproxy.http.HTTPFlow):
        if flow.request.host!= "www.so.com":
            return
        text = flow.response.get_text()
        text = text.replace("搜索","请使用谷歌")
        flow.response.set_text(text)
    def http_connect(self,flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "www.goolge.com":
            flow.response = http.HTTPResponse.make(404)