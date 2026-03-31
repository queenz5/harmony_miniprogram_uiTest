#!-*- coding: utf-8 -*-
import time
from datetime import date, datetime
# pip3 install python-dateutil
from dateutil.relativedelta import relativedelta

class TimeUtil:
  '''
  处理日期时间
  '''

  def __init__(self) -> None:
    pass
  
  def time_strf(format_str="%Y-%m", suff=""):
    """根据给定模板返回时间字符串

    Args: 
      format_str -- 接受一个格式化模板(缺省: '%Y-%m'), 参考:
      https://docs.python.org/zh-cn/3/library/datetime.html#strftime-and-strptime-format-codes
      suff -- 后缀字符

    Return:
      返回一个字符串.eg:

      '2022-06'
    """
    return time.strftime(format_str) + suff

  def datetime_strp(date_str, format_str):
    """根据给定模板返回一个datetime object
    
    Args: 
      date_str -- 接受一个日期字符串(eg: '2022-06-01')
      format_str -- 接受一个格式化模板

    Return:
      返回一个datetime对象.
    """
    return datetime.strptime(date_str, format_str)

  def relative_delta(origin_date, y, m):
    """计算相对日期
    https://dateutil.readthedocs.io/en/stable/relativedelta.html
    """
    return origin_date + relativedelta(years=y) + relativedelta(months=m)