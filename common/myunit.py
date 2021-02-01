import logging
import unittest
import warnings

from baseView.desired_caps import appium_desired


class StartEnd(unittest.TestCase):   #定义一个类，继承unittest框架中的TestCase基类，用来给测试用例继承初始化和关闭
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)  # 可以通过warnings库来忽略掉相关告警。
        logging.info('开始启动')
        cls.driver = appium_desired()

    @classmethod
    def tearDownClass(cls):
        logging.info('结束')
        cls.driver = appium_desired()
'''
    def setUp(self):                #setUp()方法中进行测试前的初始化工作
        warnings.simplefilter("ignore", ResourceWarning)     #可以通过warnings库来忽略掉相关告警。
        logging.info('启动')
        self.driver = appium_desired()
    def tearDown(self):             #teardown()方法中执行测试后的清除工作，它们都是TestCase中的方法
        logging.info('结束')
        self.driver.quit()

'''