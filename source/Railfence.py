# _*_ coding=UTF-8 _*_

from pycipher import Railfence

'''有误
def Rail_encode(string, key):
    a = Railfence(int(key)).encipher(string)
    return a
'''

def Rail_decode(e, f):
    elen = len(e)
    b = elen / f
    result = {x: '' for x in range(int(b))}
    for i in range(elen):
        a = i % b;
        result.update({a: result[a] + e[i]})
    d = ''
    for i in range(int(b)):
        d = d + result[i]
    print('分为\t', str(f), '\t', '栏时，解密结果为： ', d)


def Rail_brute(string):
    elen = len(string)
    field = []  # field 为所有可能的栏数
    for i in range(2, elen):
        if (elen % i == 0):
            field.append(i)
    for f in field:
        b = Rail_decode(string, f)
        #print('分为\t', str(f), '\t', '栏时，解密结果为： ', b)