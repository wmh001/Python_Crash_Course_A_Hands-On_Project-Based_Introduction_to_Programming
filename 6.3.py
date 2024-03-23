# 6.3 遍历字典

# 6.3.1 遍历所有的键-值对
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
# 字典实例.items()
# 返回可迭代类dict_items实例
# 其每个元素为1个记录键值对的元组，键为元组第一个元素，值为元组第二个元素，其元素元组顺序未规定
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print(type(user_0.items()))
for kv in user_0.items():
    print("(Key, Value): (" + str(kv[0]) + ", " + str(kv[1]) + ")")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rudy",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 6.3.2 遍历字典中的所有键
# 字典实例.keys()
# 返回可迭代类dict_keys实例，其元素为键，其元素顺序未规定
for name in favorite_languages.keys():
    print(name.title())

print(type(favorite_languages.keys()))

# .key()缺省时，默认遍历键
for name in favorite_languages:
    print(name.title())

# 遍历时，对于选定键施加特殊处理
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(
            "  Hi "
            + name.title()
            + ", I see your favorite language is "
            + favorite_languages[name].title()
            + "!"
        )

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll")

# 6.3.3 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值
# 字典实例.values()
# 返回可迭代类dict_values实例，其元素为值，其元素顺序未规定
print("The follow languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# type(
#     待检测量<>: 不接收关键字实参 | 无默认值)
# 返回待检测量的类型
print(type(favorite_languages.values()))

for language in sorted(favorite_languages.values()):
    print(language.title())

# set(
#     字典中所有值<dict_values类>: 仅限位置实参 | 无默认值)
# 返回去除字典中值的重复值的集合set，集合元素的顺序未规定
print("The follow languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print(type(set(favorite_languages.values())))
