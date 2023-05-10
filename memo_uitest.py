'''
1.弹出一个有16个输入框的对话框s1
2.输入框名称分别为：类型、RIG、ANT、IPT、WX、TEMP、DATE、UTCs、UTCe、MHZ、MODE、CALLSIGN、RST、QSL、OP、SUMMARY
3.提示在输入框中输入内容，内容分别存入变量c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16中
4.检查c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16是否有空值，如果有空值，为uitest_1赋值为1，如果没有空值，为uitest_1赋值为0
5.如果uitest_1的值为1，重新运行本文件，恢复已填写内容，弹出对话框，提示有未填写内容，直至uitest_1的值为0
6.如果uitest_1的值为0，打印hello world
'''
# 导入easygui模块
import easygui
# 弹出一个有16个输入框的对话框
s1 = easygui.multenterbox('请输入信息','Hrecord',['类型','RIG','ANT','IPT','WX','TEMP','DATE','UTCs','UTCe','MHZ','MODE','CALLSIGN','RST','QSL','OP','SUMMARY'])
# 将输入框的值分别存入变量c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16中
c1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16 = s1
# 判断c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16是否有空值
if c1 == '' or a2 == '' or a3 == '' or a4 == '' or a5 == '' or a6 == '' or a7 == '' or a8 == '' or a9 == '' or a10 == '' or a11 == '' or a12 == '' or a13 == '' or a14 == '' or a15 == '' or a16 == '':
    # 如果有空值，为uitest_1赋值为1
    uitest_1 = 1
else:
    # 如果没有空值，为uitest_1赋值为0
    uitest_1 = 0
# 判断uitest_1的值是否为1

# 判断uitest_1的值是否为1
if uitest_1 == 1:
    # 如果uitest_1的值为1，恢复已填写内容，弹出对话框，提示有未填写内容，直至uitest_1的值为0
    while uitest_1 == 1:
        easygui.msgbox('有未填写内容，请重新填写')
#        exec(open('memo_uitest.py').read())
        s1 = easygui.multenterbox('请输入信息','Hrecord',['类型','RIG','ANT','IPT','WX','TEMP','DATE','UTCs','UTCe','MHZ','MODE','CALLSIGN','RST','QSL','OP','SUMMARY'],s1)
        c1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16 = s1
        if c1 == '' or a2 == '' or a3 == '' or a4 == '' or a5 == '' or a6 == '' or a7 == '' or a8 == '' or a9 == '' or a10 == '' or a11 == '' or a12 == '' or a13 == '' or a14 == '' or a15 == '' or a16 == '':
            uitest_1 = 1
        else:
            uitest_1 = 0
# 如果uitest_1的值为0，打印hello world
    # 如果uitest_1的值为1，重新运行本文件，恢复已填写内容
    # 弹出对话框，提示有未填写内容
else:
    # 如果uitest_1的值为0，打印hello world
    print('hello world')