# _*_ coding:UTF-8 _*_
# md5_moudle

import hashlib


def md5_encode(string):
    a = hashlib.md5()
    a.update(string.encode()) # 加密bytes类型
    return a.hexdigest()