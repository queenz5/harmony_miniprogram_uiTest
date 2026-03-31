# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class FileSystemManager5(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/FileSystemManager/writefile?testCase=copy)')
        self.hypiumUtil.init_app( "packageAPI/pages/FileSystemManager/writefile?testCase=copy")

    def process(self):
        Step("测试用例：\n\
            case11:FileSystemManager.copyFile复制文件成功\n\
            case12:FileSystemManager.copyFileSync复制文件成功\n\
            case13:FileSystemManager.readFile读取本地文件内容成功\n\
            case14:FileSystemManager.readFileSync读取本地文件内容成功\n\
            case15:FileSystemManager.writeFile写文件成功\n\
            case16:FileSystemManager.writeFileSync写文件成功\n\
            ")
        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("copy/copySync_success"))
            if checkComponent:
                break
            else:
                sleep(1)
        self.driver.check_component_exist(BY.text("copy/copySync_success"))
        self.driver.check_component_exist(BY.text("readFile/readFileSync_success"))
        self.driver.check_component_exist(BY.text("writeFile/writeFileSync_success"))

    def teardown(self):
        Step('结束')

