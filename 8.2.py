# 8.2 传递实参

# 8.2.1 位置实参
# 调用函数时，实参顺序与形参顺序相同且序数相同的关联方式称为位置实参

# 在函数定义的参数列表中，可以使用标记对使用位置实参还是关键字实参进行限制
# 标记在形式参数列表中占用一个参数位置，在实际参数列表中不留位置
# 标记/前的参数仅限位置实参


def describe_pet_1(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_1("hamster", "harry")
# 函数多次调用可提高效率
describe_pet_1("dog", "willie")
# 使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料
describe_pet_1("harry", "hamster")

# 8.2.2 关键字实参
# 调用函数时，以=连接形参名-值对的关联方式称为关键字实参
# 使用关键字实参时，实参顺序无关紧要

# 标记*后的参数仅限关键字实参，标记*应当在标记/后
describe_pet_1(animal_type="hamster", pet_name="harry")
describe_pet_1(pet_name="harry", animal_type="hamster")

# 8.2.3 默认值
# 定义函数时可给每个形参指定默认值
# 在调用函数时，若该形参没有提供实参则使用函数的默认值
# 使用默认值可简化调用，还可指出函数的典型用法


# 指定默认值的形参置于参数列表末尾，没有默认值的形参先列出
# 这样便于解读位置实参
# 此时调用函数时未指定默认值和不使用默认值且顺序对应的形参可使用位置实参
# 使用默认值的形参缺省
# 不使用默认值且顺序不对应的形参使用关键字实参
# 这种调用方式最简单
def describe_pet_2(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_2(pet_name="willie")
describe_pet_2("willie")
describe_pet_2(pet_name="harry", animal_type="hamster")

# 8.2.4 等效的函数调用
# 由于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式

# 以下调用等价
describe_pet_2("willie")
describe_pet_2(pet_name="willie")

# 以下调用等价
describe_pet_2("harry", "hamster")
describe_pet_2(pet_name="harry", animal_type="hamster")
describe_pet_2(animal_type="hamster", pet_name="harry")

# 8.2.5 避免实参错误
# 提供的实参多于形参或少于未指定默认值形参时报错


def describe_pet_3(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_3()
