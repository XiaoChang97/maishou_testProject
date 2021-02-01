from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from baseView.baseView import BaseView
import logging
import time
class AddressManage(BaseView):
    # 登录之后页面
    laMy = (By.ID, 'com.chan.iamabuyer:id/layoutMy')  # 我的元素
    downLine = (By.ID, 'com.chan.iamabuyer:id/confirmButton')  # 当有其他设备登录挤下线的弹窗确定按钮元素
    # setIcon = (By.XPATH,'//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')
    setIcon = (By.XPATH, '//android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ImageView')

    # 账户设置页
    addressManage = (By.ID, 'com.chan.iamabuyer:id/addrassManager')  # 地址管理

    # 收货地址
    addressBack = (By.ID, 'com.chan.iamabuyer:id/back')  # 返回
    search = (By.ID, 'com.chan.iamabuyer:id/menuIv_search')  # 搜索按钮
    newaddress = (By.ID, 'com.chan.iamabuyer:id/rel_add_address_bg')  # 新建地址按钮
    amend = (By.ID, 'com.chan.iamabuyer:id/relChang')  # 修改地址按钮
    name1 = (By.ID,'com.chan.iamabuyer:id/tvName')      #地址栏中名字的元素
    address = (By.ID,'com.chan.iamabuyer:id/tvAddress') #地址栏中地址的元素
    phone1 = (By.ID,'com.chan.iamabuyer:id/tvPhone')    #地址栏中号码的元素

    #新增地址页面
    name = (By.ID,'com.chan.iamabuyer:id/editName')
    phone = (By.ID,'com.chan.iamabuyer:id/editPhone')
    region = (By.ID,'com.chan.iamabuyer:id/tVAddress')      #所在地区
    detailaddress = (By.ID,'com.chan.iamabuyer:id/editDetailAddress')   #详细地址
    save = (By.ID,'com.chan.iamabuyer:id/tv_menu')

    #地区选择
    confirm = (By.ID,'com.chan.iamabuyer:id/btnSubmit')     #确定
    cancel = (By.ID,'com.chan.iamabuyer:id/btnCancel')      #取消

    #删除地址
    delete = (By.XPATH,'//android.widget.TextView[@text="删除"]')            #删除按钮
    confirm1 = (By.ID,'com.chan.iamabuyer:id/confirmButton')        #删除提示框确认
    cancel1 = (By.ID,'com.chan.iamabuyer:id/cancelButton')          #删除提示框取消

    #设为默认
    default = (By.ID,'com.chan.iamabuyer:id/setMoren')

    # 新增地址
    def addDddress(self,consignee,phoneNum,detailedAddress):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.addressManage).click()
        logging.info('进入收货地址页面')
        time.sleep(2)
        number = len(self.driver.find_elements(*self.name1))
        logging.info('地址数量为：%d',number)
        self.driver.find_element(*self.newaddress).click()
        self.driver.find_element(*self.name).send_keys(consignee)
        self.driver.find_element(*self.phone).send_keys(phoneNum)
        self.driver.find_element(*self.region).click()
        self.driver.find_element(*self.confirm).click()
        self.driver.find_element(*self.detailaddress).send_keys(detailedAddress)
        self.driver.find_element(*self.save).click()
        number1 = len(self.driver.find_elements(*self.name1))
        try:
            self.driver.find_element(*self.newaddress)
        except NoSuchElementException:
            logging.error('新增地址出错，未新增成功')
            self.getScreenShot('新增地址')
            return False
        else:
            if number < number1:
                logging.info('新增后地址数量为：%d', number1)
                return True
            else:
                self.getScreenShot('新增地址')
                logging.error('新增地址有误')
                return False

    #删除地址
    def subDddress(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.addressManage).click()
        logging.info('进入收货地址页面')
        time.sleep(2)
        number = len(self.driver.find_elements(*self.name1))
        logging.info('地址数量为：%d', number)
        self.addressLeft()              #滑动收货地址
        self.driver.find_element(*self.delete).click()
        self.driver.find_element(*self.confirm1).click()
        number1 = len(self.driver.find_elements(*self.name1))
        try:
            self.driver.find_element(*self.newaddress)
        except NoSuchElementException:
            logging.error('删除地址出错，未删除成功')
            self.getScreenShot('删除地址')
        else:
            if number > number1:
                logging.info('删除地址后地址数量为：%d', number1)
                return True
            else:
                logging.error('地址未删除成功')
                self.getScreenShot('删除地址')
                return False

    #将最后一个地址设为默认
    def defaDddress(self):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.addressManage).click()
        logging.info('进入收货地址页面')
        time.sleep(2)
        list1 = self.driver.find_elements(*self.name1)         #地址列表各地址名字的元素内容
        nameNumber = len(list1)
        xingming = list1[(nameNumber-1)].text
        list2 = self.driver.find_elements(*self.address)  # 地址列表各地址详细地址的元素内容
        addressNumber = len(list2)
        dizhi = list2[(addressNumber - 1)].text
        list3 = self.driver.find_elements(*self.phone1)  # 地址列表各地址手机号码的元素内容
        phoneNumber = len(list3)
        haoma = list3[(phoneNumber - 1)].text
        logging.info('地址列表最后一个地址姓名：%s  地址：%s   号码：%s', xingming,dizhi,haoma)

        list = self.driver.find_elements(*self.amend)
        list[(len(list) - 1)].click()
        time.sleep(2)
        self.driver.find_element(*self.default).click()
        self.driver.find_element(*self.save).click()

        xingming1 = list1[0].text
        dizhi1 = list2[0].text
        haoma1 = list3[0].text

        logging.info('地址列表默认地址姓名：%s  地址：%s   号码：%s', xingming1,dizhi1,haoma1)

        if xingming1 == xingming and haoma == haoma1:
            return True
        else:
            self.getScreenShot('默认地址')
            return False

    #修改地址
    def modDddress(self,consignee,phoneNum,detailedAddress):
        self.driver.find_element(*self.laMy).click()
        time.sleep(2)
        self.driver.find_element(*self.setIcon).click()
        self.driver.find_element(*self.addressManage).click()
        logging.info('进入收货地址页面')
        time.sleep(2)
        self.driver.find_element(*self.amend).click()
        time.sleep(2)
        self.driver.find_element(*self.name).clear().send_keys(consignee)
        self.driver.find_element(*self.phone).clear().send_keys(phoneNum)
        self.driver.find_element(*self.detailaddress).clear().send_keys(detailedAddress)
        self.driver.find_element(*self.save).click()
        try:
            self.driver.find_element(*self.newaddress)
        except NoSuchElementException:
            logging.error('修改地址出错')
            self.getScreenShot('修改地址')
            return False
        else:
            return True
