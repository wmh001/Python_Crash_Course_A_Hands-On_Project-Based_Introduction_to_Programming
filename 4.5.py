# 4.5 元组
# 元组（tuple）是由一系列按一定顺序排列的不可修改元素组成的集合
# Python中，元组用()标记，用,分隔元素，元素可以为任何类型，不同元素类型可以不同
# 元组相当于不可修改元素的列表，是比列表更简单的数据结构

# 4.5.1 定义元组
dimensions = (200, 50)
# 利用索引访问元素
# 元组实例[索引<整型数>: 非负索引从0开始，为元素在有序集合中的序数减一; 负索引表示元素为有序集合中的倒数第几个]
# 返回元组实例中索引对应位置的元素
print(dimensions[0])
print(dimensions[1])

# 修改元组元素报错
dimensions[0] = 250

# 4.5.2 遍历元组中的所有值
# 元组与列表同为可迭代对象
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量
# 不可修改元组元素，但可以修改整个元组
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
