# coding: utf-8
import time

from aw.hypiumUtils import *
from aw.commonUtils import *
from hypium import host, CV


class image(TestCase):
    def __init__(self, controllers):
        self.TAG = self.__class__.__name__
        TestCase.__init__(self, self.TAG, controllers)
        self.driver = UiDriver(self.device1)
        self.hypiumUtil = driver_util(self.driver)

    def setup(self):
        Step('启动APP，跳转到指定的小程序和指定的页面')
        self.hypiumUtil.init_app( "/pages/component/image/image")

    def process(self):
        Step('case1:image组件，mode为空，src传网络图片样式检测')
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815172044.jpeg", True)

        Step('case2:image组件，mode为空，src传本地图片样式检测')
        self.driver.touch(BY.text("next"))
        result = find_text_in_screen(self.driver, "WeChat", lang='en')  # 查找中文 lang='ch'
        host.check_equal(result['isExits'], True, "image组件本地图片没显示出来")

        Step('case3:image组件，mode为scaleToFill，image组件样式测试不保持纵横比缩放图片，使图片完全适应')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815173353.jpeg", True)

        Step('case4:image组件，mode为aspectFit，image组件样式测试保持纵横比缩放图片，使图片的长边能完全显示出来')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815173517.jpeg", True)

        Step('case5:image组件，mode为aspectFill，image组件样式测试保持纵横比缩放图片，只保证图片的短边能完全显示出来')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815173614.jpeg", True)

        Step('case6:image组件，mode为top，image组件样式测试不缩放图片，只显示图片的顶部区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815173933.jpeg", True)

        Step('case7:image组件，mode为bottom，image组件样式测试不缩放图片，只显示图片的底部区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174046.jpeg", True)

        Step('case8:image组件，mode为center')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174139.jpeg", True)

        Step('case8:image组件，mode为left，image组件样式测试不缩放图片，只显示图片的左边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174239.jpeg", True)

        Step('case9:image组件，mode为right，image组件样式测试不缩放图片，只显示图片的右边边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174335.jpeg", True)

        Step('case10:image组件，mode为top left，image组件样式测试不缩放图片，只显示图片的左上边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174432.jpeg", True)

        Step('case11:image组件，mode为top right，image组件样式测试不缩放图片，只显示图片的右上边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174747.jpeg", True)

        Step('case12:image组件，mode为bottom left，image组件样式测试不缩放图片，只显示图片的左下边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815174841.jpeg", True)

        Step('case13:image组件，mode为bottom right，image组件样式测试不缩放图片，只显示图片的右下边区域')
        self.driver.touch(BY.text("next"))
        self.hypiumUtil.check_image_exist("testcases/image/image/20250815175540.jpeg", True)

    def teardown(self):
        Step('结束')

