# 17.3 Hacker News API
# 返回Hacker News上当前热门文章的ID，再查看每篇排名靠前的文章
from operator import itemgetter

import requests

# 执行API调用并存储响应
# 文件topstories.json存储了元素为最热门500篇文章ID的列表
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
# 分析前30篇文章
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    # 文件id.json存储了关于文章信息的字典
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    # 文章信息字典的键title的值为文章题目，键descendant的值为文章被评论次数
    submission_dict = {
        "title": response_dict["title"],
        "link": "https://news.ycombinator.com/item?id=" + str(submission_id),
        # 字典实例.get(
        #     key=待查询的键<> | 无默认值,
        #     value=键不存在时返回的值<>)
        # 返回字典键对应的值，在键不存在时返回指定值
        # 没有评论的评论数为0
        "comments": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)
# itemgetter(
#     接收数个索引<整型数>或键<>: 仅限位置实参; 指定待获取数据的索引或键)
# 返回一个用于获取集合的哪些位置的元素的函数
# 返回的函数的参数类型为集合————列表、元组、字符串、字典
# 只有一个参数时，返回的函数的返回值为集合中待获取的元素；有多个参数时，返回的函数的返回值类型为元组，元组的元素为集合中被获取的元素
# 网站上的文章根据综合指标排序，而本程序仅关注评论数，将文章依评论数降序排列
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

# 对应文章信息
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict["title"])
    print("Discussion link:", submission_dict["link"])
    print("Comments:", submission_dict["comments"])
