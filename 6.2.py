# 6.2 使用字典

# 6.2.1 访问字典中的值
alien_0 = {"color": "green"}
# 字典实例[键<>]
# 返回字典实例中对应键的值
print(alien_0["color"])
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")

# 6.2.2 添加键-值对
# 字典实例[新键<>] = 新值<>
# 在字典实例中添加新键值对，原字典实例改变
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# 某些环境下，打印键-值对的排列顺序与添加顺序不同

# 6.2.3 先创建一个空字典
alien_0 = {}
print(alien_0)
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

# 6.2.4 修改字典中的值
alien_0 = {"color": "green"}
print("The alien is " + alien_0["color"] + ".")
# 字典实例[已存在键<>] = 新值<>
# 修改字典实例中已存在键对应的值，原字典实例改变
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")

# 创建中速外星人并按其速度将其右移
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-postion: " + str(alien_0["x_position"]))
# 向右移动
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0["x_position"]))

# 中速外星人变为高速并按其速度将其右移
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
alien_0["speed"] = "fast"
print("Original x-postion: " + str(alien_0["x_position"]))
# 向右移动
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0["x_position"]))

# 6.2.5 删除键-值对
alien_0 = {"color": "green", "points": 5}
print(alien_0)
# del 字典实例[已存在键<>]
# 删除字典实例中对应键的键值对，原字典实例改变
del alien_0["points"]
print(alien_0)

# 6.2.6 由类似对象组成的字典
# 上文展示了字典存储了一个对象的多种信息
# 字典也可以存储多个对象的同一信息
# 多个被调查者最喜欢的语言
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rudy",
    "phil": "python",
}
print("Sarah's favorite language is " + favorite_languages["sarah"].title() + ".")
