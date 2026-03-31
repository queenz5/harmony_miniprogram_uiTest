from os import path
from devicetest.core.test_case import TestCase, Step
from hypium import *
from hypium.model import WindowFilter
from hypium import host, CV
from hypium.model import KeyCode, UiParam, MatchPattern
from hypium import BY
from aw.commonUtils import *
from numpy.distutils.log import debug

DEFAULT_IDLE_TIME = 0.7
DEFAULT_SLIDE_TIME = 0.3
DEFAULT_TIMEOUT = 10
DEFAULT_similarity = 0.8
bundleId = 'com.xxx.finosprite'
demoAppid = '617270d176abb100010e79b3'
apiServer = 'https://xxx-testing.xxx.club'

class driver_util:
        call_count = 4
        def __init__(self,driver):
            self.driver = driver
        """
        startApplet=True 启动APP，并输入小程序id和页面路径，并打开到指定的页面
        startApplet=False 启动APP并初始化SDK，不打开小程序
        initSdk=True 是否初始化SDK，默认是 True
        """
        def init_app(self,pathAndQuery='',appId=demoAppid,apiServer=apiServer,startApplet=True, startType='hot',initSdk=True):
            # 统计被调用的次数，达到5次执行一次APP冷启动
            driver_util.call_count += 1
            if driver_util.call_count == 5 or startType == 'cold':
                self.driver.stop_app(bundleId)
                driver_util.call_count = 0

            if startApplet:
                if pathAndQuery == '':
                    startParams = f"--ps uiTest true --ps appId {appId} --ps apiServer {apiServer} --ps shortCutKey startApplet"
                else:
                    pathAndQuery = pathAndQuery.replace("&", "\\&")
                    startParams = f"--ps uiTest true --ps appId {appId} --ps apiServer {apiServer} --ps pathAndQuery {pathAndQuery} --ps shortCutKey startApplet"
            else:
                if initSdk:
                    startParams = f"--ps uiTest true --ps apiServer {apiServer}"
                else:
                    startParams=""
            # 类似鸿蒙 hdc 启动 ：hdc shell aa start -a EntryAbility -b com.xxx.finosprite --ps appId 617270d176abb100010e79b3 --ps apiServer https://xxx-testing.xxx.club --ps pathAndQuery "/pages/component/text/text?name=text\&pzq=123" --ps uiTest true --ps shortCutKey startApplet
            self.driver.start_app(package_name=bundleId, page_name="EntryAbility", params=startParams)

        def check_image_exist(self, image_path_pc: str, expect_exist: bool = True, similarity: float = DEFAULT_similarity,timeout: int = 3, mode="template", **kwargs):
            return self.driver.check_image_exist(image_path_pc, expect_exist,similarity,timeout, mode)

        def find_image(self, image_path_pc: str, mode="sift"):
            return self.driver.find_image(image_path_pc,mode)

        def touch_image(self, image_path_pc: str, mode: str = "normal", similarity: float = DEFAULT_similarity, wait_time: int = 0.1,**kwargs):
            return self.driver.touch_image(image_path_pc, mode,similarity,wait_time)

if __name__ == '__main__':
    print("test")

