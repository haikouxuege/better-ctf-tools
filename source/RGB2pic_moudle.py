#-*- coding:utf-8 -*-
from PIL import Image
import re

def RGB2pic_main():
    print('请先用因数分解(被分解数为RGB.txt行数)，计算可能的尺寸x,y')
    x = int(input('x=')) #x坐标  通过对txt里的行数进行整数分解
    y = int(input('y=')) #y坐标  x*y = 行数

    im = Image.new("RGB",(x,y))#创建图片
    file = open('./RGB.txt') #打开rbg值文件

    #通过一个个rgb点生成图片
    for i in range(0,x):
        for j in range(0,y):
            line = file.readline()#获取一行
            rgb = line.split(",")#分离rgb
            im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素

    im.save('RGB2pic.png','png')
    print('Save as RGB2pic.png')

if __name__ == "__main__":
    RGB2pic_main()
