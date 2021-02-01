
import logging
import random

from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from baseView.desired_caps import appium_desired


#注册类
class RegisterView(BaseView):
    #注册之前页面
    loginBtn = (By.ID,'com.chan.iamabuyer:id/btn_login')    #登录按钮
    register = (By.ID,'com.chan.iamabuyer:id/btn_register')  #注册按钮

    #邀请码
    inviteIput = (By.ID,'com.chan.iamabuyer:id/edit_invitation_code')       #邀请码输入
    nextBt = (By.ID,'com.chan.iamabuyer:id/btn_next_step')      #下一步按钮
    inviteWhat = (By.ID,'com.chan.iamabuyer:id/btn_whatCode')   #什么是邀请码

    #注册页面
    phoneIput = (By.ID,'com.chan.iamabuyer:id/edit_tel_num_tip')        #手机号码输入框
    verCode = (By.ID,'com.chan.iamabuyer:id/edit_verification_code')    #验证码输入框
    getverCode = (By.ID,'com.chan.iamabuyer:id/tv_btn_verification_code')   #获取验证码按钮
    pwdInut = (By.ID,'com.chan.iamabuyer:id/edit_pwd')                     #密码输入框
    nextBt2 = (By.ID,'com.chan.iamabuyer:id/btn_next_step')                 #下一步
    regist = (By.ID,'buy-btn')          #注册商品H5页面立即购买

    #成功注册流程
    def Register(self,invite,phone,pwd):
        self.check_jurisdiction()
        logging.info('开始注册')
        try:
            self.driver.find_element(*self.register)
        except NoSuchElementException:
            logging.error('进入注册页面失败')
            self.getScreenShot('进入注册页面')
        else:
            self.driver.find_element(*self.register).click()
            logging.info('注册页面')
        self.driver.find_element(*self.inviteIput).send_keys(invite)   #验证码
        self.driver.find_element(*self.nextBt).click()     #下一步
        logging.info('邀请码：%s，注册号码：%s',invite,phone)
        self.driver.find_element(*self.phoneIput).send_keys(phone)
        self.driver.find_element(*self.verCode).send_keys('123')
        self.driver.find_element(*self.pwdInut).send_keys(pwd)
        self.driver.find_element(*self.nextBt2).click()

        #presence_of_element_located判断某个元素中的text是否包含了预期的字符串

        toast = WebDriverWait(driver, 5, 0.1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@text=\'{}\']'.format("请先获取验证码"))))
        print(toast)
        logging.error(toast)

if __name__ == '__main__':
    driver = appium_desired()
    re = RegisterView(driver)
    re.Register('1o46l056',str(random.randint(15100000000,15199999999)),'123456xiao')
    #lo.login_action2()

