# coding: utf-8
from aw.hypiumUtils import *
from time import sleep

class file(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面(packageAPI/pages/File/index)')
        self.hypiumUtil.init_app( "packageAPI/pages/File/index")

    def process(self):
        Step("测试用例：\n\
            case1:saveFile保存临时文件到本地成功\n\
            case2:getSavedFileList获取该小程序下已保存的本地缓存文件列表成功\n\
            case3:getSavedFileInfo获取该小程序下已保存的本地缓存文件信息成功\n\
            case4:getFileInfo获取该小程序下的 本地临时文件或本地缓存文件信息成功\n\
            case5:removeSavedFile删除该小程序下已保存的本地缓存文件成功\n\
            ")

        for i in range(10):
            checkComponent = self.driver.find_component(BY.text("saveFile_test_success"))
            if checkComponent:
                break
            else:
                sleep(1)

        self.driver.check_component_exist(BY.text("saveFile_test_success"))
        self.driver.check_component_exist(BY.text("getSavedFileList_test_success"))
        self.driver.check_component_exist(BY.text("getSavedFileinfo_test_success"))
        self.driver.check_component_exist(BY.text("getFileinfo_test_success"))
        self.driver.check_component_exist(BY.text("removeSavedFile_test_success"))


    def teardown(self):
        Step('结束')

