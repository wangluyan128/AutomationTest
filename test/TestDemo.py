#-*- coding:utf8 -*-
import os
import subprocess
from time import sleep

import multiprocessing as mp

import mitmproxy.http
from mitmproxy import ctx
from mitmproxy.net.tcp import Counter

from common.strTool import StrTool


class TestDemo:
    def __init__(self):
        self.num = 0
    def T_1(self):
        get_process_id_command='netstat -ano|findstr "0.0.0.0:80"'
        #httpserver_process_id = subprocess.Popen(get_process_id_command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #print(httpserver_process_id.stdout.read().decode('gbk'))
        httpserver_process_id = subprocess.check_output(get_process_id_command,shell=True)
        print(httpserver_process_id.decode('utf-8'))
        process_id = httpserver_process_id.decode('utf-8')
        #print(process_id)
        process_id = StrTool.getStringWithLBRB(process_id, 'LISTENING', '\r\n').strip()

       #方法1
        #r1 = os.popen('dir')
        #print(r1.read())
       #方法2
        #r2 = subprocess.Popen('dir',shell=True,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        #print(r2.stdout.read().decode('gbk'))
    def main(self,sec):
        sleep(sec)
        print("Child process start")
        sleep(sec)

    def request(self,flow: mitmproxy.http.HTTPFlow):
        self.num = self.num+1
        ctx.log.info("We've seen %d flows" %self.num)
addons = [
    Counter()
]
if __name__ == '__main__':
    t = TestDemo()
    t.T_1()
    #p = mp.Process(name='child',target=t.main,args=(10,0))
    #p.daemon = True
    #print('Main process',os.getpid())
    #p.start()
    #print('child PID:',p.pid)
    #print('-----------------------')
    #print('End')

