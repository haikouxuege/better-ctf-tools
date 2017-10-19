# _*_ coding:UTF-8 _*_
from source import md5_moudle,MD5_online_crack,b64_moudle,caesar,Railfence,ascii_brute_moudle,rot13_moudle,RGB2pic_moudle,factorization_moudle,num_to_QR_moudle
from source.morse_moudle import Morse
import urllib.request

def begin():
    print('''
 _          _   _             ____ _____ _____ _____ ___   ___  _     
| |__   ___| |_| |_ ___ _ __ / ___|_   _|  ___|_   _/ _ \ / _ \| |___ 
| '_ \ / _ \ __| __/ _ \ '__| |     | | | |_    | || | | | | | | / __|
| |_) |  __/ |_| ||  __/ |  | |___  | | |  _|   | || |_| | |_| | \__ \

|_.__/ \___|\__|\__\___|_|   \____| |_| |_|     |_| \___/ \___/|_|___/


+---------------------------------------------------------------------------------+
|        1.MD5加密                  10.栅栏解密            19.01字符串转换二维码  |
|        2.MD5在线解密              11.栅栏爆破            20.utf9转utf8          |
|        3.Base64加密               12.字符串反转                                 |
|        4.Base64解密               13.URL编码                                    |
|        5.Morse加密                14.URL解码                                    |
|        6.Morse解密                15.ascii位移解密                              |
|        7.Caesar加密               16.rot13编解码                                |
|        8.Caesar解密               17.RGB值转图片                                |
|        9.Caesar爆破               18.因数分解                                   |
+---------------------------------------------------------------------------------+
    ''')
    fun_choice = input('选择：')
    return int(fun_choice)

def URLDecode():
    a = input("URL:")
    b = urllib.request.quote(a,encoding='UTF-8')
    print(b)

def URLEncode():
    a = input("url:")
    b = urllib.request.unquote(a,encoding='UTF-8')
    print(b)


def reverse():
    a = input('需要反转的字符串:')
    b = a[::-1]
    print(b)

def md5():
    a = input('需要加密的字符串:')
    b = md5_moudle.md5_encode(a)
    print("MD5('%s'):%s" % (a, b))


def md5_net():
    b = input("需要解密的字符串:")
    a = MD5_online_crack.md5_online_crack(b) #实例化对象
    try:
        print("www.dmd5.com解密中...")
        a.dmd5_online()
    except:
        print("连接到dmd5.com失败...")

    try:
        print("http://pmd5.com解密中...")
        a.pmd5_online()
    except:
        print("连接到pmd5.com失败...")

def b64de():
    string = input('需解密的字符串：')
    a = b64_moudle.b64decode(string)
    print(a)


def b64en():
    string = input('需加密字符串：')
    a = b64_moudle.b64encode(string)
    print(a)


def morse_en():
    a = Morse()
    b = a.morse_en()
    for i in b:
        print(i, end=' ')


def morse_de():
    a = Morse()
    b = a.morse_de()
    for i in b:
        print(i, end='')


def caesar_en():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_encode(a, key)
    print(b)


def caesar_de():
    a = input('String=')
    key = input('key=')
    b = caesar.caesar_decode(a, key)
    print(b)


def caesar_brute():
    a = input('String=')
    caesar.caesar_brute(a)


def raildecode():
    string = input('String=')
    key = input('key=')
    Railfence.Rail_decode(string, key)


def railbrute():
    string = input('String=')
    Railfence.Rail_brute(string)

def ascii_brute():
    filename=input('(ASCII码一行一个)\nfilename=')
    ascii_brute_moudle.ascii_brute_main(filename)

def rot_encode():
    rot13_moudle.rot13_moudle_main()

def RGB2pic():
    RGB2pic_moudle.RGB2pic_main()

def factorization():
    num = int(input('num=:'))
    factorization_moudle.fac(num)

def num_to_QRcode():
    filename=input('filename=')
    num_to_QR_moudle.num_to_QR_main(filename)

def main():
    try:
        while True:
            main_choice = begin()
            if main_choice == 1:
                md5()
            elif main_choice == 2:
                md5_net()
            elif main_choice == 3:
                b64en()
            elif main_choice == 4:
                b64de()
            elif main_choice == 5:
                morse_en()
            elif main_choice == 6:
                morse_de()
            elif main_choice == 7:
                caesar_en()
            elif main_choice == 8:
                caesar_de()
            elif main_choice == 9:
                caesar_brute()
            elif main_choice == 10:
                raildecode()
            elif main_choice == 11:
                railbrute()
            elif main_choice == 12:
                reverse()
            elif main_choice == 13:
                URLDecode()
            elif main_choice == 14:
                URLEncode()
            elif main_choice == 15:
                ascii_brute()
            elif main_choice == 16:
                rot_encode()
            elif main_choice == 17:
                RGB2pic()
            elif main_choice == 18:
                factorization()
            elif main_choice == 19:
                num_to_QRcode()
            elif main_choice == 20:
                utf9_to_utf8()
            elif main_choice == 0:
                exit(0)

            again = input('\n继续？(T/F)').upper()
            if again == 'F':
                break
    except Exception as e:
        print(e)
        print('异常中止')



if __name__ == '__main__':
    main()
