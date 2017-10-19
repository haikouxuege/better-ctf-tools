def ascii_brute_main(filename):
    with open(filename) as f:
        line = []
        for each in f:
            line.append(int(each[:-1]))

    print(line)
    flag = ''
    length = len(line)
    for j in range(26):
        for i in line:
            i+=j
            flag+=chr(i)
        print('位移{0}时，flag:{1}'.format(j+1,flag))
        print('-----------------------------------------')
        flag=''

if __name__ == "__main__":
    ascii_brute_main()
