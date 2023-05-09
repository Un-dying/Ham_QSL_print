'''
1.提示用户输入图片路径，去除首尾各一个字符，存为变量pic_path
2.获得图片的jpg或者pngbase64编码，存为变量pic_jpgpng
3.打印pic_jpgpng
4.把pic_jpgpng赋值给变量imgBase64String，类型为string
5.从memo2.py中导入变量a_key，存为变量ak
6.以post方法请求url，url地址为http://open.memobird.cn/home/getSignalBase64Pic?ak=dddddd&imgBase64String=imgBase64
'''
# 1.提示用户输入图片路径，去除首尾各一个字符，存为变量pic_path
pic_path = input('请输入图片路径：')[1:-1]
# 2.获得图片的jpg或者pngbase64编码，存为变量pic_jpgpng
import base64
with open(pic_path,'rb') as f:
    pic_jpgpng = base64.b64encode(f.read())
# 3.打印pic_jpgpng
#print(pic_jpgpng)
# 4.把pic_jpgpng赋值给变量imgBase64String，类型为string
imgBase64 = pic_jpgpng.decode('utf-8')
#print(imgBase64)
# 5.从memo2.py中导入变量a_key，存为变量ak
from memo2 import a_key
ak = a_key
# 6.以post方法请求url，url地址为http://open.memobird.cn/home/getSignalBase64Pic?ak=dddddd&imgBase64String=imgBase64
import requests
url = 'http://open.memobird.cn/home/getSignalBase64Pic?ak='+ak+'&imgBase64String='+imgBase64
r = requests.get(url)
print(r.text)
print(url)