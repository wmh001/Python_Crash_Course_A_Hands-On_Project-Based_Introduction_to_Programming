# 3.2 修改、添加和删除元素

# 3.2.1 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# 访问列表元素并赋值即修改元素
motorcycles[0] = "ducati"
print(motorcycles)

# 3.2.2 在列表中添加元素
# 列表实例.append(
#     待添加的元素<>: 不接收关键字实参 | 无默认值)
# 在列表实例的末尾添加元素，原列表实例改变
motorcycles.append("honda")
print(motorcycles)
# 动态创建列表
motorcycles = []
print(motorcycles)
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
# 列表实例.insert(
#     索引<整型数>: 不接收关键字实参 | 无默认值,
#     新元素值<>: 不接收关键字实参 | 无默认值)
# 在列表实例的对应索引处插入新元素，原列表实例改变，原列表实例中该索引及其后的元素索引加一（后移一位）
motorcycles.insert(0, "ducati")
print(motorcycles)

# 3.2.3 从列表中删除元素
# 已知索引，del语句删除元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# del 列表实例[索引<整型数>: 非负索引从0开始，为元素在有序集合中的序数减一; 负索引表示元素为有序集合中的倒数第几个]
# 删除列表实例中对应索引处的元素，原列表实例改变，原列表实例中该索引后的元素索引减一（前移一位）
del motorcycles[0]
print(motorcycles)
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# 列表实例.pop(
#     索引<整型数>: 不接收关键字实参 | -1: 最后一个元素)
# 返回列表实例中对应索引处的元素，原列表实例删除该元素，其后元素索引减一（前移一位）
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
print(motorcycles)

# 已知元素的值，remove方法删除元素
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
# 列表实例.remove(
#     表达式<>: 不接收关键字实参 | 无默认值)
# 删除原列表实例中第一个等于该表达式的值的元素，原列表实例改变，原列表实例中该值后的元素索引减一（前移一位）
# 原列表实例中没有等于该表达式的值的元素时报错
motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
