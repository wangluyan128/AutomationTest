mitmdump -s E:\work\AutomationTest\test\myproxy.py -p 8800
mitmdump -s E:\work\AutomationTest\test\addons.py -p 8800
谷歌浏览器加入代理
MyChrome.exe --proxy-server=127.0.0.1:8800 --ignore-certificate-errors


usage: mitmproxy [options]
#可选参数：

 -h, --help      show this help message and exit
 --version       show version number and exit
 --options       Show all options and their default values
 --commands      显示所有命令及其签名
 --set option[=value]	设置一个选项。 省略该值时，布尔值设置为true，字符串和整数设置为None（如果允许），并且序列为空。 布尔值可以为true，false或toggle
 -q, --quiet      Quiet.
 -v, --verbose     增加日志详细程度
 --mode MODE, -m MODE 	模式可以是“常规”，“透明”，“ socks5”，“反向：SPEC”或“上游：SPEC”。 对于反向和上游代理模式，SPEC是主机规范，形式为“ http [s]：// host [：port]”
 --no-anticache
 --anticache     去除可能导致服务器返回304-not-modified的请求头
 --no-showhost
 --showhost      使用Host标头构造用于显示的URL
 --rfile PATH, -r PATH		从文件读取流量
 --scripts SCRIPT, -s SCRIPT	执行脚本。 可能会多次通过
 --stickycookie FILTER		设置粘性Cookie过滤条件，根据要求匹配
 --stickyauth FILTER  设置粘性身份验证过滤条件，根据要求匹配
 --save-stream-file PATH, -w PATH	流量到达时保存到文件（附加路径）。      
 --no-anticomp
 --anticomp      尝试令服务器向我们发送未压缩的数据。
 --console-layout {horizontal,single,vertical}		控制台布局
 --no-console-layout-headers
 --console-layout-headers		显示布局组件标题

#代理选项：

 --listen-host HOST  	绑定代理的地址到HOST
 --listen-port PORT, -p PORT	代理服务端口
 --no-server, -n
 --server      启动代理服务器（ 默认启用）
 --ignore-hosts HOST		忽略主机并转发所有流量，而不对其进行处理。 在透明模式下，建议使用IP地址（范围），而不要使用主机名。 在常规模式下，仅SSL流量会被忽略，应使用主机名。 利用正则表达式解释提供的值，并与ip或主机名匹配
 --allow-hosts HOST 与--ignore-hosts相反
 --tcp-hosts HOST   与--ignore-hosts相反。 对于与该模式匹配的所有主机，可以通过通用TCP SSL代理模式。 与--ignore相似，但是SSL连接被拦截。 通信内容以详细模式打印到日志中
 --upstream-auth USER:PASS	通过将HTTP基本身份验证添加到上游代理和反向代理请求。 格式：用户名：密码
 --proxyauth SPEC	需要代理身份验证。 格式：“用户名：密码”，“任何”以接受任何用户/密码组合，“ @ path”以使用Apache htpasswd文件或用于LDAP认证的“ ldap [s]：url_server_ldap：dn_auth：password：dn_subtree”
 --no-rawtcp
 --rawtcp       启用/禁用实验性原始TCP支持。 以非ascii字节开头的TCP连接将被视为与tcp_hosts匹配。 启发式方法很粗糙，请谨慎使用。 默认禁用
 --no-http2
 --http2        启用/禁用HTTP / 2支持。 默认情况下启用HTTP / 2支持

#SSL:

 --certs SPEC     形式为“ [domain =] path”的SSL证书。 该域可以包含通配符，如果未指定，则等于“ *”。 路径中的文件是PEM格式的证书。 如果PEM中包含私钥，则使用私钥，否则使用conf目录中的默认密钥。 PEM文件应包含完整的证书链，并将叶子证书作为第一项
 --no-ssl-insecure
 --ssl-insecure, -k  不要验证上游服务器SSL / TLS证书
 --key-size KEY_SIZE  证书和CA的TLS密钥大小

#客户端重发:

 --client-replay PATH, -C PATH		重发来自已保存文件的客户端请求

#服务端重发:

 --server-replay PATH, -S PATH		从保存的文件重发服务器响应
 --no-server-replay-kill-extra
 --server-replay-kill-extra		在重发期间杀死额外的请求。  
 --no-server-replay-nopop
 --server-replay-nopop		使用后，请勿从服务器重发状态中删除流量。 这样可以多次重发相同的响应。 
 --no-server-replay-refresh
 --server-replay-refresh		通过调整日期，到期和最后修改的header头，以及调整cookie过期来刷新服务器重发响应。   

#更换：

 --replacements PATTERN, -R PATTERN		替换形式：替换形式为``/ pattern / regex / replacement‘‘，其中分隔符可以是任何字符。 可能会多次通过。

#设置Headers:

 --setheaders PATTERN, -H PATTERN		格式为“ /pattern/header/value”的标题设置模式，其中分隔符可以是任何字符。

#Filters:

有关过滤条件表达式语法，请参见mitmproxy中的帮助。

 --intercept FILTER  设置拦截过滤表达式。
 --view-filter FILTER 将视图限制为匹配流。
 
 例：
 mitmdump -w outfile		#保存流量
 mitmdump -nr infile -w outfile "~m post"	#保存过滤后的流量
 mitmdump -nc outfile		#客户端重发
 mitmdump -nc srcfile -w dstfile
 mitmdump -s examples/add_header.py		#运行一个脚本
 mitmdump -ns example/add_header.py -r srcfile -w dstfile		#脚本化数据转换
 
 netstat -ano|findstr 8800
 tasklist|findstr PID