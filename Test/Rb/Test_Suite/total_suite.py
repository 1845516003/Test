import unittest

from Test_Case.case import LoginCase
from Test_Case.case import UsermanagementCase
from Test_Case.case import GroupmanagementCase
from Test_Case.case import FilemanagementCase



def return_suite():
    # 测试套件
    suite = unittest.TestSuite()
    # 加载器
    loader = unittest.TestLoader()
    # 通过使用加载器，将测试用例添加到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(LoginCase))
    suite.addTests(loader.loadTestsFromTestCase(UsermanagementCase))
    suite.addTests(loader.loadTestsFromTestCase(GroupmanagementCase))
    suite.addTests(loader.loadTestsFromTestCase(FilemanagementCase))

    # 返回测试套件
    return suite
