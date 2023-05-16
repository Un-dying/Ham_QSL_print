'''
1.定义变量a，值为Qk0OAgAAAAAAAD4AAAAoAAAAOgAAAMb///8BAAEAAAAAAAAAAADEDgAAxA4AAAIAAAACAAAAAAAA//////8A///////AAAP///////AAB///////+AAf///////+AB////////4AP///++/f/wB////719//gH///frv/+A////+7ff/8D////779//wP/////37//A////9dW//8D////6rV//wP////a1r//A////+1bf/8D////7/7//wP/////////A/////qr//8D////7/1//wP////aq7//A////3/+1/8D////1VX//wP///17v1f/A////67q+v8D///1d3ev/wP////a3XX/A///9X/73v8D///+1R7rfwP//7XvG17/A//+21u9978D//1v/vda/wP/+6qr2+9/A//1bfbtW78D/263Xb/2/wP/9arvaq2/A/3vV7Xff38D//f63vXV/wP23/93Xvt/A///f9vrV78D/33/dr39fwP19+/d11f/A//f/+77uv8D//9/t1bv/wP/e//b/bX/A//v//1Xf/8D//7/q7vX/wP////e7X//A//7/3W3v/8D////333//wP///9r1v//Af///717//4B///+76///gD///+1///8AH////////gAf///////+AAf///////gAA///////8AAA///////AAA==
2.base64图片还原
'''
import os,base64 
strs = '/9jQk0OAgAAAAAAAD4AAAAoAAAAOgAAAMb///8BAAEAAAAAAAAAAADEDgAAxA4AAAIAAAACAAAAAAAA//////8A///////AAAP///////AAB///////+AAf///////+AB////////4AP///++/f/wB////719//gH///frv/+A////+7ff/8D////779//wP/////37//A////9dW//8D////6rV//wP////a1r//A////+1bf/8D////7/7//wP/////////A/////qr//8D////7/1//wP////aq7//A////3/+1/8D////1VX//wP///17v1f/A////67q+v8D///1d3ev/wP////a3XX/A///9X/73v8D///+1R7rfwP//7XvG17/A//+21u9978D//1v/vda/wP/+6qr2+9/A//1bfbtW78D/263Xb/2/wP/9arvaq2/A/3vV7Xff38D//f63vXV/wP23/93Xvt/A///f9vrV78D/33/dr39fwP19+/d11f/A//f/+77uv8D//9/t1bv/wP/e//b/bX/A//v//1Xf/8D//7/q7vX/wP////e7X//A//7/3W3v/8D////333//wP///9r1v//Af///717//4B///+76///gD///+1///8AH////////gAf///////+AAf///////gAA///////8AAA///////AAA=='

imgdata=base64.b64decode(strs)
file=open('1.png','wb')
file.write(imgdata)
file.close()
