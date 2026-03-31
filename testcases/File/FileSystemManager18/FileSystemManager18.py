# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class FileSystemManager18(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/FileSystemManager/writefile?testCase=unzip)')
        self.hypiumUtil.init_app( "packageAPI/pages/FileSystemManager/writefile?testCase=unzip")

    def process(self):
        Step("case38:FileSystemManager.unzip解压文件成功")
        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("unzip_success"))
            if checkComponent:
                break
            else:
                sleep(1)
        self.driver.check_component_exist(BY.text("unzip_success"))

    def teardown(self):
        Step('结束')

