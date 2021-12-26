def reversedSting(s):
    x = ''
    for i in range(len(s)-1,-1,-1):
        x+=s[i]
    return x

if __name__ == '__main__':
    s = "hi there"
    print(reversedSting(s))