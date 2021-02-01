from common.login import Login
from common.myunit import StartEnd
from businessView.accountSetup.addressManage import AddressManage
import unittest
import logging
class TestAddressmanage(StartEnd):
    csv_file = '../data/address.csv'
    #正常新增地址
    #@unittest.skip('增加地址')

    def test_addDddress(self):
        self.driver.launch_app()
        logging.info('开始执行新增地址用例')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file,1)
        self.assertTrue(add.addDddress(data[0],data[1],data[2]),msg = '用例执行失败，地址没有新增')
        self.driver.close_app()

    # 正常删除地址
    #@unittest.skip('删除地址')
    def test_subDddress(self):
        self.driver.launch_app()
        logging.info('开始执行删除地址用例')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        self.assertTrue(add.subDddress(),"用例执行失败，地址没有删除")
        self.driver.close_app()

    #@unittest.skip('默认地址')
    def test_defaDddress(self):
        self.driver.launch_app()
        logging.info('开始执行设置默认地址用例')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        self.assertTrue(add.defaDddress(), msg="用例执行失败，设置默认未完成")
        self.driver.close_app()

    @unittest.skip('修改地址')
    def test_modDddress(self):
        self.driver.launch_app()
        logging.info('开始执行修改地址用例')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        date = add.get_csv_data(self.csv_file,7)
        self.assertTrue(add.modDddress(date[0],date[1],date[2]),msg="用例执行失败，修改地址未完成")
        self.driver.close_app()

    @unittest.skip('异常新增地址，不添加姓名')
    def test_addDddressError(self):
        self.driver.launch_app()
        logging.info('异常新增地址，不添加姓名')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 2)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()

    @unittest.skip('异常新增地址，不添加号码')
    def test_addDddressError1(self):
        self.driver.launch_app()
        logging.info('异常新增地址，不添加号码')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 3)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()

    @unittest.skip('异常新增地址，不添加详细地址')
    def test_addDddressError2(self):
        self.driver.launch_app()
        logging.info('异常新增地址，不添加详细地址')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 4)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()

    @unittest.skip('异常新增地址，手机号码输入中文')
    def test_addDddressError3(self):
        self.driver.launch_app()
        logging.info('异常新增地址，手机号码输入中文')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 5)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()

    @unittest.skip('异常新增地址，手机号码英文')
    def test_addDddressError3(self):
        self.driver.launch_app()
        logging.info('异常新增地址，手机号码英文')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 6)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()

    @unittest.skip('异常新增地址，手机不足11位')
    def test_addDddressError4(self):
        self.driver.launch_app()
        logging.info('异常新增地址，手机不足11位')
        lo = Login(self.driver)
        lo.login()
        add = AddressManage(self.driver)
        data = add.get_csv_data(self.csv_file, 7)
        self.assertFalse(add.addDddress(data[0], data[1], data[2]), msg='用例执行失败，地址新增成功')
        self.driver.close_app()


if __name__ == '__main__':
    unittest.main()