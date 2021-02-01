from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from businessView.loginView import LoginView
from common.myunit import StartEnd
import unittest
import logging

class TestLogin(StartEnd):
    laMy = (By.ID, 'com.chan.iamabuyer:id/layoutMy')  # 我的元素
    csv_file = '../data/account.csv'

    #正确账号
    #@unittest.skip("正确账号")  # 跳过此条用例，skip跳过的意思
    def test_login_ok(self):
        self.driver.launch_app()
        lo = LoginView(self.driver)
        data = lo.get_csv_data(self.csv_file,1)
        #检测当前是否为登录状态
        try:
            self.driver.find_element(*self.laMy)
        except NoSuchElementException:
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertTrue(lo.login_status(), msg='正确用例登录失败')
        else:
            logging.info('当前app处于已登录状态，开始退出登录')
            lo.exitAccount()
            logging.info('执行登录账号%s，密码%s 的用例', data[0],data[1])
            lo.login_action(data[0], data[1])
            self.assertTrue(lo.login_status(),msg='正确用例登录失败')
        self.driver.close_app()

    # 密码错误
    #@unittest.skip('密码错误')
    def test_login_error01(self):
        self.driver.launch_app()
        lo = LoginView(self.driver)
        data = lo.get_csv_data(self.csv_file,2)
        try:
            self.driver.find_element(*self.laMy)
        except NoSuchElementException:
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(),msg='密码错误用例')
        else:
            logging.info('当前app处于已登录状态，开始退出登录')
            lo.exitAccount()
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(), msg='密码错误用例')
        self.driver.close_app()

    #账号不存在
    #@unittest.skip('账号不存在')
    def test_login_error02(self):
        self.driver.launch_app()
        lo = LoginView(self.driver)
        data = lo.get_csv_data(self.csv_file,3)
        try:
            self.driver.find_element(*self.laMy)
        except NoSuchElementException:
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(),msg='账号不存在用例')
        else:
            logging.info('当前app处于已登录状态，开始退出登录')
            lo.exitAccount()
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(), msg='账号不存在用例')
        self.driver.close_app()

    #账号不足11位
    #@unittest.skip('账号不足11位')
    def test_login_error03(self):
        self.driver.launch_app()
        lo = LoginView(self.driver)
        data = lo.get_csv_data(self.csv_file,4)
        try:
            self.driver.find_element(*self.laMy)
        except NoSuchElementException:
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(),msg='账号不存在用例')
        else:
            logging.info('当前app处于已登录状态，开始退出登录')
            lo.exitAccount()
            logging.info('执行登录账号%s，密码%s 的用例', data[0], data[1])
            lo.login_action(data[0], data[1])
            self.assertFalse(lo.login_status(), msg='账号不存在用例')
        self.driver.close_app()



if  __name__=='__main__':
    unittest.main()

