我们从最常用的 Python 包入手，去解答这个问题——全球各地的程序员都是怎样使用 Python？。最初，我列出过去一年在 PyPI 上下载次数最多的 Python 包。接下来，深入研究其用途、它们之间的关系和它们备受欢迎的原因。

1.Urllib3
下载次数：8.93 亿



Urllib3是一个 Python 的 HTTP 客户端，它拥有 Python 标准库中缺少的许多功能：



线程安全

连接池

客户端 SSL/TLS 验证

使用分段编码上传文件

用来重试请求和处理 HTTP 重定向的助手

支持 gzip 和 deflate 编码

HTTP 和 SOCKS 的代理支持



不要被名字所误导，Urllib3并不是urllib2的后继者，而后者是 Python 核心的一部分。如果你想使用尽可能多的 Python 核心功能，或者你能安装什么东西是受限，那么请查看urlllib.request。



对最终用户来说，我强烈建议使用 requests 包（参阅列表中的 #6）。这个包之所以会排名第一，是因为有差不多 1200 个包依赖urllib3，其中许多包在这个列表中的排名也很高。

2.Six
下载次数：7.32 亿



six 是一个是 Python 2 和 3 的兼容性库。这个项目旨在支持可同时运行在 Python 2 和 3 上的代码库。



它提供了许多可简化 Python 2 和 3 之间语法差异的函数。一个容易理解的例子是six.print_()。在 Python 3 中，打印是通过print()函数完成的，而在 Python 2 中，print后面没有括号。因此，有了six.print_()后，你就可以使用一个语句来同时支持两种语言。



事实：



它的名字叫six，是因为二乘以三等于六。

同类库还可以看看future包。

如果你要将代码转换为 Python3（并停止支持 2），请查看2to3。



虽然我理解它为什么这么受欢迎，但我希望人们能完全放弃 Python 2，因为要知道从 2020 年 1 月 1 日起 Python 2 的官方支持就已停止。



相关链接：PyPI页面和文档。

3.botocore、boto3、s3transfer、awscli
这里，我把相关的几个项目列在一起：



botocore（#3，6.6 亿次下载）

s3transfer（#7，5.84 亿次下载）

awscli（#17，3.94 亿次下载）

boto3（#22，3.29 亿次下载）



Botocore是 AWS 的底层接口。Botocore是 Boto3 库（#22）的基础，后者让你可以用 Amazon S3 和 Amazon EC2 一类的服务。



Botocore 还是AWS-CLI的基础，后者为 AWS 提供统一的命令行界面。



S3transfer（#7）是用于管理 Amazon S3 传输的 Python 库。它正在积极开发中，其介绍页面不推荐人们现在使用，或者至少等版本固定下来再用，因为它的 API 可能发生变化，在次要版本之间都可能更改。Boto3、AWS-CLI和其他许多项目都依赖s3transfer。



令人惊讶的是，这些针对 AWS 库的排名竟如此之高——这充分说明了 AWS 有多厉害。



相关链接：



botocore——PyPI页面和文档，

Boto3——PyPI页面和文档

awscl——PyPI页面

4.Pip
下载次数：6.27 亿






我想，你们大多数人都知道并且很喜欢 pip，它是 Python 的包安装器。你可以用 pip 轻松地从Python包索引和其他索引（例如本地镜像或带有私有软件的自定义索引）来安装软件包。



有关 pip 的一些有趣事实：



pip是“Pip Installs Packages”的首字母递归缩写。

pip很容易使用。要安装一个包只需pip install <package name>即可，而删除包只需pip uninstall <package name>即可。

最大优点之一是它可以获取包列表，通常以requirements.txt文件的形式获取。该文件能选择包含所需版本的详细规范。大多数 Python 项目都包含这样的文件。

如果结合使用pip与virtualenv（列表中的 #57），就可以创建可预测的隔离环境，同时不会干扰底层系统，反之亦然。要了解更多细节，请查看这篇文章：Stop Installing Python Packages Globally — Use Virtual Environments

5.Python-dateutil
下载次数：6.17 亿



python-dateutil模块提供了对标准datetime模块的强大扩展。我的经验是，常规的Python datetime缺少哪些功能，python-dateutil就能补足那一块。



你可以用这个库做很多很棒的事情。其中，我发现的一个特别有用的功能就是：模糊解析日志文件中的日期，例如：



from dateutil.parser import parse

logline = 'INFO 2020-01-01T00:00:01 Happy new year, human.'
timestamp = parse(log_line, fuzzy=True)
print(timestamp)
# 2020-01-01 00:00:01

6.Requests
下载次数：6.11 亿



