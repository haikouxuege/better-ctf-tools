# better-ctf-tools
更好的ctf密码学加解密及编解码工具，持续更新

在该项目基础上更改：https://github.com/Ollyder/CTF_tools

运行截图：

![](./1.png)

部分解题结果：

01转换成二维码：

![](./0101.txt_to_QR.png)

RGB转换图片：

![](./RGB2pic.png)

## 环境
Linux Python 3.x

## 所需Python模块及安装

* pycipher
```
pip3 install pycipher
```
* Pillow
```
pip3 install Pillow
```
* utf9
```
pip3 install utf9
```

## 使用
python3 CTFtools.py

## 当前版本功能
* MD5加密以及进行MD5在线解密
* Base64加解密
* 摩斯密码加解密
* 凯撒密码加解密以及爆破
* 栅栏密码加解密以及爆破
* 字符串反转
* URL编码解码
* 位移密码解密
* ROT13解码
* RGB值转换图片
* 整数分解
* 01字符串转二维码
* utf9转utf8

## 文件说明
* ./source/morse_dic.txt 为摩斯电码表
* 0101.txt 为"01字符串转二维码"示例，"0101.txt\_to\_QR.png"是示例结果
* ascii.txt 为"ascii位移解密"示例
* RGB.txt 为"RGB值转图片"示例，"RGB2pic.png"是示例结果

## 当前版本
v1.1.2

## 更新说明
修复一些小问题，增加新功能
