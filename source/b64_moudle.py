# _*_ coding:UTF-8 _*_
# b64 decode and encode

import base64


def b64encode(string):
    a = base64.b64encode(string.encode())
    return a.decode()


def b64decode(string):
    a = base64.b64decode(string).decode()
    return a
