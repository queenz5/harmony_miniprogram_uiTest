# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class FileSystemManager10(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/FileSystemManager/writefile?testCase=readdir)')
        self.hypiumUtil.init_app( "packageAPI/pages/FileSystemManager/writefile?testCase=readdir")

    def process(self):
        Step("测试用例：\n\
            case25:FileSystemManager.readdir读取目录内文件列表成功\n\
            case26:FileSystemManager.readdirSync读取目录内文件列表成功\n\
            ")
        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("readdir/readdirSync_success"))
            if checkComponent:
                break
            else:
                sleep(1)
        self.driver.check_component_exist(BY.text("readdir/readdirSync_success"))

    def teardown(self):
        Step('结束')

