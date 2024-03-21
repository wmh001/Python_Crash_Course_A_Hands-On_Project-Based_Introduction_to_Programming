# 7.3 使用while循环来处理列表和字典

# 7.3.1 在列表之间移动元素
# 在循环中对列表执行的操作在循环结束后仍有效
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Veifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# 7.3.2 删除包含特定值的所有列表元素
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

# 删除原列表中所有等于值的元素应使用以下方案
while "cat" in pets:
    pets.remove("cat")
    print(pets)

print(pets)

# 7.3.3 使用用户输入来填充字典
responses = {}

# 标志
polling_active = True

while polling_active:
    # 获取输入
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 存储
    responses[name] = response

    # 是否继续循环
    repeat = input("would you like to let another person respond? (yes/ no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