Requests建立在我们的 #1 库——urllib3基础上。它让 Web 请求变得非常简单。相比urllib3来说，很多人更喜欢这个包。而且使用它的最终用户可能也比urllib3更多。后者更偏底层，并且考虑到它对内部的控制级别，它一般是作为其他项目的依赖项。



下面这个例子说明 requests 用起来有多简单：



import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
# 200
r.headers['content-type']
# 'application/json; charset=utf8'
r.encoding
# 'utf-8'
r.text
# u'{"type":"User"...'
r.json()
# {u'disk_usage': 368627, u'private_gists': 484, ...}



相关链接：



PyPI页面

文档

7.S3transfer
这里把 #3、#7、#17 和 #22 放在一起介绍，因为它们的关系非常密切。

8.Certifi
下载次数：5.52 亿



近年来，几乎所有网站都转向 SSL，你可以通过地址栏中的小锁符号来识别它。加了小锁意味着与该站点的通信是安全和加密的，能防止窃听行为。






小锁告诉我们此网站已使用 SSL 保护



加密过程是基于 SSL 证书的，并且这些 SSL 证书由受信任的公司或非营利组织（如 LetsEncrypt）创建。这些组织使用他们的（中间）证书对这些证书进行数字签名。



你的浏览器使用这些证书的公开可用部分来验证这些签名，这样就能确保你正查看的是真实内容，并且没有人能窥探到通信数据。Python 软件也能做同样事情。这就是 certifi 的用途所在。它与 Chrome、Firefox 和 Edge 等网络浏览器随附的根证书集合没有太大区别。



Certifi是根证书的一个精选集合，有了它，你的 Python 代码就能验证 SSL 证书的可信度。



如此处所示，许多项目信任并依赖 certifi。这也是该项目排名如此之高的原因所在。



相关链接：certifi PyPI页面、文档、certifi.io

9.Idna
下载次数：5.27 亿



根据其 PyPI 页面，idna提供了“对RFC5891中指定的应用程序中国际化域名（IDNA）协议的支持。”



可能你像我一样也是一头雾水，不知道Idna是什么，有什么用！据悉，应用程序中的国际化域名（IDNA）是一种用来处理包含非 ASCII 字符的域名机制。但是，原始域名系统已经提供对基于非 ASCII 字符的域名支持。所以，哪有问题？






问题在于应用程序（例如电子邮件客户端和 Web 浏览器）不支持非 ASCII 字符。更具体地说，电子邮件和 HTTP 用的协议不支持这些字符。对许多国家来说，这没什么问题，但是像中国、俄罗斯、德国、希腊和印度尼西亚等国家，这是个问题。最后，来自这些地方的一群聪明人想到 IDNA。



IDNA的核心是两个函数：ToASCII和ToUnicode。ToASCII会将国际 Unicode 域转换为 ASCII 字符串。ToUnicode则逆转该过程。在IDNA包中，这些函数称为idna.encode()和idna.decode()，如以下代码片段所示：



import idna
idna.encode('ドメイン.テスト')
# b'xn--eckwd4c7c.xn--zckzah'
print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
# ドメイン.テスト



如果你是受虐狂，则可以阅读RFC-3490了解这一编码的详细信息。



相关链接：



Idna PyPI 页面，GitHub页面

10.PyYAML
下载次数：5.25 亿



YAML是一种数据序列化格式。它的设计宗旨是让人类和计算机都能很容易地阅读代码——人类很容易读写它的内容，计算机也可以解析它。






PyYAML是 Python 的YAML解析器和发射器，这意味着它可以读写YAML。它会把任何 Python 对象写成YAML：列表、字典，甚至是类实例都包括在内。



Python 提供了自己的配置解析器，但是与 Python 的ConfigParser的基本.ini文件结构相比，YAML 提供更多功能。



例如，YAML可以存储任何数据类型：布尔值、列表、浮点数等等。ConfigParser会将所有内容存储为内部字符串。如果要使用ConfigParser加载整数，则你需要指定自己要显式获取一个int：



config.getint(“section”, “my_int”)



pyyaml能自动识别类型，所以这将使用PyYAML返回你的int：



config[“section”][“my_int”]



YAML还允许任意的 deep trees，虽然不是每个项目都需要这种东西，但是需要时，它就可以派上用场。你可能有自己的偏好，但是许多项目都使用YAML作为配置文件，所以这个项目是很受欢迎的。



相关链接：PyYAML PyPI 页面、文档

11.Pyasn1
下载次数：5.12 亿



像上面的IDNA一样，这个项目也非常有用：



ASN.1 类型和 DER/BER/CER 编码（X.208）的纯 Python 实现



