'''
1.定义变量b2、b3、b4、b5、b6、b7、b8、b9、b10、b11、b12、b13、b14、b15、b16，值分别为：RIG ： ,ANT ：,IPT ：,W X ：,TEMP：,DATE：,UTCs：,UTCe：,MHZ ：,MODE：,C S ：,RST ：,QSL ：,O P ：,      -----abstract-----
2.从memo_uitest.py中获取c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16的定义
3.将变量b2和a2、b3和a3、b4和a4、b5和a5、b6和a6、b7和a7、b8和a8、b9和a9、b10和a10、b11和a11、b12和a12、b13和a13、b14和a14、b15和a15、b16和a16的值各自分别拼接成15个字符串，分别存储到c2、c3、c4、c5、c6、c7、c8、c9、c10、c11、c12、c13、c14、c15、c16中
4.将变量c1、c2、c3、c4、c5、c6、c7、c8、c9、c10、c11、c12、c13、c14、c15、c16的值拼接成一个字符串，中间用换行符连接，赋值给变量d1和d2
'''
# 导入base64模块
import base64
# 定义变量b2、b3、b4、b5、b6、b7、b8、b9、b10、b11、b12、b13、b14、b15、b16，，值分别为：RIG ： ,ANT ：,IPT ：,W X ：,TEMP：,DATE：,UTCs：,UTCe：,MHZ ：,MODE：,C S ：,RST ：,QSL ：,O P ：,      -----abstract-----
b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16 = 'RIG ：','ANT ：','IPT ：','W X ：','TEMP：','DATE：','UTCs：','UTCe：','MHZ ：','MODE：','C S ：','RST ：','QSL ：','O P ：','       -----abstract-----'
# 从memo_uitest.py中获取c1、a2、a3、a4、a5、a6、a7、a8、a9、a10、a11、a12、a13、a14、a15、a16的定义
from memo_uitest import c1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16
# 将变量b2和a2、b3和a3、b4和a4、b5和a5、b6和a6、b7和a7、b8和a8、b9和a9、b10和a10、b11和a11、b12和a12、b13和a13、b14和a14、b15和a15、b16和a16的值各自分别拼接成15个字符串，分别存储到c2、c3、c4、c5、c6、c7、c8、c9、c10、c11、c12、c13、c14、c15、c16中
c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16 = b2+a2,b3+a3,b4+a4,b5+a5,b6+a6,b7+a7,b8+a8,b9+a9,b10+a10,b11+a11,b12+a12,b13+a13,b14+a14,b15+a15,b16+'\n'+'    '+a16
# 将变量c1、c2、c3、c4、c5、c6、c7、c8、c9、c10、c11、c12、c13、c14、c15、c16的值拼接成一个字符串，中间用换行符连接，赋值给变量info_1和info_2
info_1= c1 + '\n' + c2 + '\n' + c3 + '\n' + c4 + '\n' + c5 + '\n' + c6 + '\n' + c7 + '\n' + c8 + '\n' + c9 + '\n' + c10 + '\n' + c11 + '\n' + c12 + '\n' + c13 + '\n' + c14 + '\n' + c15 + '\n' + '\n' + c16
info_2 = c1+'\n'+c2+'\n'+c3+'\n'+c4+'\n'+c5+'\n'+c6+'\n'+c7+'\n'+c8+'\n'+c9+'\n'+c10+'\n'+c11+'\n'+c12+'\n'+c13+'\n'+c14+'\n'+c15+'\n'+c16
# 将变量info_1和info_2的值分别转化为string形式，赋值给变量info_1和info_2
info_1 = str(info_1)
info_2 = str(info_2)
print(info_1)