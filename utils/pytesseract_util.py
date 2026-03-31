# -*- encoding=utf8 -*-
__author__ = "ftjk-peng"

import os
from PIL import Image
import pytesseract
import random
import string
from paddleocr import PaddleOCR
import random
import string


"""
图片转文字函数：
:param root_dir: 传调用方当前文件所在的路径，可以通过这样获取：root_dir = os.path.dirname(__file__)
:eccpect_text:需要校验的字符串
:lang:语言，默认是英文"eng"，简体中文是chi_sim，繁体中文是chi_tra
:return: isExits(目标字符串是否出现在图片上，值是true或者false)、text（识别到图片内的文所有文字）、count（目标字符串出现的次数）
"""
def find_text_in_screen_pytesseract(driver,eccpect_text,lang="eng"):
  screenshot_filename = "reports/screenShot/"+generate_random_string()+"_screenshot.jpeg"
  screenshot_path = driver.capture_screen(screenshot_filename,True)
  if(os.access(screenshot_path, os.F_OK)):
    im = Image.open(screenshot_path)
    text = pytesseract.image_to_string(im, lang=lang)
    if(eccpect_text in text):
        isExits=True
        count = text.count(eccpect_text)
    else:
        isExits=False
        count=0
    return {'isExits': isExits, 'text': text,'count': count}
  else:
     print("截图图片路径错误:",screenshot_path)



"""
识别图片中目标文案的坐标：
:param root_dir: 传调用方当前文件所在的路径，可以通过这样获取：root_dir = os.path.dirname(__file__)
:target_text:需要点击的字符串
:lang:语言，默认是英文"en"，支持['ch', 'en', 'korean', 'japan', 'chinese_cht', 'ta', 'te', 'ka', 'latin', 'arabic', 'cyrillic', 'devanagari']
"""
def find_text_in_screen_PaddleOCR(driver,target_text,lang="en",target_text_index=1) :
    #截屏
    screenshot_filename = "reports/screenShot/"+generate_random_string()+"_screenshot.jpeg"
    screenshot_path = driver.capture_screen(screenshot_filename,True)
    # image_compression(screenshot_path)  #图片压缩
    if(os.access(screenshot_path, os.F_OK)):
        ocr = PaddleOCR(use_angle_cls=True, lang=lang,use_gpu=False)
        ocr_result = ocr.ocr(screenshot_path, cls=True)
        text = str(ocr_result)
        if(target_text in text):
            isExits=True
            count = text.count(target_text)
            n = 0
            # 遍历识别结果，找到目标文字的坐标
            target_coords = None
            for line in ocr_result:
                for word_info in line:
                    # 获取识别结果的文字信息
                    if target_text in word_info[1][0]:
                        # 获取文字的坐标（中心点）
                        x1, y1 = word_info[0][0]
                        x2, y2 = word_info[0][2]
                        target_coords = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                        n += 1
                        if n == target_text_index:
                            break
                if target_coords:
                    break
            return {'isExits': isExits, 'text': text,'count': count,'target_coords':target_coords}
        else:
            isExits=False
            count=0
            target_coords= None
            return {'isExits': isExits, 'text': text,'count': count,'target_coords':target_coords}
    else:
      print("截图路径错误:",screenshot_path)

def generate_random_string(length=5):
    """
    生成一个指定长度的随机字符串，包含大小写字母和数字。
    :param length: 字符串的长度，默认为5。
    :return: 一个随机字符串。
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# 图片压缩
def image_compression(image_path, base_width=360, save_path=None):
    img = Image.open(image_path)
    if img.width > base_width:
        w_percent = base_width / float(img.width)
        h_size = int((float(img.height) * float(w_percent)))
        # 兼容 Pillow 新旧版本
        try:
            img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        except AttributeError:
            img = img.resize((base_width, h_size), Image.ANTIALIAS)
        if save_path:
            img.save(save_path)
        else:
            img.save(image_path)

 
if __name__ == '__main__':
  print("")
  ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=False)
  ocr_result = ocr.ocr("123.jpeg", cls=True)
  print("---------------",ocr_result)
