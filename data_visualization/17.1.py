# 17.1 使用Web API
# Web API是网站的一部分，用于与使用非常具体的URL请求特定信息特定信息的程序交互
# 这种请求称为API调用
# 请求的数据将以易于处理的格式（如JSON或CSV）返回

# 17.1.1 Git和GitHub
# 本章将基于来自GitHub的信息
# 使用GitHub的API请求GitHub中的Python项目信息，使用Pygal生成交互式可视化，呈现这些项目的受欢迎程度

# Git是一个分布式版本控制系统，让程序员团队能够协作开发、同步修改项目，避免团队成员各自对项目的修改产生冲突
# 在GitHub上，用户可以给喜欢的项目加星以表示支持

# 17.1.2 使用API调用请求数据
# 网址https://api.github.com/search/repositories?q=language:python&sort=stars
#     记录了GitHub当前托管了多少个Python项目、最受欢迎的Python仓库信息
# https://api.github.com/  将请求发送到GitHub中响应API调用的部分
# search/repositories  让API搜索GitHub上的所有仓库
# ?  要传递一个实参
# q  查询
# =  指定查询什么
# language:python  获取主要语言为Python的仓库的信息
# sort=stars  将项目按其获得的星级进行排序

# "total_count":  GitHub总共有几个项目
# "incomplete_results": false  返回不是不完整的，请求成功
# "items":  最受欢迎的Python项目的详细信息

# 17.1.3 安装requests
# pip install requests

# 17.1.4 处理API响应
import requests

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# requests.get(
#     url=请求的网址<字符串> | 无默认值,
#     params=url中额外参数<字典/字节流> | None
#     其他项目: 均有默认值)
# 返回请求响应Response实例，记录本次请求的服务器响应结果

# requests.models.Response类的常用属性：
# status_code<整型数>：HTTP请求的返回状态，200连接成功，404连接失败
# text<字符串>：响应内容的字符串形式，即url对应的页面内容
# encoding<字符串>：从HTTP header中猜测的响应内容编码方式
# apparent_encoding<字符串>：从内容分析出的响应内容编码方式（备选编码方式）
# content：HTTP响应内容的二进制形式
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
# requests.models.Response实例.json()
# 如果请求响应内容的格式是json格式，返回记录请求响应内容的字典
response_dict = r.json()

# 处理结果
print(response_dict.keys())

# 17.1.5 处理响应字典
print("Total repositories:", response_dict["total_count"])

# 探索有关仓库的信息
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# 打印信息
print("\nSelected information about first repository:")
print("Name:", repo_dict["name"])
print("Owner:", repo_dict["owner"]["login"])
print("Stars:", repo_dict["stargazers_count"])
print("Repository:", repo_dict["html_url"])
print("Created:", repo_dict["created_at"])
print("Updated:", repo_dict["updated_at"])
print("Description:", repo_dict["description"])

# 17.1.6 概述最受欢迎的仓库
# 循环处理
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print("\nName:", repo_dict["name"])
    print("Owner:", repo_dict["owner"]["login"])
    print("Stars:", repo_dict["stargazers_count"])
    print("Repository:", repo_dict["html_url"])
    print("Description:", repo_dict["description"])

# 17.1.7 监视API的速率限制
# 大多数API都存在速率限制，即在特定时间内可执行的请求数存在限制
# 网址https://api.github.com/rate_limit 记录了速率限制

# search["limit"]：搜索速率限制（次/分钟）
# search["remaining"]：本分钟剩余请求次数（次）
# search["reset"]：配额将重置的Unix时间或新纪元时间（新纪元时间为1970年1月1日午夜），用完配额后，必须等待配额重置

# 很多API都要求注册获得API密钥后才能执行API调用，目前GitHub没有这样的要求，但获得API密钥后，配额将高得多
