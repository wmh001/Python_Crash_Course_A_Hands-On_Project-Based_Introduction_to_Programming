"""生成全名"""


def get_formatted_name_1(first, last):
    """生成全名（名和姓）"""
    full_name = first + " " + last
    return full_name.title()


def get_formatted_name_2(first, middle, last):
    """生成全名（名、中间名和姓）"""
    full_name = first + " " + middle + " " + last
    return full_name.title()


def get_formatted_name_3(first, last, middle=""):
    """生成全名（名、中间名和姓或名和姓）"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()
