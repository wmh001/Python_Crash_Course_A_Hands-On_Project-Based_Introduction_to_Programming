# 4.4 使用列表的一部分
# 切片：列表的部分元素组成的列表

# 4.4.1 切片
players = ["charles", "martina", "michael", "florence", "eli"]
# 列表实例[起点索引<整型数> | 0:终点索引<整型数> | end+1: 假定的最后一个元素的后一个元素的索引]
# 返回起点索引到终点索引（不含）对应的所有元素按原列表实例的顺序排列组成的列表实例
# 支持负索引
# 起点索引与终点索引对应位置相同和起点索引比终点索引对应位置靠后时，返回空列表
print(players[0:3])
print(players[1:4])

# 第一个索引省略时，默认为0
print(players[:4])
# 第二个索引省略时，切片默认包括到最后一个元素
print(players[2:])
# 可以使用负索引
print(players[-3:])

# 4.4.2 遍历切片
# 在for循环中使用切片
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

# 4.4.3 复制列表
my_food = ["pizza", "falafel", "carrot cake"]
# 被复制列表实例<列表>[:]
# 返回新列表实例，其元素与被复制列表实例的元素相等并顺序相同
friend_food = my_food[:]
print("My favorite foods are:")
print(my_food)
print("\nMy friend's favorite foods are:")
print(friend_food)

# 对二者的操作不会相互影响
my_food.append("cannoli")
friend_food.append("ice cream")
print("My favorite foods are:")
print(my_food)
print("\nMy friend's favorite foods are:")
print(friend_food)


my_food = ["pizza", "falafel", "carrot cake"]
# 新列表实例 = 旧列表实例
# 给旧列表实例起别名，不创建新列表实例，而是将新列表实例指向旧列表实例
friend_food = my_food
# 对二者的操作等价于对同一列表操作
my_food.append("cannoli")
friend_food.append("ice cream")
print("My favorite foods are:")
print(friend_food)
print("\nMy friend's favorite foods are:")
print(friend_food)
