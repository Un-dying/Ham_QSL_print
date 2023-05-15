'''
1.弹出一个50行的输入框
2.提示在输入框中输入内容
3.将输入内容转换为base64编码，如果为汉字，需要先转换为gbk编码
4.将转换的内容存储到变量aa中
'''
# 导入base64模块
import base64
# 导入easygui模块
import easygui as g
# 弹出一个50行的输入框
msg = '请输入打印内容'
title = '打印内容'
# 提示在输入框中输入内容
p_content = g.enterbox(msg,title,strip=True)
# 将输入内容转换为base64编码，如果为汉字，需要先转换为gbk编码
p_content = base64.b64encode(p_content.encode('gbk'))
# 将转换的内容存储到变量aa中
aa = str(p_content,'utf-8')
# 打印aa的值
print(aa)