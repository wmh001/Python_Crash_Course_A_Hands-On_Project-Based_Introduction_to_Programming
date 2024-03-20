# 3.1 列表是什么
# 列表（list）是由一系列按一定顺序排列的可修改元素组成的集合
# Python中，列表用[]标记，用,分隔元素，元素可以为任何类型，不同元素类型可以不同
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# 3.1.1 访问列表元素
# 列表实例[索引<整型数>: 非负索引从0开始，为元素在有序集合中的序数减一; 负索引表示元素为有序集合中的倒数第几个]
# 返回列表实例中对应索引的元素
print(bicycles[0])
print(bicycles[0].title())

# 3.1.2 索引从0而不是1开始
# 第二个元素索引为1，第四个元素索引为3
print(bicycles[1])
print(bicycles[3])
# 索引-1对应最后一个元素，-2对应倒数第二个元素
print(bicycles[-1])

# 3.1.3 使用列表中的各个值
print("My first bicycle was a " + bicycles[0].title() + ".")
