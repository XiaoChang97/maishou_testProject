#基类，将原生的方法都封装一遍，让继承的类去调用
import csv
import logging
import os
from time import sleep, strftime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from baseView.desired_caps import appium_desired

class BaseView(object):
    def __init__(self,driver):          #初始化方法
        self.driver = driver

    def find_element(self,*loc):        #传入可变参数，元素定位的方法
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):        #传入可变参数，元素定位的方法
        return self.driver.find_element(*loc)

    def get_window_size(self):        #获取屏幕大小的方法
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration=None):      #滑动屏幕的方法
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration=None)

    # 获取屏幕大小方法
    def get_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x, y

    loginBtn = (By.ID, 'com.chan.iamabuyer:id/btn_login')  # 登录按钮元素
    jurBtn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')  # 获取权限按钮元素

    #定义一个根据坐标相对定位点击相册照片的方法
    def photoSalbum(self):
        logging.info('调用photosalbum，进行屏幕相对定位点击')
        l = self.get_size()
        self.driver.tap([((l[0] * 0.5), (l[1] * 0.14))], 500)
        sleep(2)
        self.driver.tap([((l[0] * 0.1), (l[1] * 0.14))], 500)

    # 从引导页右往左滑动方法
    # @classmethod
    def swipeLeft(self):
        logging.info('调用swipeLeft滑动引导页')
        l = self.get_size()  # 调用方法获取屏幕大小
        x1 = int(l[0] * 0.9)  # x1点在最右边
        x2 = int(l[0] * 0.1)  # x2点在最左边
        y1 = int(l[1] * 0.5)  # Y1点
        self.swipe(x1, y1, x2, y1, 1000)  # 从右边划向最左边，y轴不变,持续1秒（1000毫秒）

    #删除滑动
    def addressLeft(self):
        logging.info('调用addressLeft滑动地址管理')
        l = self.get_size()  # 调用方法获取屏幕大小
        x1 = l[0] * 0.7      # x1点在最右边
        x2 = l[0] * 0.4      # x2点在最左边
        y1 = l[1] * 0.12     # Y1点
        self.swipe(x1, y1, x2, y1, 1000)  # 从右边划向最左边，y轴不变,持续1秒（1000毫秒）

    # 定义一个接受当前时间的方法，用来做命名
    def getTime(self):
        # 接收以时间元组，并返回以可读字符串表示的当地时间
        self.now = strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    # 定义截屏的方法，已传过来的module参数加上日期命名
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)
        logging.info('获取 %s 截图' % module)
        # get_screenshot_as_file(image_file)是webdriver中的截图方法
        self.driver.get_screenshot_as_file(image_file)

    # 拿account.csv的账户密码
    def get_csv_data(self, csv_file, line):  # 传过来的是文件地址和账户位置
        #logging.info('调用csv文件')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)  # 前面的reader是自定义变量，后面的是方法，读取问文件
            for i, row in enumerate(reader, 1):  # 1为设置初始下标为1
                if i == line:
                    return row  # 返回找到的位置的账号密码内容

    # 定义一个方法，启动页面获取权限，如果没有找到元素就报异常打印没有获取到元素，否则进行点击上
    def check_jurisdiction(self):
        # 因为有写手机打开会有3秒的广告停留，有些手机时间长一点没有写手机时间短一点，所以设置一个隐式等待，在5秒时间内不断扫描元素，全局。
        self.driver.implicitly_wait(5)
        try:
            # self.driver.implicitly_wait(5)
            self.driver.find_element(*self.loginBtn)  # 登录按钮元素
        except NoSuchElementException:
            try:
                logging.info("第一次启动app")
                # 获取权限按钮元素
                ok = self.driver.find_element(*self.jurBtn)
            except NoSuchElementException:
                # sleep(3)  3秒广告
                logging.info("无需手动获取权限，直接滑动引导页")
                for i in range(0, 3):
                    self.swipeLeft()
                    logging.info('第%d次调用向左滑动', i)
                    #                    sleep(0.5)
            else:
                for i in range(0, 2):
                    ok.click()
                    sleep(0.5)
                    # 第一次启动引导页
                    # sleep(3)  # 3秒广告
                for i in range(0, 3):
                    self.swipeLeft()
                    logging.info('第%d次调用向左滑动', i)
                    sleep(0.5)
        else:
            logging.info("获取到登录按钮元素，不是第一次启动")
            # 浏览器前进操作

if __name__=='__main__':
    driver=appium_desired()
    ba = BaseView(driver)
    ba.check_jurisdiction()    #然后调用Commom类中的方法
    #file = '../data/account.csv'
    #ba.get_csv_data(file,1)