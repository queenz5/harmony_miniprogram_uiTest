from xdevice.__main__ import main_process
import shutil
import os
from aw.commonUtils import *

if __name__ == "__main__":
  # 创建报告文件夹
  reports_path = 'reports'
  if os.path.exists(reports_path):
    shutil.rmtree(reports_path)  # 删除整个文件夹及内容
  os.makedirs(reports_path)  # 重新创建空文件夹
  
  # 创建保存报告的文件夹
  folder_path = 'reports/harmonyReports'
  os.makedirs(folder_path)  # 重新创建空文件夹
  
  #创建保存截图的文件夹
  screenShot_path = 'reports/screenShot'
  os.makedirs(screenShot_path)  # 重新创建空文件夹
  
  
  casePath = os.path.dirname(__file__) + '/conf/testcases.conf' # 测试用例文件路径
  caseList = get_case_list(casePath)  #生成测试用例列表，格式为： suit1.case1,suit1.case2,suit2.case1
  # runParame = "run -l tabbar/tabbar/tabbar -ta agent_mode:bin;screenshot:true -rp  harmonyReports"
  runParame = "run -l " + caseList + " -sn 2LQ0223A26014853 -ta agent_mode:bin;screenshot:true -rp  harmonyReports"
  main_process(runParame)


  # 执行testcases下的 Example.py用例
  # main_process("run -l Example/Example/Example -ta agent_mode:bin;screenshot:true")