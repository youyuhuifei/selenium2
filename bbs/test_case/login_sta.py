from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    """社区登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名密码为空'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login5(self):
        '''用户名密码正确'''
        self.user_login_verify(username="zhangsan", password="123456")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '张三')
        function.insert_img(self.driver, "user_pawd_turn,jpg")

    if __name__ == "__main__":
        unittest.main()
