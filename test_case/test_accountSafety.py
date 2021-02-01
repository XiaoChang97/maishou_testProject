from common.login import Login
from common.myunit import StartEnd
from businessView.accountSetup.accountSafety import AccountSafety
import unittest
import logging
class TestAboutUs(StartEnd):
    #未完成
    def test_about(self):
        logging.info('执行账户安全')
        lo = Login(self.driver)
        lo.login()
        ab = AccountSafety(self.driver)
        ab.alterPhone()

if __name__ == '__main__':
    unittest.main()