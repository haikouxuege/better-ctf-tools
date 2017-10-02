# _*_ coding:UTF-8 _*_
'''
使用requests得到POST后的使用BeautifulSoup 来解析并得到解密后的信息

最好加上请求头  Cookie(?)

'''


import re
import requests
# 注意 requests中post的数据必须是原本的数据
#不能被urlencode过  （来自被坑了的作者的忠告）
from bs4 import BeautifulSoup


class md5_online_crack(object):
    def __init__(self,md5):
        self.md5 = md5

    def dmd5_online(self):
        data = {'_VIEWRESOURSE':'c4c92e61011684fc23405bfd5ebc2b31','result':'c1fa08ee052e00e5b8e7527f9211d9c0453bc6f335a6181f2f58c7816f79278e75b69a1b7b15134cf0c8e85babf20959a886cf755794b796d9313ae57cbe48d6ac8eb7d2b168fff553584bff499fd06bd9dd0dbef033481c9a0609c9208ac7fe5449d50bd300580c2f85ed40a13f7b7cb52544a8a54f53c0cd6d65abf92be35e087578f55212be438fd6c238acaafbce81ef24d38e688395'}
        data['md5'] = self.md5
        r = requests.post('http://www.dmd5.com/md5-decrypter.jsp', data=data)
        bsOBJ = BeautifulSoup(r.text,'html.parser')
        nameList = bsOBJ.findAll('p')
        for i in nameList:
            m = re.search('解密结果：[0-9]*',str(i))
            if m:
                print(m.group(0))

    def pmd5_online(self):
        # 除了key以外要post的数据
        data = {'__VIEWSTATE':'/wEPDwUKMTM4NTE3OTkzOWRkP4hmXYtPPhcBjbupZdLOLfmeTK4=','__VIEWSTATEGENERATOR':'CA0B0334','__EVENTVALIDATION':'/wEWAwK75ZuyDwLigPTXCQKU9f3vAheUenitfEuJ6eGUVe2GyFzb7HKC','jiemi':'MD5解密'}
        data['key'] = self.md5
        r = requests.post('http://pmd5.com/#',data=data)
        bsOBJ = BeautifulSoup(r.text,'html.parser')
        nameList = bsOBJ.findAll('em')
        i = str(nameList[1])
        print(i[4:-5])

def test():
    a = md5_online_crack('887BF855FE35AFA4598232AC82880463')
    a.dmd5_online()
    a.pmd5_online()

if __name__ == '__main__':
    test()
