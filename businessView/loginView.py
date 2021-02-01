#coding = utf-8
import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from baseView.baseView import BaseView
from baseView.desired_caps import appium_desired


class LoginView(BaseView):

    #登录之前页面
    loginBtn = (By.ID,'com.chan.iamabuyer:id/btn_login')    #登录按钮
    register = (By.ID,'com.chan.iamabuyer:id/btn_register')  #注册按钮

    # 登录页面
    phone = (By.ID,'com.chan.iamabuyer:id/edit_phone')
    pwd = (By.ID,'com.chan.iamabuyer:id/edit_pwd')
    loginBtn2 = (By.ID, 'com.chan.iamabuyer:id/loginBtn')
    verCode = (By.ID,'com.chan.iamabuyer:id/pwd_login')     #验证码登录链接
    fogetPwd = (By.ID,'com.chan.iamabuyer: id / tv_forgetPwd')  #忘记密码链接
    lookPor = (By.ID,'com.chan.iamabuyer:id/ll_userAgreement')  #查看协议
    visitor = (By.ID,'com.chan.iamabuyer:id/guest_mode')        #游客模式

    # 登录之后页面
    laMy = (By.ID,'com.chan.iamabuyer:id/layoutMy')     #我的元素
    downLine = (By.ID,'com.chan.iamabuyer:id/confirmButton')    #当有其他设备登录挤下线的弹窗确定按钮元素

    # 我的页面设置图标,因为没有唯一属性定位，所以用xpath相对路径
    setIcon = (By.XPATH,'//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')
    exitLogin = (By.ID,'com.chan.iamabuyer:id/btnLoginOut')     #设置里面退出登录按钮
    confirm = (By.ID,'com.chan.iamabuyer:id/confirmButton')     #确认退出中的确定按钮
    cancel = (By.ID,'com.chan.iamabuyer:id/cancelButton')       #确认退出中的取消按钮

    #账号密码登录
    def login_action(self,username,password):
        try:
            self.driver.find_element(*self.laMy)    #此为登录成功后“我的”按钮id属性
        except NoSuchElementException:
            self.check_jurisdiction()               #启动页
            #WebDriverWait(driver,3).until(lambda x:x.find_element_by_id("com.chan.iamabuyer:id/btn_login"))
            logging.info('开始点击登录进入登录页面')
            self.driver.find_element(*self.loginBtn).click()
            self.driver.find_element(*self.phone).send_keys(username)
            self.driver.find_element(*self.pwd).send_keys(password)
            self.driver.find_element(*self.loginBtn2).click()
            #driver.find_element_by_android_uiautomator('new uiSelector().resourceId("com.chan.iamabuyer:id/loginBtn")').click()
            #driver.get_screenshot_as_file('./images/login.jpg')
        else:
            pass

#检测执行完登录后停留在主页的状态
    def login_status(self):
        try:
            self.driver.find_element(*self.laMy)    #此为登录成功后“我的”按钮id属性
        except NoSuchElementException:
            logging.error("账号密码登录失败")
            self.getScreenShot('账号密码登录')
            return False
        else:
            logging.info("登录成功")
            self.exitAccount()          #调用退出账号的方法
            return True

    #游客模式登录
    def login_action2(self):
        self.check_jurisdiction()
        # WebDriverWait(driver,3).until(lambda x:x.find_element_by_id("com.chan.iamabuyer:id/btn_login"))
        self.driver.find_element(*self.loginBtn).click()
        self.driver.find_element(*self.visitor).click()
        try:
            self.driver.find_element(*self.laMy)
        except NoSuchElementException:
            logging.error("游客登录失败")
            self.getScreenShot('游客登录')
        else:
            pass

    #退出账号
    def exitAccount(self):
        logging.info('退出账号')
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.exitLogin).click()
        self.driver.find_element(*self.confirm).click()
        try:
            self.driver.find_element(*self.loginBtn)
        except NoSuchElementException:
            logging.error('退出失败')
            self.getScreenShot('退出')
        else:
            logging.info('退出成功')


    #检测是有否账号下限提示
    def check_account_alert(self):
        try:
            self.driver.find_element(*self.downLine)
        except NoSuchElementException:
            logging.error('没有检测到账号下线提示')
            self.getScreenShot('检测账号下限')


if __name__ == '__main__':
    driver = appium_desired()
    lo = LoginView(driver)
    com = Common(driver)
    #lo.login_action2()