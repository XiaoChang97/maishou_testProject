import logging

from selenium.common.exceptions import NoSuchElementException

from baseView.desired_caps import appium_desired
from businessView.loginView import LoginView

#实现登录流程的类
class Login(LoginView):
    csv_file = '../data/account.csv'
    def login(self):
        lo = LoginView(self.driver)
        data = lo.get_csv_data(self.csv_file,1)
        try:
            self.driver.find_element_by_id("com.chan.iamabuyer:id/layoutMy")
        except NoSuchElementException:
            lo.login_action(data[0], data[1])
            logging.info('开始登录账号%s，密码%s', data[0], data[1])
        else:
            lo.login_action(data[0], data[1])

if __name__ == '__main__':
    driver = appium_desired()
    lo = Login(driver)
    lo.login()