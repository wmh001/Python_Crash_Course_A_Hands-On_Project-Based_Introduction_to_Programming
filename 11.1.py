# 11.1 测试函数
import unittest

from name_function11_1 import (
    get_formatted_name_1,
    get_formatted_name_2,
    get_formatted_name_3,
)

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("Please give me a last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name_1(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")

# 11.1.1 单元测试和测试用例
# 单元测试用于核实函数的每个方面没有问题
# 测试用例是一组单元测试，核实函数在各种情形下的行为都符合要求

# 11.1.2 可通过的测试
# class 测试类名(unittest.TestCase):
#     def 测试函数1(self):
#         函数体1
#     ···
#     def 测试函数i(self):
#         函数体i
#     ···
#     def 测试函数n(self):
#         函数体n
# 定义用于测试的类（unittest.TestCase的子类）


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name_1(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name_1("janis", "joplin")
        # unittest.TestCase实例.assertEqual(
        #     first=函数返回值<> | 无默认值,
        #     second=目标值<> | 无默认值,
        #     其他参数: 均有默认值)
        # 打印测试报告，比较函数返回值与目标值是否相同

        # 报告格式为
        # 第一行为表明各个单元测试是否通过，
        # .表明某个单元测试通过了
        # E表明某个单元测试引发错误
        # F表明某个单元测试导致断言失败
        # 排列.、E和F的顺序无意义
        # 如果存在测试未通过（E或F），下一区域为依未通过的单元测试的测试函数定义顺序排列未通过报告
        # 下一行为---分隔线
        # 下一行指出运行了几个测试，并指出测试时间
        # 下一行为一空行
        # 下一行表明是否有测试未通过
        # 在所有单元测试都通过时为OK
        # 在有单元测试未通过时为FAILED(errors=引发错误单元测试数, failures=断言失败单元测试数)，单元测试数为0时该项缺省

        # 未通过报告格式为
        # 第一行为===分隔线
        # 下一行为ERROR（引发错误）/FAIL（导致断言失败）: 未通过的单元测试的测试函数名(__main__.测试类名)
        # 下一行为未通过的单元测试的测试函数的文档字符串
        # 下一行为---分隔线
        # 下一区域显示一个traceback，其中包含有关异常的报告
        # 下一行为一空行
        self.assertEqual(formatted_name, "Janis Joplin")

    # 11.1.3 不能通过的测试
    def test_first_last_name_2(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name_2("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    # 11.1.4 测试未通过时怎么办
    # 修改函数
    def test_first_last_name_3(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name_3("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    # 11.1.5 添加新测试
    # 增加方法
    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name_3("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


# unittest.main()
# 运行用于测试的类的setUp()方法和所有以test_打头的方法
unittest.main()
