'''
1.提示输入打印内容
2.将输入的内容转换为base64编码，如果为汉字，需要先转换为gbk编码
3.将转换后的内容赋值给变量p_content
'''
# 导入base64模块
import base64
# 提示输入打印内容
p_content = input('请输入打印内容：')
# 将输入的内容转换为base64编码，如果为汉字，需要先转换为gbk编码
p_content = base64.b64encode(p_content.encode('gbk'))
# 将转换后的内容赋值给变量p_content
p_content = str(p_content,'utf-8')
# 打印p_content的值
print(p_content)