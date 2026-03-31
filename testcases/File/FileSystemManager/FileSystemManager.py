# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class FileSystemManager(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/FileSystemManager/writefile?testCase=access)')
        self.hypiumUtil.init_app( "packageAPI/pages/FileSystemManager/writefile?testCase=access")

    def process(self):
        Step("测试用例：\n\
            case1:FileSystemManager.access判断本地文件地址temp、store、usr地址判断正确\n\
            case2:FileSystemManager.accessSync判断本地文件地址temp、store、usr地址判断正确\n\
            case3:FileSystemManager.saveFile保存临时文件到本地成功\n\
            case4:FileSystemManager.saveFileSync保存临时文件到本地成功\n\
            ")
        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("access_ok"))
            if checkComponent:
                break
            else:
                sleep(1)

        self.driver.check_component_exist(BY.text("access_ok"))
        self.driver.check_component_exist(BY.text("accessSync_ok"))
        self.driver.check_component_exist(BY.text("saveFile/saveFileSync_success"))

    def teardown(self):
        Step('结束')

