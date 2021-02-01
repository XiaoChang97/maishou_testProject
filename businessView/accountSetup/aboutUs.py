from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
import time
import logging

from baseView.desired_caps import appium_desired


class AboutUs(BaseView):
    # 登录之后页面
    laMy = (By.ID, 'com.chan.iamabuyer:id/layoutMy')  # 我的元素
    downLine = (By.ID, 'com.chan.iamabuyer:id/confirmButton')  # 当有其他设备登录挤下线的弹窗确定按钮元素
    setIcon = (By.XPATH, '//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')

    #账户页面
    about1 = (By.ID,'com.chan.iamabuyer:id/about_app')     #关于我是买手

    def about(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        time.sleep(2)
        self.driver.find_element(*self.about1).click()
