# 10.2 写入文件

# 10.2.1 写入空文件
filename = "programming10_2_1.txt"

with open(filename, "w") as file_object:
    # 文件实例.write(
    #     写入内容<字符串>: 仅限位置实参 | 无默认值)
    # 将一个字符串写入文件实例
    file_object.write("I love programming.")

# 10.2.2 写入多行
# 没有换行符
filename = "programming10_2_2.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# 有换行符
filename = "programming10_2_3.txt"

with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.2.3 附加到文件
# 将新内容添加到原文件结尾
filename = "programming10_2_3.txt"

with open(filename, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
