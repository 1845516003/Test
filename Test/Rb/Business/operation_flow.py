from Page_Object.page import *
#from Page_Object.index import Index


class Login(LoginPage):
    def login(self, username, password):
        self.send_username(username)
        self.send_password(password)
        self.send_login()
        pass

class Usermanagement(UsermanagementPage):
    def usermanagement(self, username1, password1 ,password2):
        self.send_usermanagement()
        self.send_adduser()
        self.send_username1(username1)
        self.send_password1(password1)
        self.send_password2(password2)
        self.send_selectgroup1()
        self.send_selectgroup2()
        self.send_preservation1()
        pass

class Groupmanagement(GroupmanagementPage):
    def groupmanagement(self, groupname):
        self.send_groupmanagent()
        self.send_addgroup()
        self.send_groupname(groupname)
        self.send_preservation2()
        pass

class Filemanagement(FilemanagementPage):
    def filemanagement(self,newtitle):
        self.send_filemanagement()
        self.send_clickmodify()
        self.send_newtitle(newtitle)
        self.send_determine()
        pass