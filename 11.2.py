# 11.2 测试类

# 11.2.1 各种断言方法
# unittest.TestCase类常用的断言方法：
# assertEqual(a, b)       核实a == b
# assertNotEqual(a, b)    核实a != b
# assertTrue(x)           核实x为True
# assertFalse(x)          核实x为False
# assertIn(item, list)    核实item在list中
# assertNotIn(item, list) 核实item不在list中

# 11.2.2 一个要测试的类
import unittest

from survey11_2 import AnonymousSurvey

# 定义一个问题，并创建一个问卷调查实例
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

# 11.2.3 测试AnonymousSurvey类


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    # 11.2.4 方法setUp()
    # unittest.TestCase子类.setUp()
    # 如果在unittest.TestCase的子类中重写unittest.TestCase类.setUp()函数，将先运行该函数，再运行test_打头的函数
    # 该函数用于测试初始化，如创建多个测试函数使用的属性等
    def setUp(self):
        """创建一个调查对象和一组答案，供测试函数使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["C++", "Python", "Java"]

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        # unittest.TestCase实例.assertIn(
        #     member=目标值<> | 无默认值,
        #     container=实例属性<列表> | 无默认值,
        #     其他参数: 均有默认值)
        # 打印测试报告，核实目标值是否在属于实例属性的列表中
        # 报告格式与函数unittest.TestCase实例.assertEqual(函数返回值<>, 目标值<>)相同
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
