import unittest
from BSTestRunner import BSTestRunner
from HTMLTestRunnerCN import HTMLTestReportCN
import logging
import time
import sys
path='D:\\maishou_testProject\\'
sys.path.append(path)
import os

test_dir = '../test_case'           #用例路径
#report_dir = os.path.dirname(os.path.dirname(__file__)) + '/report'
report_dir = '../report'           #生成报告路径

#定义报告的文件格式
now = time.strftime("%Y-%m-%d_%H-%M-%S")           #返回以可读字符串表示的当地时间,不可用冒号，文件命名规则不能有冒号
report_name = report_dir + '/' + now + '_test-report.html'

#discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')

#这个方法用来将用例组织起来按顺序执行
def suite():
    suite = unittest.TestSuite()
    # 加载测试用例
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py',top_level_dir=None)
    for testpy in discover:                 #找到测试用例的py文件
        for testcase in testpy:             #找到测试py文件的测试用例
            suite.addTests(testcase)        #测试用例添加到测试套件中
    return suite

#运行用例并生成测试报告
#以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
with open(report_name,'wb') as f:
    runner = HTMLTestReportCN(stream=f,title="我是买手测试用例",description="我是买手app安卓测试用例")
    logging.info('开始启动测试用例...')
    runner.run(suite())

