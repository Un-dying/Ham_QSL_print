'''
1.从memo1.py中获取t_stamp，a_key，md_id的定义
user_id的定义
#2.从memo_cal.py中获取print_send的定义
3.以get方式请求url，url地址为http://open.memobird.cn/home/printpaper?ak=a_key&timestamp=t_stamp&printcontent=T:d3&memobirdID=md_id&userID=user_id
'''
# 导入memo1.py中的变量
from memo1 import t_stamp,a_key,md_id
from memo2 import user_id
# 打印a的值
from memo_cal import print_send
#print(p_content)
# 导入time模块
import time
# 导入requests模块
import requests
# 定义url
url_p = 'http://open.memobird.cn/home/printpaper?ak=%s&timestamp=%s&printcontent=T:%s&memobirdID=%s&userID=%s' % (a_key,t_stamp,print_send,md_id,user_id)
# 发送get请求
r = requests.get(url_p)
# 打印响应内容
print(r.text)
# 打印响应状态码
print(r.status_code)
# 打印响应头
print(r.headers)