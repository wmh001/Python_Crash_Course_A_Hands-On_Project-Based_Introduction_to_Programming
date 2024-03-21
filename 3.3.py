# 3.3 组织列表
# 调整排列顺序

# 3.3.1 使用方法sort()对列表进行永久性排序
# 列表实例.sort(
#     key=排序依据<函数名>: 仅限关键字实参; 返回列表实例元素用于排序的属性 | None: 列表实例元素的值,
#     reverse=是否降序排列<布尔>: 仅限关键字实参 | Flase)
# 对列表实例的元素以一定依据进行按一定顺序的排序，原列表实例改变
# 列表实例元素用于排序的属性的类型应当相同或进行自动类型转换后可以相同（如整型数向浮点数）
# 一般排序规则：
# 若排序属性为数字，升序为从小到大，降序相反
# 若排序属性为字符串，升序为英文字典顺序（先按字符串第1个字符的编码顺序，第1个字符相同再按字符串的第2个字符的编码顺序），降序相反
# 若排序属性为列表和元组，先按各元素排序属性的第1个元素排，第1个元素相同再按各元素排序属性的第2个元素排，以此类推
# 若排序属性为字典，报错
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# 3.3.2 使用函数sorted()对列表进行临时排序
# 序列即有序集合
# sorted(
#     原始序列<列表/字符串/字典/dict_keys/dict_values/其他某些可迭代对象>: 不接收关键字实参;
#         该序列元素用于排序的属性的类型应当相同或进行自动类型转换后可以相同，如整型数向浮点数 | 无默认值,
#     key=排序依据<函数名>: 仅限关键字实参; 返回原始序列元素用于排序的属性 | None: 原始序列元素的值,
#     reverse=是否降序排列<布尔>: 仅限关键字实参 | Flase)
# 返回对原始序列的元素以一定依据进行按一定顺序排序后的序列转换成的列表实例，原始序列不变
# 一般排序规则：
# 若排序属性为数字，升序为从小到大，降序相反
# 若排序属性为单个字符，升序为字母表顺序（编码顺序），降序相反
# 若排序属性为字符串，升序为英文字典顺序（先按字符串第1个字符的编码顺序，第1个字符相同再按字符串的第2个字符的编码顺序），降序相反
# 若排序属性为列表和元组，先按各元素排序属性的第1个元素排，第1个元素相同再按各元素排序属性的第2个元素排，以此类推
# 若排序属性为键值对，返回字典键组成的列表实例，字典键的排序规则为一般排序规则
# 若排序属性为字典，报错
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)
print("\nHere is the reversed list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list:")
print(cars)

# 3.3.3 倒着打印列表
# 列表实例.reverse()
# 对列表实例的元素进行顺序反转，原列表实例改变
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)

# 3.3.4 确定列表的长度
# len(
#     待统计规模集合<列表/元组/字符串/其他某些集合>: 仅限位置实参 | 无默认值)
# 返回集合元素数量
print(len(cars))
