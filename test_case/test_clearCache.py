import logging
import unittest
from businessView.accountSetup.clearCache import ClearCache
from common.login import Login
from common.myunit import StartEnd
class Test_cache(StartEnd):
    def test_cache(self):
        logging.info('执行清理缓存用例')
        lo = Login(self.driver)
        lo.login()
        cache = ClearCache(self.driver)
        logging.info('开始清理缓存')
        self.assertEqual(cache.clear(),'0.0M',msg='用例执行失败，缓存清理不成功')

if __name__ == '__main__':
    unittest.main()
