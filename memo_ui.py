'''
1.使用tkinter弹出一个对话框，提示输入打印内容
'''
# 导入tkinter模块
import tkinter as tk
# 导入tkinter.messagebox模块
import tkinter.messagebox as msgbox
# 导入base64模块
import base64
# 创建一个窗口
window = tk.Tk()
# 设置窗口标题
window.title('打印内容')
# 设置窗口大小
window.geometry('300x200')
# 设置窗口位置
window.geometry('+500+200')
# 设置窗口图标
# 设置窗口是否可变长、宽，True：可变，False：不可变
window.resizable(width=True,height=True)
# 创建一个标签，用于显示提示信息
label = tk.Label(window,text='请输入打印内容：')
# 将标签放置到窗口中
label.pack()
# 创建一个输入框，用于输入打印内容
entry = tk.Entry(window)
# 将输入框放置到窗口中
entry.pack()
# 创建一个按钮，用于触发打印
button = tk.Button(window,text='打印')
# 将按钮放置到窗口中
button.pack()
# 创建一个函数，用于打印
def print_content():
    # 获取输入框中的内容
    p_content = entry.get()
    # 将输入的内容转换为base64编码，如果为汉字，需要先转换为gbk编码
    p_content = base64.b64encode(p_content.encode('gbk'))
    # 将转换后的内容赋值给变量p_content
    p_content = str(p_content,'utf-8')
    # 打印p_content的值
    print(p_content)
    # 弹出一个对话框，提示打印成功
    msgbox.showinfo('提示','打印成功')
# 绑定按钮的单击事件，触发打印函数
button.config(command=print_content)
# 进入消息循环
window.mainloop()
# Compare this snippet from memo_ui.py:
# '''