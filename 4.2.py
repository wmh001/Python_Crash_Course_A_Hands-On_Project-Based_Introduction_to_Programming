# 4.2 避免缩进错误
# Python根据缩进来判断代码行与前一个代码行的关系

# 4.2.1 忘记缩进
# 缺少缩进报错
mangicians = ["alice", "david", "carolina"]
for mangician in mangicians:
print(mangician)

# 4.2.2 忘记缩进额外的代码行
# 可能不会报错，但在循环中仅执行部分代码
for mangician in mangicians:
    print(mangician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + mangician.title() + ".\n")

# 4.2.3 不必要的缩进
# 多余缩进报错
message = "Hello Python world!"
    print(message)

# 4.2.4 循环后不必要的缩进
# 可能不会报错，但在循环中执行多余代码
for mangician in mangicians:
    print(mangician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + mangician.title() + ".\n")
    print("Thank you, everyone. That was a great magic show!")

# 4.2.5 遗漏了冒号
# 缺少冒号报错
for mangician in mangicians
    print(mangician)