所幸这个已有数十年历史的标准有很多信息可用。ASN.1是 Abstract Syntax Notation One 的缩写，它就像是数据序列化的教父。它来自电信行业。也许你知道协议缓冲区或 Apache Thrift？这就是它们的 1984 年版本。



ASN.1 描述了系统之间的跨平台接口，以及可以通过该接口发送的数据结构。



还记得 Certifi（请参阅 #8）吗？ASN.1 用于定义 HTTPS 协议和其他许多加密系统中使用的证书格式。它也用在了 SNMP、LDAP、Kerberos、UMTS、LTE 和 VOIP 协议中。



这是一个非常复杂的规范，并且某些实现已被证明满是漏洞。你可能还会喜欢关于 ASN.1 的这个有趣的Reddit帖子。



一个建议，除非你真的需要，否则还是敬而远之吧。但由于它用在很多地方，因此许多包都依赖这个包。

12.Docutils
下载次数：5.08 亿



Docutils是一个模块化系统，用来将纯文本文档处理为很多有用的格式，例如 HTML、XML 和 LaTeX 等。Docutils能读取reStructuredText格式的纯文本文档，这种格式是类似于 MarkDown 的易读标记语法。



你可能听说过，甚至读过PEP文档。那么什么是 PEP 文档？最早的PEP文档，PEP-1 为我们提供很好的解释：



PEP 的意思是 Python 增强提案。一个 PEP 就是一个设计文档，用来向 Python 社区提供信息，或描述 Python 或其过程或环境的新功能。PEP 应该提供该功能的简明技术规范以及功能的原理。



PEP 文档使用固定的reStructuredText模板编写，并使用docutils转换为格式正确的文档。



Docutils 也是Sphinx的核心。Sphinx用于创建文档项目。如果Docutils是一台机器，则Sphinx就是工厂。它最初是为了构建 Python 文档而创建的，但其他许多项目也使用它为代码提供文档。你可能已经读过readthedocs.org上的文档，那里的大多数文档都是由Sphinx和docutils创建的。

13.Chardet
下载次数：5.01 亿



你可以用chardet模块来检测文件或数据流的字符集。比如说，需要分析大量随机文本时，这会很有用。但你也可以在处理远程下载的数据，但不知道用的是什么字符集时使用它。



安装chardet后，你还有一个名为chardetect的命令行工具，用法如下：



chardetect somefile.txt
somefile.txt: ascii with confidence 1.0



你还能通过编程方式使用这个库，具体参阅文档。Chardet是requests等许多包的需求。我觉得没有多少人会单独使用chardet，所以它这么流行肯定是因为这些依赖项。

14.RSA
下载次数：4.92 亿



rsa包是一个纯 Python 的 RSA 实现。它支持：



加密和解密

签名和验证签名，

根据 PKCS#1 1.5 版生成密钥。



它既可以用作 Python 库，也能在命令行中使用。



一些事实：



RSA 是 RonRivest、Adi Shamir 和 Leonard Adleman 三人姓的首字母。他们在 1977 年发明该算法。

RSA 是最早的公钥密码系统之一，被广泛用于安全数据传输。在这样的密码系统中，有两个密钥：公共部分和私有部分。你用公钥加密数据，只能用私钥解密数据。

RSA 是一种 slow algorithm。它很少用于直接加密用户数据。通常，RSA 用于安全传递对称密钥加密的共享密钥，这样加密和解密大量数据时会快得多。



以下代码段展示了如何在一个非常简单的用例中使用 RSA：



import rsa

# Bob creates a key pair:
(bob_pub, bob_priv) = rsa.newkeys(512)

# Alice ecnrypts a message for Bob
# with his public key
crypto = rsa.encrypt('hello Bob!', bob_pub)

# When Bob gets the message, he
# decrypts it with his private key:
message = rsa.decrypt(crypto, bob_priv)
print(message.decode('utf8'))
# hello Bob!



假设 Bob 保留自己的私钥 private，那么 Alice 可以确定他是唯一可以阅读该消息的人。



但是，Bob 不能确定是 Alice 发送了该消息，因为任何人都可以获取并使用他的公钥。为证明是她，Alice 可以用她的私钥在邮件上签名。Bob 可以用她的公钥验证此签名，确保消息的确是她发送的。



诸如google-auth（#37）、oauthlib（#54）、awscli（#17）之类的包都依赖rsa包。很少有人会将这个工具独立使用，因为有更快、更原生的替代方法。

15.Jmespath
下载次数：4.73 亿



在 Python 中用 JSON 非常容易，因为它在 Python 字典上的映射非常好。对我来说，这是它最好的特性之一。






