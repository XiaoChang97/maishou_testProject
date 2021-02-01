from common.login import Login
from common.myunit import StartEnd
from businessView.accountSetup.perInformation import PerInformation
import unittest
import time
from selenium.webdriver.common.by import By
import logging
class TestPerInformation(StartEnd):

    #打开相机
    @unittest.skip('打开相机')
    def test_openCamear(self):
        logging.info('开始执行打开相机用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        per.openCamear()

    #设置头像打开相册
    @unittest.skip('打开相册')
    def test_hendPortrait(self):
        logging.info('开始执行打开相册用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        self.assertTrue(per.hendPortrait(),msg='用例执行失败')

    #设置头像取消
    @unittest.skip('取消设置')
    def test_hendPortrait2(self):
        logging.info('开始执行设置头像取消用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        logging.info('头像设置取消')
        self.assertTrue(per.hendPortrait2(), msg='用例执行失败')

    #选择性别男
    @unittest.skip('修改性别男')
    def test_sexMan(self):
        logging.info('开始执行将性别修改为男用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        logging.info('将性别设置成男')
        self.assertEqual('男',per.sexMan(),'性别未修改成男，用例执行失败')
        logging.info('修改成功')

    # 选择性别女
    @unittest.skip('修改性别女')
    def test_sexWoman(self):
        logging.info('开始执行讲性别修改为女用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        logging.info('将性别设置成女')
        self.assertEqual('女',per.sexWoman(),'性别未修改成女，用例执行失败')
        logging.info('用例通过，修改成功')

    #不修改性别，进入性别页面返回
    @unittest.skip('修改性别页面返回')
    def test_sexWoman(self):
        logging.info('开始执行修改性别返回用例')
        lo = Login(self.driver)
        lo.login()
        per = PerInformation(self.driver)
        logging.info('进入性别页面，返回不修改')
        sex = per.sexReturn()
        self.assertEqual(sex[0],sex[1],'性别有改变，用例执行失败')
        logging.info('用例通过')

if __name__ == '__main__':
    unittest.main()