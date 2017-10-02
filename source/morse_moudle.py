# _*_ coding:UTF-8 _*_


class Morse(object):
    def __init__(self):
        file = open('./source/morse_dic.txt', 'r', encoding='utf8')

        self.sum_char = []
        for i in file.readlines():
            self.sum_char.append(i.strip())

        self.items = []
        for j in range(0,len(self.sum_char),2):
            self.items.append(self.sum_char[j])

        self.values = []
        for k in range(1,len(self.sum_char),2):
            self.values.append(self.sum_char[k])
        #print(self.values)
        #print(self.items)

    def morse_en(self):
        string = input('输入加密字符串\n')
        ok = []
        for i in string.upper():
            for k in range(len(self.items)):
                if i == self.items[k]:
                    ok.append(self.values[k])

        return ok

    def morse_de(self):
        a = input('解密字符串以空格隔开\n')
        b = a.split()
        ok = []
        for i in b:
            for k in range(len(self.values)):
                if self.values[k] == i:
                    ok.append(self.items[k])

        return ok
