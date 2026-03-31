#!-*- coding: utf-8 -*-
import json 
import requests
import os

import xlwt

class json_util:
    ''' 
    功能：json文件操作；
    参数：文件路径,字符串类型；
    '''
    def __init__(self,file):
        self.file = file


    '''
    功能：读取json文件；
    返回值：Dict；
    '''
    def readJson(self):
        with open(self.file) as fp:
            data = json.load(fp)
        return json.loads(json.dumps(data,indent=2,sort_keys=True))


    '''
    功能：根据Key获取Value；
    参数：Json Key；
    返回值：value；
    '''
    def get_value(self, key):
        data = self.readJson()
        return data[key]


    '''
    功能：覆盖Json文件，往Json文件写入数据,没有文件就会新建一个;
    参数：data，字典类型（dict），需要写入的内容；
    '''
    def override_json(self,data):
        with open(self.file,'w') as fp:
            fp.write(json.dumps(data,indent=2,sort_keys=True))


    '''
    功能：更新Json文件;
    参数：data，字典类型（dict），需要更新的内容；
    '''
    def update_json(self,data):
        oldData = self.readJson()
        oldData.update(data)
        with open(self.file,'w') as fp:
            fp.write(json.dumps(oldData,indent=2,sort_keys=True))


# if __name__ == "__main__":
    # jsonFilePath = os.path.abspath("..") + '/test/data.json'
    # json_obj = json_util(jsonFilePath)
    # new_data = {
    #             "add": "add",
    #             "app_type": "newSTAFF"
    #             }
    # json_obj.update_json(new_data)
    # print json_obj.readJson()
    # json_obj.override_json(new_data)
    # print json_obj.readJson()
    # print json_obj.get_value("add")