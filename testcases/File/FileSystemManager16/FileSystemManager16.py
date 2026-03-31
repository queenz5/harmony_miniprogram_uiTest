# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class FileSystemManager16(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/FileSystemManager/writefile?testCase=unlink)')
        self.hypiumUtil.init_app( "packageAPI/pages/FileSystemManager/writefile?testCase=unlink")

    def process(self):
        Step("测试用例：\n\
            case34:FileSystemManager.unlink删除文件成功\n\
            case35:FileSystemManager.unlinkSync删除文件成功\n\
            ")
        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("unlink/unlinkSync_success"))
            if checkComponent:
                break
            else:
                sleep(1)
        self.driver.check_component_exist(BY.text("unlink/unlinkSync_success"))

    def teardown(self):
        Step('结束')

