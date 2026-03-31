import sys,os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

from utils.pytesseract_util import *
from utils.ConfigParser_util import ConfigParser_util
import time



# #识别截图中的文字，断言目标文案是否存在，出现次数、截图文案
# def find_text_in_screen(driver,eccpect_text,lang="eng"):
#     return find_text_in_screen_pytesseract(driver,eccpect_text,lang="eng")

#识别截图中的文字，获取目标文案的坐标并点击
def find_text_in_screen(driver,target_text,lang="en",target_text_index=1,wait_time=1) :
    for i in range(wait_time):
        time.sleep(1)
        result = find_text_in_screen_PaddleOCR(driver,target_text,lang,target_text_index)
        if result['isExits']:
            break
    return result

# 返回所有用例名称
def get_case_list(testcaseDir):
        con_obj = ConfigParser_util(testcaseDir)
        return con_obj.format_test_cases()

# 同一个用例，不同手机截图，只要有1张识别通过就算通过
def check_images_exist(driver, image_list, expect_exist):
    for image in image_list:
        check_result = driver.find_image(image)
        if check_result:
            break
    if (check_result and expect_exist) or (not check_result and not expect_exist):
        return
    else:
        assert False, '检测全部图片是否存在与预期不相符'


    
    
if __name__ == '__main__':
    # base_cases_dir = os.path.dirname(__file__)
    # con_obj = ConfigParser_util(base_cases_dir + '/conf/config.conf')   

    configPath = os.path.dirname(__file__) + '/../conf/testcases.conf'
    print(get_case_list(configPath))

