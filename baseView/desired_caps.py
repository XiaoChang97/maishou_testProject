from appium import webdriver
import yaml
import logging.config
import os

CON_LOG = '../config/log.conf'

logging.config.fileConfig(CON_LOG)
#模拟器
def appium_desired():
    #file = open('../config/ms_caps.yaml','r',encoding='utf-8')这种打开文件的
    #这打开文件的好处是，如果出现异常，读取过程中文件不存在或异常，执行到末尾一样会关闭文件
    with open('../config/ms_caps.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file)
    # 获取的yaml数据转换过来是字典类型，data[键值对]
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']['xiaoyao']
    desired_caps['deviceName'] = data['deviceName']['xiaoyao']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['app'] = data['appname']
    #desired_caps['automationName'] = data['automationName']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']  # 使用unicode输入法,可以输入中文
    desired_caps['resetKeyboard'] = data['resetKeyboard']  # 重置输入法到初始状态
    desired_caps['noReset'] = data['noReset']  # true启动app时不要清除app里的原有的数据,false清除
    # 将获取的ip和端口用str方法转换成字符串类型
    logging.debug('开始启动app')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver

#oppo真机
def appium_desired_oppo():
    #file = open('../config/ms_caps.yaml','r',encoding='utf-8')这种打开文件的
    #这打开文件的好处是，如果出现异常，读取过程中文件不存在或异常，执行到末尾一样会关闭文件
    with open('../config/ms_caps.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file)
    # 获取的yaml数据转换过来是字典类型，data[键值对]
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']['oppo']
    desired_caps['deviceName'] = data['deviceName']['oppo']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    #desired_caps['app'] = data['appname']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']   # 使用unicode输入法,可以输入中文
    desired_caps['resetKeyboard'] = data['resetKeyboard']  # 重置输入法到初始状态
    desired_caps['noReset'] = data['noReset']  # true启动app时不要清除app里的原有的数据,false清除
    # 将获取的ip和端口用str方法转换成字符串类型
    logging.info('开始启动app')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver


if __name__=='__main__':
   appium_desired()
    #appium_desired_oppo()
   #base_dir = os.path.dirname(os.path.dirname(__file__))
   #print(os.path.dirname(__file__))
   #print(base_dir)
   #app_path = os.path.join(base_dir,'app','data[appname]')
   #print(app_path)
