'''
1.从memo_info.py中获取info_1的定义
2.从memo_head.py中获取head的定义,从memo_cut.py中获取cut_send的定义
3.将head，info_1，cut_send拼接起来，中间用换行符连接，赋值给变量print_1
4.将print_1的值转换为base64编码，如遇汉字则先转化为gbk编码，再转换为base64编码，赋值给变量print_send
'''
# 导入memo_info.py中的变量
from memo_info import info_1
# 导入memo_head.py中的变量
from memo_head import head
# 导入memo_cut.py中的变量
from memo_cut import cut_send
# 导入base64模块
import base64
# 将head和info_1拼接起来，中间用换行符连接，赋值给变量print_1
print_1 = head + '\n' + info_1 + '\n' + '\n' + cut_send
# 将print_1的值转换为base64编码，如遇汉字则先转化为gbk编码，再转换为base64编码
print_send_1 = base64.b64encode(print_1.encode('gbk'))
# 将print_send_1转化为string形式，存入print_send
print_send = str(print_send_1,'utf-8')
# 打印print_send的值
print(print_send_1)
print(print_send)