from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from baseView.baseView import BaseView
import logging
import time

#账户设置中的个人信息
class PerInformation(BaseView):
    # 登录之后页面
    laMy = (By.ID, 'com.chan.iamabuyer:id/layoutMy')  # 我的元素
    downLine = (By.ID, 'com.chan.iamabuyer:id/confirmButton')  # 当有其他设备登录挤下线的弹窗确定按钮元素
    # setIcon = (By.XPATH,'//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')
    setIcon = (By.XPATH, '//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')

    #账户设置页
    information = (By.ID,'com.chan.iamabuyer:id/personal_info')     #个人信息元素

    #个人信息页
    #portrait = (By.ID,'com.chan.iamabuyer:id/nex')       #头像元素
    portrait = (By.ID, 'com.chan.iamabuyer:id/modifyHead')  #修改头像元素
    sex = (By.ID,'com.chan.iamabuyer:id/tv_gander')         #性别
    birthday = (By.ID,'com.chan.iamabuyer:id/rel_birthday_bg')  #生日
    city = (By.ID, 'com.chan.iamabuyer:id/rel_city_bg')         #城市

    #点击修改头像后
    photos = (By.ID, 'com.chan.iamabuyer:id/btn_camera')        #拍照
    photosalbum = (By.ID, 'com.chan.iamabuyer:id/btn_pictures') #相册
    unselect =  (By.ID, 'com.chan.iamabuyer:id/btn_cancel')   #取消

    #进入头像设置
    affirm = (By.ID,'com.coloros.gallery3d:id/action_apply')      #确认

    #修改性别页面
    man = (By.ID,'com.chan.iamabuyer:id/relZhiNan')
    woman = (By.ID,'com.chan.iamabuyer:id/relMengmei')
    save = (By.ID,'com.chan.iamabuyer:id/saveBtn')
    back = (By.ID,'com.chan.iamabuyer:id/back')

    # 邀请码
    copy = (By.ID,'com.chan.iamabuyer:id/btn_copy')
    invitationCode = (By.ID,'com.chan.iamabuyer:id/tv_inviteCode')

    #设置头像打开相机
    def openCamear(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        self.driver.find_element(*self.portrait).click()
        logging.info('启动相机')
        self.driver.find_element(*self.photos).click()

    # 设置头像使用相册
    def hendPortrait(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        self.driver.find_element(*self.portrait).click()
        logging.info('打开相册')
        self.driver.find_element(*self.photosalbum).click()
        self.photoSalbum()          #调用方法通过坐标来定位选择图片
        self.find_element(*self.affirm).click()
        try:
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_id('com.chan.iamabuyer:id/modifyHead'))
        except BaseException as e:           #所有基本异常
            self.getScreenShot('修改头像')
            logging.error('头像修改失败')
            return False
        else:
            logging.info('头像修改成功')
            return True

     #设置头像取消

    #设置头像取消
    def hendPortrait2(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        self.driver.find_element(*self.portrait).click()
        logging.info('取消修改')
        self.driver.find_element(*self.unselect).click()
        try:
            self.driver.find_element(*self.portrait)
        except NoSuchElementException:
            self.getScreenShot('取消修改头像')
            logging.error('取消头像失败')
            return False
        else:
            logging.info('取消头像成功')
            return True

    #性别选择男
    def sexMan(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        self.driver.find_element(*self.sex).click()
        self.driver.find_element(*self.man).click()
        self.driver.find_element(*self.save).click()
        #time.sleep(2)
        try:
            xingbie = self.driver.find_element(*self.sex)
        except NoSuchElementException:
            self.getScreenShot('性别选择男')
            logging.error('未获取到性别')
        else:
            #logging.info(xingbie.text)
            return xingbie.text

    #性别选择女
    def sexWoman(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        self.driver.find_element(*self.sex).click()
        self.driver.find_element(*self.woman).click()
        self.driver.find_element(*self.save).click()
        # time.sleep(2)
        try:
            xingbie = self.driver.find_element(*self.sex)
        except NoSuchElementException:
            self.getScreenShot('性别选择女')
            logging.error('未获取到性别')
        else:
            # logging.info(xingbie.text)
            return xingbie.text

    #设置性别不选择，返回
    def sexReturn(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.information).click()
        time.sleep(2)
        xingbie = []
        xingbie.append(self.driver.find_element(*self.sex).text)
        logging.info(xingbie[0])
        self.driver.find_element(*self.sex).click()
        self.driver.find_element(*self.back).click()
        # time.sleep(2)
        try:
            self.driver.find_element(*self.sex)
        except NoSuchElementException:
            self.getScreenShot('返回性别选择')
            logging.error('未回到个人信息页')
        else:
            xingbie.append(self.driver.find_element(*self.sex).text)
            return xingbie