实话实说——尽管我已经用 JSON 做过很多工作，但我从未听说过这个包。我只是用 json.loads()并从字典中手动获取数据，也许再搞个循环什么的。



JMESPath，发音为“James path”，使 Python 中的 JSON 更容易使用。它允许你声明性地指定如何从 JSON 文档中提取元素。以下是一些基本示例：



import jmespath

# Get a specific element
d = {"foo": {"bar": "baz"}}
print(jmespath.search('foo.bar', d))
# baz

# Using a wildcard to get all names
d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
print(jmespath.search('foo.bar[*].name', d))
# [“one”, “two”]



更多消息，请参见PyPI页面和文档。

16.Setuptools
下载次数：4.01 亿



它是用于创建 Python 包的工具。不过，其文档很糟糕。它没有清晰描述它的用途，并且文档中包含无效链接。最好的信息源是这个站点，特别是这个创建 Python 包的指南。

17.Awscli
这里把 #3、#7、#17 和 #22 放在一起介绍，因为它们的关系非常密切。

18.Pytz
下载次数：3.94 亿次



像dateutils（#5）一样，这个库可帮助你处理日期和时间。有时候，时区处理起来可能很麻烦。幸好有这样的包，可以让事情变得简单些。



我自己关于计算机上处理时间的经验总结来说是：始终在内部使用 UTC。仅当生成供人类读取的输出时，才转换为本地时间。



这是pytz用法的示例：



from datetime import datetime
from pytz import timezone

amsterdam = timezone('Europe/Amsterdam')

ams_time = amsterdam.localize(datetime(2002, 10, 27, 6, 0, 0))
print(ams_time)
# 2002-10-27 06:00:00+01:00

# It will also know when it's Summer Time
# in Amsterdam (similar to Daylight Savings Time):
ams_time = amsterdam.localize(datetime(2002, 6, 27, 6, 0, 0))
print(ams_time)
# 2002-06-27 06:00:00+02:00



请查看 PyPI 页面以获取更多示例和文档。

19.Futures
下载次数：3.89 亿



从 Python 3.2 开始，python 提供current.futures模块，可帮助你实现异步执行。futures 包是该库适用于 Python 2 的 backport。它不适用于 Python3 用户，因为 Python 3 原生提供了该模块。



正如我之前提到的，从 2020 年 1 月 1 日起，Python 2的官方支持停止。希望我明年重新再来看的时候，这个包不会再出现在前 22 名中吧。



下面是 futures 的基本示例：



from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
def return_after_5_secs(message):
  sleep(5)
  return message
 
pool = ThreadPoolExecutor(3)
 
future = pool.submit(return_after_5_secs, 
                     ("Hello world"))

print(future.done())
# False
sleep(5)
print(future.done())
# True
print(future.result())
# Hello World



如你所见，你可以创建一个线程池并提交一个要由这些线程之一执行的函数。同时，你的程序将继续在主线程中运行。这是并行执行程序的简便方法。

20.Colorama
下载次数：3.7 亿



使用Colorama，你可以为终端添加一些颜色：






这样做起来非常容易，具体请查看以下示例代码：



from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

21.Simplejson
下载次数：3.41 亿



原生的json模块有什么问题，才需要这种高级替代方案呢？并没有！实际上，Python 的json就是simplejson。但是simplejson也有一些优点：



它适用于更多的 Python 版本。

它比 Python 更新的频率更频繁。

它有用 C 编写的（可选）部分，因此速度非常快。



你经常会在支持 JSON 的脚本中看到以下内容：



try:
  import simplejson as json
except ImportError:
  import json



除非你需要标准库中所没有的内容，否则我只会使用json。Simplejson可以比json快很多，因为它有一些用 C 实现的部分。除非你正在处理成千上万个 JSON 文件，否则这种优势对你来说不是什么大事。还可以看看UltraJSON，它应该更快一些，因为它几乎所有的代码都是用 C 编写的。

22.Boto3
这里把 #3、#7、#17 和 #22 放在一起介绍，因为它们的关系非常密切。

小结
仅仅介绍这 22 个包恐怕不够，因为排在后面的许多包都是像我们这样最终用户感兴趣的。



通过制作这份列表，我了解到一些新东西：



许多排名靠前的 package（包）都提供某种核心功能，例如处理时间、配置文件、加密和标准化等。它们往往是其他项目的依赖项。

一个常见的主题是连接性。这些包大多允许你连接到服务器和服务，或支持其他包这样做。

剩下的那些是对 Python 的扩展。创建 Python 包的工具、帮助创建文档的工具、创建版本之间兼容性的库等。

