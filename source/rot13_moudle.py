#_*_ coding=UTF-8 _*_
def rot13_moudle_main():
    string =input('string:')
    new_str = ''
    rot = 13
    for i in string:
        if i>='a' and i<='z':
            i = ord(i)
            i = ((i-rot)-97)%26+97
            i = chr(i)
            new_str = new_str+i
            print(new_str)

if __name__ == "__main__":
    rot13_moudle_main()
