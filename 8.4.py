# 8.4 传递列表


def greet_users(names):
    """向列表中的每位用户都发出简单的问题"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "try", "margot"]
greet_users(usernames)

# 8.4.1 在函数中修改列表
# 在Python中，在函数中对一般变量的修改通常在函数结束后无效，但对列表的修改在函数运行结束后仍然有效
# Python推崇这样一种理念：每个函数应只负责一项具体的工作，通过函数嵌套和连续使用函数完成复杂任务

# 不使用函数
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# 使用函数
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []


def print_models(unprinted_designs, completed_models):
    """打印每个设计，打印后将其移动到新列表中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.4.2 禁止函数修改列表
# 向函数传递列表的副本（与被复制列表实例的元素和顺序相同的新列表实例）
# 这样做会降低程序效率
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
print(completed_models)
