'''
1.定义变量head_1、headd_2、head_3、head_4、head_5,值分别为--------------------------------、       -----CRAC HAM-----、       ------BD4VUG------、       -------INFO-------、       -------------------
2.将变量head_1、headd_2、head_3、head_4、head_5的值拼接起来，中间用换行符连接，赋值给变量head，head的类型为string
'''
head_1 = '--------------------------------'
head_2 = '       -----CRAC HAM-----'
head_3 = '       ------BD4VUG------'
head_4 = '       ---QSL/SWL GIST---'
head_5 = '   --------------------------'
head_6 = head_1 + '\n' + head_2 + '\n' + head_3 + '\n' + head_4 + '\n' + head_5
# 将head_6转化为string形式，存入head
head = str(head_6)
print(head)