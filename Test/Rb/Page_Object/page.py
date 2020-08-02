from selenium.webdriver.common.by import By
from Common.selenium_tools import SeleniumWebDriver

#登入
class LoginPage(SeleniumWebDriver):
    username_loc = (By.XPATH, '/html/body/div/div/div[1]/form/div[3]/div/div/div/div[1]/input')          #定位用户名输入框
    password_loc = (By.XPATH, '/html/body/div/div/div[1]/form/div[4]/div/div/div/div/input')          #定位密码输入框
    login_loc = (By.XPATH, "/html/body/div/div/div[1]/form/div[5]/div/button")             #定位点击登入按钮
    def send_username(self, username):
        ele=self.find_element(self.username_loc)
        ele.clear()
        ele.send_keys(username)
    def send_password(self, password):
        ele=self.find_element(self.password_loc)
        ele.clear()
        ele.send_keys(password)
    def send_login(self):
        self.find_element(self.login_loc).click()


#用户管理
class UsermanagementPage(SeleniumWebDriver):
    usermanagement_loc =(By.XPATH,'/html/body/div/div/div[3]/div/ul/li[4]/a/span') #定位点击用户管理模块
    adduser_loc = (By.XPATH,'/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/button[1]')              #定位点击添加用户按钮
    username1_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[1]/div/div/div/div/input')           #定位输入用户名输入框
    password1_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[2]/div/div/div/div/input')           #定位输入密码输入框
    password2_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[3]/div/div/div/div/input')           #定位再次输入密码输入框
    selectgroup1_loc =(By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[5]/div/div/div/div/div[1]/input')         #定位选择分组框
    selectgroup2_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')        #定位选择分组
    preservation1_loc = (By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/button[1]')       #定位保存按钮
    def send_usermanagement(self):
        self.find_element(self.usermanagement_loc).click()
    def send_adduser(self):
        self.find_element(self.adduser_loc).click()
    def send_username1(self, username1):
        ele=self.find_element(self.username1_loc)
        ele.clear()
        ele.send_keys(username1)
    def send_password1(self, password1):
        ele=self.find_element(self.password1_loc)
        ele.clear()
        ele.send_keys(password1)
    def send_password2(self, password2):
        ele=self.find_element(self.password2_loc)
        ele.clear()
        ele.send_keys(password2)
    def send_selectgroup1(self):
        self.find_element(self.selectgroup1_loc).click()
    def send_selectgroup2(self):
        self.find_element(self.selectgroup2_loc).click()
    def send_preservation1(self):
        self.find_element(self.preservation1_loc).click()


#分组管理
class GroupmanagementPage(SeleniumWebDriver):
    groupmanagement_loc =(By.XPATH,'/html/body/div/div/div[3]/div/ul/li[3]/a/span')                 #定位点击分组管理
    addgroup_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/button[1]')                          #定位添加分组按钮
    groupname_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[1]/form/div[1]/div/div/div/div/input')                         #定位输入分组名框
    preservation2_loc = (By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/button[1]')                     #定位保存按钮
    def send_groupmanagent(self):
        self.find_element(self.groupmanagement_loc).click()
    def send_addgroup(self):
        self.find_element(self.addgroup_loc).click()
    def send_groupname(self, groupname):
        ele=self.find_element(self.groupname_loc)
        ele.clear()
        ele.send_keys(groupname)
    def send_preservation2(self):
        self.find_element(self.preservation2_loc).click()


#文件管理
class FilemanagementPage(SeleniumWebDriver):
    filemanagement_loc =(By.XPATH,'/html/body/div/div/div[3]/div/ul/li[5]/a/span')                          #定位点击文件管理
    clickmodify_loc =(By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/ul/li[1]/a/div[2]/span[2]')                            #定位点击修改按钮
    newtitle_loc =(By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[2]/form/div[1]/div/div/input')                               #定位文件名输入框
    determine_loc =(By.XPATH, '/html/body/div/div/div[4]/div/div[1]/div/div[1]/div[3]/div/div[3]/div/button[2]')                              #定位确定按钮
    def send_filemanagement(self):
        self.find_element(self.filemanagement_loc).click()
    def send_clickmodify(self):
        self.find_element(self.clickmodify_loc).click()
    def send_newtitle(self, newtitle):
        ele=self.find_element(self.newtitle_loc)
        ele.clear()
        ele.send_keys(newtitle)
    def send_determine(self):
        self.find_element(self.determine_loc).click()