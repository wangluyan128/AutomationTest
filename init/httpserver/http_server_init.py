# @Author  : yanchunhuo
# @Time    : 2020/1/19 14:33
# github https://github.com/yanchunhuo
from base.read_httpserver_config import Read_Http_Server_Config
from common.strTool import StrTool
import multiprocessing
import platform
import subprocess

def start_http_server(port):
    if 'Windows' == platform.system():
        subprocess.check_output("start cmd.exe @cmd /c python -m http.server %s" % (port), shell=True) ##python3中启动一个简单的http服务器
    else:
        subprocess.check_output('nohup python3 -m http.server %s %s' % (port, '>>logs/httpserver.log 2>&1 &'),shell=True)

def http_server_init():
    httpserver_config = Read_Http_Server_Config().httpserver_config  #获取ip及端口
    port = httpserver_config.httpserver_port
    if "windows"==platform.system().lower():
        get_httpserver_process_id_command='netstat -ano|findstr "0.0.0.0:%s"'%port
        try:
            httpserver_process_id = subprocess.check_output(get_httpserver_process_id_command, shell=True)
            httpserver_process_id = httpserver_process_id.decode('utf-8')
            httpserver_process_id = StrTool.getStringWithLBRB(httpserver_process_id, 'LISTENING', '\r\n').strip()
            kill_httpserver_process_command = 'taskkill /F /pid %s' % httpserver_process_id
            try:
                print('关闭http.server进程,进程id:' + httpserver_process_id + ',该进程监听已监听端口:' + port)
                subprocess.check_call(kill_httpserver_process_command, shell=True)
            except:
                print('关闭http.server进程失败,进程id:' + httpserver_process_id + ',该进程监听已监听端口:' + port)
        except:
            print('http.server未查找到监听端口%s的服务'%port)
    elif "linux"==platform.system().lower():
        # 获得当前httpserver所有进程id
        get_httpserver_process_ids_command = "ps -ef|grep 'http.server %s'|grep -v grep|awk '{print $2}'"%port
        try:
            httpserver_process_ids = subprocess.check_output(get_httpserver_process_ids_command, shell=True)
            httpserver_process_ids = httpserver_process_ids.decode('utf-8')
            get_lambda = lambda info: list(filter(None, info.split('\n'))) if info else []
            httpserver_process_ids = get_lambda(httpserver_process_ids)
            if not len(httpserver_process_ids)>0:
                print('http.server未查找到监听端口%s的服务' % port)
            for httpserver_process_id in httpserver_process_ids:
                try:
                    print('关闭http.server进程,进程id:' + httpserver_process_id + ',该进程监听已监听端口:' + port)
                    subprocess.check_output("kill -9 " + httpserver_process_id, shell=True)
                except:
                    print('关闭http.server进程失败,进程id:' + httpserver_process_id + ',该进程监听已监听端口:' + port)
        except:
            print('http.server未查找到监听端口%s的服务' % port)
    elif "darwin"==platform.system().lower():
        pass
    print('启动http.server,使用端口' + port)
    p = multiprocessing.Process(target=start_http_server,args=(port,))
    p.daemon = True  #主进程运行完不会检查子进程的状态（是否执行完），直接结束进程；
    p.start()
