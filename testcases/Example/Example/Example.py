# coding: utf-8
import time

from aw.hypiumUtils import *
from aw.commonUtils import *
from hypium import host, CV


class Example(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面')
        self.hypiumUtil.init_app( "/pages/component/movable/movable?uiTest=yes&testCase=type")

    def process(self):
        Step('测试场景1')
        # self.driver.touch(BY.text("打开小程序"))
        # self.hypiumUtil.check_image_exist("testcases/movable/movable/20250728103530.jpeg", True)
        #
        # Step('测试场景2')
        # result = find_text_in_screen(self.driver, "xxxx", lang='en')  # 查找中文 lang='ch'
        # host.check_equal(result['isExits'], True, "没有找到xxxx")
        # self.driver.touch(result["target_coords"])  # 点击坐标


    def teardown(self):
        Step('结束')

