from common.login import Login
from common.myunit import StartEnd
from businessView.accountSetup.aboutUs import AboutUs
import unittest
import logging
class TestAboutUs(StartEnd):
    def test_about(self):
        logging.info('执行关于我是买手')
        lo = Login(self.driver)
        lo.login()
        ab = AboutUs(self.driver)
        ab.about()

if __name__ == '__main__':
    unittest.main()