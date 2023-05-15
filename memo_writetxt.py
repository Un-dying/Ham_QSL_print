'''
1.读取1.txt文件中的内容
2.将读取的内容转换为base64编码，如果为汉字，需要先转换为gbk编码
3.将转换后的内容赋值给变量aa
4.打印aa的值
'''
# 导入base64模块
import base64
# 读取1.txt文件中的内容
with open('1.txt','r') as f:
    p_content = f.read()
# 将读取的内容转换为base64编码，如果为汉字，需要先转换为gbk编码
a2 = base64.b64encode(p_content.encode('gbk'))
# 将转换后的内容赋值给变量aa
a1 = str(a2,'utf-8')
# 打印aa的值
print(p_content)