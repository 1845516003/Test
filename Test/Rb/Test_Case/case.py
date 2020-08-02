import unittest
import time
import ddt
from Common.read_test_data import read_txt
from Business.operation_flow import *


@ddt.ddt
class LoginCase(unittest.TestCase, Login):
    def setUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/login_data'))
    def test_login(self, username, password, asserttpye):
        self.driver.get("http://172.16.45.33:8088")
        self.login(username, password)
        #Login.login(self, username, password)
        time.sleep(2)
        self.addImage()
        if asserttpye == 2:
            ele = self.driver.find_element_by_xpath('/html/body/div[2]/p').text
            self.assertEqual('用户名或密码错误', ele, '测试通过')
        elif asserttpye == 1:
            ele = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/img").text
            self.assertEqual('/html/body/div/div/div[2]/div/img ', ele.text, "测试通过")

        time.sleep(1)
        self.addImage()

@ddt.ddt
class UsermanagementCase(unittest.TestCase, Usermanagement):
    def setUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/user_data'))
    def test_usermanagement(self, username1, password1,password2, asserttpye1):
        self.driver.get("http://172.16.45.33:8088")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/div/div/div[1]/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[4]/div/div/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[5]/div/button/span').click()
        self.usermanagement(username1, password1,password2)
        # Login.login(self, username, password)
        time.sleep(2)
        self.addImage()
        if asserttpye1 == 2:
            ele = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[3]/div/div/div/div[2]').text
            self.assertEqual('两次密码不一致', ele, '测试通过')
        elif asserttpye1 == 3:
            ele = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[1]/div/div/div/div[2]").text
            self.assertEqual('用户名只能是中文、英文、数字组成，最长填写16位', ele.text, "测试通过")
        elif asserttpye1 == 1:
            ele = self.driver.find_element_by_xpath('/html/body/div[3]/p').text
            self.assertEqual('保存成功', ele.text, "测试通过")
        elif asserttpye1 == 4:
            ele = self.driver.find_element_by_xpath('/html/body/div[3]/p').text
            self.assertEqual('用户已存在', ele.text, "测试通过")
        time.sleep(1)
        self.addImage()



@ddt.ddt
class GroupmanagementCase(unittest.TestCase, Groupmanagement):
    def setUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/group_data'))
    def test_groupmanagement(self, groupname, asserttpye2):
        self.driver.get("http://172.16.45.33:8088")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/div/div/div[1]/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[4]/div/div/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[5]/div/button/span').click()
        self.groupmanagement(groupname)
        # Login.login(self, username, password)
        time.sleep(2)
        self.addImage()
        if asserttpye2 == 2:
            ele = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[1]/div/div/div/div[2]').text
            self.assertEqual('组名只能是中文、英文、数字组成，最长填写16位', ele, '测试通过')
        elif asserttpye2 == 1:
            ele = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
            self.assertEqual('登入成功', ele.text, "测试通过")
        elif asserttpye2 == 3:
            ele = self.driver.find_element_by_xpath('/html/body/div[3]/p').text
            self.assertEqual('分组已存在', ele.text, "测试通过")
        time.sleep(1)
        self.addImage()

@ddt.ddt
class FilemanagementCase(unittest.TestCase, Filemanagement):
    def setUp(self):
        self.driver = self.get_browser()
        self.driver.implicitly_wait(10)
        pass

    def tearDown(self):
        self.driver.quit()
        pass

    @ddt.unpack
    @ddt.data(*read_txt('Test_Data/newtitle_data'))
    def test_filemanagement(self, newtitle, asserttpye3):
        self.driver.get("http://172.16.45.33:8088")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[3]/div/div/div/div[1]/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[4]/div/div/div/div/input').send_keys("admin")
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/form/div[5]/div/button/span').click()
        self.filemanagement(newtitle)
        # Login.login(self, username, password)
        time.sleep(2)
        self.addImage()
        if asserttpye3 == 2:
            ele = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/form/div[1]/div/div[2]').text
            self.assertEqual('文件夹名称只能由中文、英文、数字、下划线组成，请检查格式', ele, '测试通过')
        elif asserttpye3 == 1:
            ele = self.driver.find_element_by_xpath("/html/body/div[3]/p").text
            self.assertEqual('保存成功', ele.text, "测试通过")
        time.sleep(1)
        self.addImage()
