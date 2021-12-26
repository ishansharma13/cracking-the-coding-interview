def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])

if __name__ == '__main__':
    s = "HELLO   WORLD"
    print(lengthOfLastWord(s))